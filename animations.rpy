init python:

    ## Petit saut sur place (ex. : surprise)
    ##
    ## Utilisation dans le script :
    ##     show eileen at hop                  # saut par défaut
    ##     show eileen at hop(80)              # saut plus haut (80 px)
    ##     show eileen at hop(h=80, up=0.08)   # plus haut et montée plus sèche
    ##
    ## Sans changer la position du personnage.
    ## Si tu veux la fixer : show eileen at right, hop

    transform hop(h=40, up=0.12, down=0.18):
    yoffset 0
    easeout_quad up yoffset -h      # monte vite, ralentit au sommet
    easein_quad down yoffset 0      # retombe en accélérant, comme la gravité


    transform hop_bounce(h=50):
    yoffset 0
    easeout_quad 0.12 yoffset -h
    easein_quad 0.16 yoffset 0
    easeout_quad 0.06 yoffset -h/4      # petit rebond
    easein_quad 0.07 yoffset 0



    def _sprite_x(trans):
        """Position horizontale du sprite en fraction de l'écran (0.0 = gauche, 1.0 = droite)."""
        x = trans.xpos
        if x is None:                       # position définie par une autre transform (ex. "right")
            try:
                x = trans.child.get_placement()[0]
            except Exception:
                x = None
        if x is None:
            return 0.5
        if isinstance(x, int):              # pixels -> fraction
            x = x / float(config.screen_width)
        return x

    class ShiftX(object):
        """Décale le sprite en xoffset vers le centre ou vers le bord le plus proche."""
        def __init__(self, dx, duration, mode, side=None):
            self.dx = dx
            self.duration = max(duration, 0.001)
            self.mode = mode                # "center" ou "edge"
            self.side = side                # "left" / "right" : pour un perso pile au centre
            self.start = None
            self.target = 0
            self.last_st = 0.0

        def __call__(self, trans, st, at):
            if self.start is None or st < self.last_st:     # (ré)initialisation
                self.start = trans.xoffset or 0
                x = _sprite_x(trans)
                to_center = 1 if x < 0.49 else (-1 if x > 0.51 else 0)
                if self.mode == "center":
                    direction = to_center
                elif to_center != 0:
                    direction = -to_center
                else:
                    direction = -1 if self.side == "left" else 1
                self.target = direction * self.dx
            self.last_st = st

            p = min(st / self.duration, 1.0)
            k = _warper.ease_cubic(p)
            trans.xoffset = int(round(self.start + (self.target - self.start) * k))

            if p >= 1.0:
                self.start = None           # prêt pour la prochaine utilisation
                return None
            return 0

    def _init_brightness(trans, st, at):
        # Sans matrice de départ, le fondu vers l'assombrissement ne s'interpole pas
        if trans.matrixcolor is None:
            trans.matrixcolor = BrightnessMatrix(0.0)
        return None

## Vers le centre de l'écran, et éclaircit à la luminosité normale
##     show eileen at highlight
##     show eileen at highlight(dx=60, t=0.4)
transform highlight(dx=30, t=0.25):
    function _init_brightness
    parallel:
        function ShiftX(dx, t, "center")
    parallel:
        linear t matrixcolor BrightnessMatrix(0.0)

## Vers le bord le plus proche, et assombrit
##     show eileen at cover
##     show eileen at cover(dx=40, t=0.3, dark=0.35)
##     show eileen at cover(side="left")     # seulement si le perso est pile au centre
transform cover(dx=30, t=0.25, dark=0.25, side=None):
    function _init_brightness
    parallel:
        function ShiftX(dx, t, "edge", side)
    parallel:
        linear t matrixcolor BrightnessMatrix(-dark)

## Retour à la position et à la luminosité normales
transform neutral(t=0.25):
    function _init_brightness
    parallel:
        function ShiftX(0, t, "center")
    parallel:
        linear t matrixcolor BrightnessMatrix(0.0)