# ==============================================================================
# ILLUSTRATIONS, CARTE TITRE ET ANIMATION "FIGURE IT OUT"
# ------------------------------------------------------------------------------
# NB : aucun screen "illus" n'existait dans les fichiers fournis, il est donc
# défini ici. Si tu en as déjà un ailleurs, supprime-le d'ici et adapte les
# appels  show screen illus("images/illus/xxx.png")  à sa signature.
# ==============================================================================

## Dossier supposé des illustrations : game/images/illus/
## Hauteur de la zone d'illustration : tout l'écran par défaut.
## Mets DLG_TOP pour que l'illustration s'arrête au-dessus du cadre de dialogue.
define ILLUS_H = config.screen_height


# ------------------------------------------------------------------------------
# SCREEN ILLUS
# ------------------------------------------------------------------------------
## Usage :
##     show screen illus("images/illus/shed_message.png") with dissolve
##     ...dialogue...
##     hide screen illus with dissolve
## L'écran est sur la couche "master" : au-dessus des sprites, mais sous le
## cadre de dialogue (couche "dialogue"), qui reste donc lisible.
## Rappeler "show screen illus(autre image)" remplace l'image en place.
screen illus(img, bg="#000000"):
    layer "master"
    zorder 60

    fixed:
        xsize config.screen_width
        ysize ILLUS_H

        add Solid(bg)
        add img:
            fit "contain"
            xysize (config.screen_width, ILLUS_H)
            xalign 0.5
            yalign 0.5


# ------------------------------------------------------------------------------
# CARTE TITRE DU JEU
# ------------------------------------------------------------------------------
## Séquence complète (entrée, maintien, sortie) gérée par l'ATL lui-même :
## l'écran est invisible à la fin même si l'événement "hide" n'est jamais reçu.
define TITLE_DURATION = 4.2

transform card_fade:
    alpha 0.0
    linear 0.9 alpha 1.0
    pause TITLE_DURATION - 1.8
    linear 0.9 alpha 0.0

transform title_rise:
    alpha 0.0
    yoffset 24
    pause 0.5
    parallel:
        ease 1.2 alpha 1.0
    parallel:
        ease 1.6 yoffset 0

transform title_line:
    xzoom 0.0
    pause 1.0
    ease 1.2 xzoom 1.0

screen title_card(title="NOVEMBER DAWNS"):
    layer "overlay"
    zorder 300
    modal True

    fixed at card_fade:
        add Solid("#000000")

        vbox:
            xalign 0.5
            yalign 0.45
            spacing 28

            text title:
                xalign 0.5
                size 120
                color "#ffffff"
                kerning 10
                outlines [ (0, "#33dbe7", 4, 4) ]
                at title_rise

            add Solid("#33dbe7"):
                xysize (700, 6)
                xalign 0.5
                at title_line

    ## Filet de sécurité : l'écran se retire tout seul à la fin.
    timer TITLE_DURATION action Function(renpy.hide_screen, "title_card", layer="overlay")

label show_game_title:
    show screen title_card
    $ renpy.pause(TITLE_DURATION, hard=True)
    $ renpy.hide_screen("title_card", layer="overlay")
    return


# ------------------------------------------------------------------------------
# ANIMATION "FIGURE IT OUT" (avant chaque contre-interrogatoire)
# ------------------------------------------------------------------------------
## Les lettres apparaissent une à une (petit rebond), puis un trait cyan
## (#33dbe7, la couleur du cadre de dialogue) se déploie sous le texte.
define FIO_DURATION = 2.7

transform fio_root:
    alpha 0.0
    linear 0.2 alpha 1.0
    pause FIO_DURATION - 0.55
    linear 0.35 alpha 0.0

transform fio_letter(d=0.0):
    alpha 0.0
    yoffset 60
    pause d
    parallel:
        easeout 0.2 alpha 1.0
    parallel:
        easeout_back 0.35 yoffset 0

transform fio_bar:
    xzoom 0.0
    pause 1.1
    easeout 0.5 xzoom 1.0

screen figure_it_out(words=("FIGURE", "IT", "OUT")):
    zorder 120

    fixed at fio_root:
        add Solid("#000000a0")

        $ n = 0
        hbox:
            xalign 0.5
            yalign 0.38
            spacing 40

            for wi, w in enumerate(words):
                hbox:
                    for ch in w:
                        text ch:
                            size 120
                            bold True
                            color ("#33dbe7" if wi == len(words) - 1 else "#ffffff")
                            outlines [ (5, "#06282b", 0, 0) ]
                            at fio_letter(n * 0.07)
                        $ n += 1

        add Solid("#33dbe7"):
            xysize (880, 8)
            xalign 0.5
            yalign 0.52
            at fio_bar

    timer FIO_DURATION action Function(renpy.hide_screen, "figure_it_out")

## À appeler juste avant le "$ current_cx = CrossExamination(...)" :
##     call figure_it_out_anim
label figure_it_out_anim:
    show screen figure_it_out
    $ renpy.pause(FIO_DURATION, hard=True)
    hide screen figure_it_out
    return
