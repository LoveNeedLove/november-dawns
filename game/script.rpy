label travel_to(destination, in_dialogue=False):
    # Bloque back au début du déplacement
    $ renpy.block_rollback()

    scene black with dissolve
    $ current_room = destination
    show screen room_screen onlayer backgrounds
    $ renpy.checkpoint()

    if current_room.cutscene is not None:
        $ cutscene_to_play = current_room.cutscene
        $ current_room.cutscene = None
        call expression cutscene_to_play

    if in_dialogue:
        return
    else:
        jump room_loop

label room_loop:
    window hide None
    scene onlayer front_sprites
    show screen room_screen onlayer backgrounds
    call screen room_hud
    jump room_loop


label start:
    call initialisation

    $ current_room = R_livingRoom
    jump prologue_part1_arrival
    # Dialogue de test par-dessus
    jump room_loop

label room_not_neighbor:
    image Banane = Solid("#e1ea61", xsize=500, ysize=100, xalign=0.5, yalign=1.0)
    hide Carmille
    show Banane
    e "OMG.... Cette room n'existe PAAAAAAAAS"
    return