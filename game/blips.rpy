## blips.rpy — Système de « blips » (bips de dialogue) pour Ren'Py 8.x
##
## Chaque personnage reçoit sa propre voix (BlipVoice) :
##   sound         chemin d'un .wav 16 bits (None = son synthétisé par défaut)
##   pitch         hauteur : 1.0 = normale, 2.0 = octave au-dessus, 0.5 = en dessous
##   pitch_var     variation aléatoire relative du pitch (0.1 = ±10 %)
##   volume        0.0 à 1.0 (se combine avec le volume du mixer)
##   frequency     1 blip toutes les N lettres (1 = chaque lettre, 2 = une sur deux…)
##   cps           vitesse propre à cette voix (None = préférence du joueur)
##   tone/shape    hauteur en Hz et forme d'onde du son synthétisé par défaut
##                 ("square", "sine", "triangle", "saw", "noise")
##   duration      durée du son synthétisé, en secondes
##   min_interval  écart minimal entre deux blips (évite la mitraillette à cps élevé)
##
## Synchronisation : le texte du dialogue est analysé avant l'affichage.
## Les balises {w}, {w=1.0}, {p}, {p=1.0}, {cps=30}, {cps=*2}, {/cps}, {fast}
## sont prises en compte, ainsi que la vitesse de texte choisie par le joueur.
## Les espaces et la ponctuation ne déclenchent pas de blip.

default persistent.blip_enabled = True

