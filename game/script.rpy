label travel_to(destination):
    scene black with dissolve
    $ current_room = destination
    show screen room_screen onlayer backgrounds

    if current_room.cutscene is not None:
        $ cutscene = current_room.cutscene
        $ print(f"ça a call {current_room} {cutscene} ")
        $ current_room.cutscene = None  # Consommée
        call expression cutscene
    else:
        $ print("no cutscene")

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