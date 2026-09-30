default last_speaker = None

init -1 python:

    _cls = renpy.character.ADVCharacter

    # Garde l'original une seule fois (évite l'empilement au rechargement Shift+R)
    if not hasattr(_cls, "_unpaged_call"):
        _cls._unpaged_call = _cls.__call__

    def _paged_call(self, what, *args, **kwargs):
        # Mémorise le dernier personnage nommé (le narrateur est ignoré)      
        store.last_speaker = self

        pages = split_pages(what)
        last = len(pages) - 1
        for i, page in enumerate(pages):
            kw = dict(kwargs)
            if i < last:
                kw["interact"] = True    # force le clic entre les pages
            _cls._unpaged_call(self, page, *args, **kw)

    _cls.__call__ = _paged_call

    TEXT_W = 1100   # largeur utile du texte (= xsize du style say_dialogue)
    TEXT_H = 150    # hauteur utile de la zone de texte

    def _fits(text):
        t = renpy.text.text.Text(text, style="say_dialogue")
        w, h = renpy.render(t, TEXT_W, 10000, 0, 0).get_size()
        return h <= TEXT_H

    def split_pages(what):
        what = renpy.substitute(what)    # résout les [variables]
        if _fits(what):
            return [what]

        pages = []
        current = ""
        for word in what.split(" "):
            candidate = (current + " " + word).strip()
            if current and not _fits(candidate):
                pages.append(current)
                current = word
            else:
                current = candidate
        if current:
            pages.append(current)
        return pages