init -10 python:
    import re
    import io
    import copy
    import math
    import wave
    import random
    import collections
    from array import array

    BLIP_MIXER = "sfx"
    BLIP_CHANNEL = "blip"
    BLIP_SILENT = u" \t\r\n.,;:!?…-–—\"'“”‘’«»()[]{}*_/\\¡¿"

    BLIP_DEBUG = False    # passe à False quand tout fonctionne

    def blip_log(msg, notify=False):
        """Écrit dans log.txt et la console (Shift+O), et peut afficher une notification."""
        if not BLIP_DEBUG:
            return
        renpy.log("[blips] " + msg)
        print("[blips] " + msg)
        if notify:
            renpy.notify("[blips] " + msg)

    renpy.music.register_channel(BLIP_CHANNEL, mixer=BLIP_MIXER, loop=False)

    def blip_semitones(n):
        """Convertit des demi-tons en multiplicateur de pitch (ex. +12 -> 2.0)."""
        return 2.0 ** (n / 12.0)


    class BlipState(object):
        # Attributs de classe : volontairement hors du store, donc jamais
        # sauvegardés ni restaurés par le rollback.
        cache = collections.OrderedDict()
        driver = None
        rng = random.Random()


    ## ------------------------------------------------------------------
    ## Génération / traitement audio
    ## ------------------------------------------------------------------

    _BLIP_RATE = 22050

    def _wav_bytes(samples, channels, rate):
        bio = io.BytesIO()
        w = wave.open(bio, "wb")
        w.setnchannels(channels)
        w.setsampwidth(2)
        w.setframerate(rate)
        w.writeframes(samples.tobytes())
        w.close()
        return bio.getvalue()

    def _synth(freq, duration, shape):
        n = max(1, int(_BLIP_RATE * duration))
        attack = max(1, int(_BLIP_RATE * 0.004))
        out = array("h")
        for i in range(n):
            ph = (i * freq / _BLIP_RATE) % 1.0
            if shape == "square":
                s = 1.0 if ph < 0.5 else -1.0
            elif shape == "triangle":
                s = 4.0 * abs(ph - 0.5) - 1.0
            elif shape == "saw":
                s = 2.0 * ph - 1.0
            elif shape == "noise":
                s = BlipState.rng.uniform(-1.0, 1.0)
            else:
                s = math.sin(2.0 * math.pi * ph)
            env = min(1.0, i / float(attack)) * (1.0 - i / float(n))
            out.append(int(s * env * 0.6 * 32767))
        return _wav_bytes(out, 1, _BLIP_RATE)

    def _load_wav(path):
        f = renpy.open_file(path)
        try:
            data = f.read()
        finally:
            f.close()
        w = wave.open(io.BytesIO(data), "rb")
        try:
            ch, sw, rate = w.getnchannels(), w.getsampwidth(), w.getframerate()
            raw = w.readframes(w.getnframes())
        finally:
            w.close()
        if sw != 2:
            return None
        a = array("h")
        a.frombytes(raw)
        return a, ch, rate

    def _blip_source(path):
        key = ("src", path)
        if key not in BlipState.cache:
            try:
                BlipState.cache[key] = _load_wav(path)
            except Exception:
                BlipState.cache[key] = None   # ogg/mp3/etc. : pas de pitch
        return BlipState.cache[key]

    def _resample(samples, channels, pitch):
        """Changement de hauteur par rééchantillonnage (comme une bande qu'on accélère)."""
        frames = len(samples) // channels
        n = int(frames / pitch)
        out = array("h", bytes(n * channels * 2))
        for i in range(n):
            pos = i * pitch
            i0 = int(pos)
            i1 = min(i0 + 1, frames - 1)
            f = pos - i0
            for c in range(channels):
                a = samples[i0 * channels + c]
                b = samples[i1 * channels + c]
                out[i * channels + c] = int(a + (b - a) * f)
        return out


    ## ------------------------------------------------------------------
    ## Voix
    ## ------------------------------------------------------------------

    class BlipVoice(object):
        def __init__(self, sound=None, pitch=1.0, pitch_var=0.08, volume=1.0,
                frequency=2, cps=None, tone=330.0, shape="square",
                duration=0.05, min_interval=0.04, silent=BLIP_SILENT):
            self.sound = sound
            self.pitch = pitch
            self.pitch_var = pitch_var
            self.volume = volume
            self.frequency = max(1, int(frequency))
            self.cps = cps
            self.tone = tone
            self.shape = shape
            self.duration = duration
            self.min_interval = min_interval
            self.silent = silent

        def _build(self, p):
            if self.sound is None:
                data = _synth(self.tone * p, self.duration, self.shape)
                return AudioData(data, "blip.wav")
            if p == 1.0:
                return self.sound
            src = _blip_source(self.sound)
            if src is None:
                blip_log("'%s' n'est pas un WAV 16 bits PCM lisible : joué sans "
                        "changement de pitch (ou introuvable)." % self.sound)
                return self.sound        # format non pitchable : joué tel quel
            a, ch, rate = src
            return AudioData(_wav_bytes(_resample(a, ch, p), ch, rate), "blip.wav")

        def sample(self):
            p = self.pitch
            if self.pitch_var:
                p *= 1.0 + BlipState.rng.uniform(-self.pitch_var, self.pitch_var)
            p = max(0.25, min(4.0, round(p, 2)))   # quantifié -> cache efficace
            key = (self.sound, self.tone, self.shape, self.duration, p)
            audio = BlipState.cache.get(key)
            if audio is None:
                audio = self._build(p)
                BlipState.cache[key] = audio
                if len(BlipState.cache) > 256:
                    BlipState.cache.popitem(last=False)
            return audio

        def check(self):
            """Vérifie une fois que le fichier son existe (signalé si absent)."""
            if self.sound is not None and not renpy.loadable(self.sound):
                blip_log("FICHIER INTROUVABLE : '%s' (chemin relatif à game/, "
                        "casse et extension comprises)" % self.sound, notify=True)
                return False
            return True

        def play(self):
            if not getattr(self, "_checked", False):
                self._checked = True
                self.check()
            vol = max(0.0, min(1.0, self.volume))
            try:
                renpy.music.play(self.sample(), channel=BLIP_CHANNEL, loop=False,
                                relative_volume=vol)
            except Exception as ex:
                blip_log("ERREUR à la lecture de '%s' : %r" % (self.sound, ex), notify=True)


    ## ------------------------------------------------------------------
    ## Planification : texte -> liste de (temps, est_une_attente_clic)
    ## ------------------------------------------------------------------

    _BLIP_TOKEN = re.compile(r"(\{\{)|\{([^{}]*)\}|([^{]+|\{)")

    def blip_schedule(text, base_cps, voice):
        items = []
        t = 0.0
        cps = base_cps
        counter = 0
        last = -99.0
        every = voice.frequency

        for m in _BLIP_TOKEN.finditer(text):
            if m.group(2) is not None:                      # balise {...}
                name, _, arg = m.group(2).partition("=")
                name = name.strip()
                try:
                    if name in ("w", "p"):
                        if arg:
                            t += float(arg)                 # pause chronométrée
                        else:
                            items.append((t, True))         # attend un clic
                        counter = 0                         # 1re lettre après pause = blip
                    elif name == "cps":
                        cps = base_cps * float(arg[1:]) if arg.startswith("*") else float(arg)
                    elif name == "/cps":
                        cps = base_cps
                    elif name == "fast":
                        items = []
                        t, last, counter = 0.0, -99.0, 0
                except ValueError:
                    pass
                continue

            chars = u"{" if m.group(1) else m.group(3)
            for ch in chars:
                if ch not in voice.silent:
                    if counter % every == 0 and t - last >= voice.min_interval:
                        items.append((t, False))
                        last = t
                    counter += 1
                if cps > 0:
                    t += 1.0 / cps

        return items


    ## ------------------------------------------------------------------
    ## Lecteur : affiche les blips au bon moment, image par image
    ## ------------------------------------------------------------------

    class BlipDriver(renpy.Displayable):
        def __init__(self, items, voice, **kwargs):
            super(BlipDriver, self).__init__(**kwargs)
            self.items = items
            self.voice = voice
            self.idx = 0
            self.clock = 0.0
            self.last_st = None
            self.waiting = False      # en pause {w}/{p} sans durée
            self.stopped = False

        def render(self, width, height, st, at):
            if not self.stopped:
                dt = 0.0 if self.last_st is None else max(0.0, st - self.last_st)
                self.last_st = st

                if renpy.is_skipping():
                    self.stopped = True
                elif not self.waiting:
                    self.clock += dt
                    due = False
                    while self.idx < len(self.items):
                        t, is_wait = self.items[self.idx]
                        if t > self.clock:
                            break
                        self.idx += 1
                        if is_wait:
                            self.clock = t
                            self.waiting = True
                            break
                        due = True
                    if due:
                        self.voice.play()    # un seul son par image

                if self.idx >= len(self.items) and not self.waiting:
                    self.stopped = True
                elif not self.waiting:
                    renpy.redraw(self, 0)
            return renpy.Render(1, 1)

        def event(self, ev, x, y, st):
            if self.waiting and renpy.map_event(ev, "dismiss"):
                self.waiting = False
                self.last_st = None
                renpy.redraw(self, 0)
            return None


    def blip_stop():
        d = BlipState.driver
        if d is not None:
            d.stopped = True
            BlipState.driver = None
        if renpy.get_screen("blip_driver"):
            renpy.hide_screen("blip_driver")

    def blip_start(voice):
        what = getattr(renpy.store, "_last_say_what", None)
        if not what:
            blip_log("pas de texte (_last_say_what vide) : aucun blip.")
            return
        try:
            text = renpy.substitute(what)
        except Exception:
            text = what

        cps = voice.cps if voice.cps is not None else preferences.text_cps
        if not cps:          # 0 = texte instantané : pas de blips
            blip_log("cps = 0 (texte instantané, réglage des préférences) : aucun blip.")
            return

        items = blip_schedule(text, float(cps), voice)
        if not items:
            blip_log("aucun blip planifié pour ce texte.")
            return

        blip_log("%d blips planifiés (cps=%s) pour : %s" % (len(items), cps, text[:40]))
        d = BlipDriver(items, voice)
        BlipState.driver = d
        renpy.show_screen("blip_driver", driver=d)

    def blip_callback(event, interact=True, **kwargs):
        voice = kwargs.get("voice") or kwargs.get("cb_voice")
        if event == "show":
            blip_stop()
            if voice is None:
                blip_log("callback appelé sans voix (cb_voice manquant) : utilise BlipCharacter.")
                return
            if persistent.blip_enabled is False:
                blip_log("blips désactivés (persistent.blip_enabled = False).")
                return
            blip_start(voice)
        elif event in ("slow_done", "end"):
            blip_stop()


    ## ------------------------------------------------------------------
    ## Raccourci pour créer un personnage avec sa voix
    ## ------------------------------------------------------------------

    def BlipCharacter(name, voice=None, **kwargs):
        voice = voice or BlipVoice()
        # Respecte un what_slow_cps défini sur le personnage.
        if voice.cps is None and kwargs.get("what_slow_cps"):
            voice = copy.copy(voice)
            voice.cps = kwargs["what_slow_cps"]
        kwargs["callback"] = blip_callback
        kwargs["cb_voice"] = voice
        return Character(name, **kwargs)


## Écran invisible qui porte le lecteur (au-dessus de tout pour recevoir les clics en premier).
screen blip_driver(driver):
    zorder 1000
    add driver


## ----------------------------------------------------------------------
## EXEMPLES (à copier dans ton script)
## ----------------------------------------------------------------------
##
## define e = BlipCharacter("Eileen", voice=BlipVoice(pitch=1.4, volume=0.6, frequency=2))
##
## define l = BlipCharacter("Lucy", voice=BlipVoice(
##     sound="audio/blip_low.wav", pitch=0.8, pitch_var=0.08, frequency=3, volume=0.8))
##
## define r = BlipCharacter("Robot", voice=BlipVoice(shape="saw", tone=180, frequency=1,
##     min_interval=0.06), what_slow_cps=25)
##
## define narrateur = Character(None)   # sans callback = silencieux
##
## Option dans l'écran de préférences :
##     textbutton _("Blips") action ToggleField(persistent, "blip_enabled")
