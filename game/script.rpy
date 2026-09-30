init python:
    from renpy.display.transition import Transition
    
label travel_to(destination, in_dialogue=False, trans_duration=0.4, trans_in=None, anim_out=None, anim_in=None, all_screen=False):
    $ renpy.block_rollback()

    if anim_out is not None:
        if isinstance(anim_out, Transition):
            $ renpy.transition(anim_out)
        else:
            show screen room_screen(at_anim=anim_out, all_screen=all_screen) onlayer backgrounds
            $ renpy.pause(0.4)

    scene black

    if trans_in is None:
        with Fade(trans_duration, 0.0, trans_duration)
    else:
        with trans_in

    # --- CHANGEMENT DE DESTINATION ET ENTRÉE ---
    $ current_room = destination

    # --- TRANSITION / ANIMATION D'ENTRÉE (anim_in) ---
    if anim_in is not None and not isinstance(anim_in, Transition):
        show screen room_screen(at_anim=anim_in, all_screen=all_screen) onlayer backgrounds
    else:
        show screen room_screen onlayer backgrounds

    # Application de la transition d'entrée si anim_in ou trans_in est un objet Transition
    $ entry_trans = anim_in if isinstance(anim_in, Transition) else trans_in
    if entry_trans is not None:
        with entry_trans             # None : la nouvelle pièce apparaît d'un coup[cite: 1]

    $ renpy.checkpoint()

    if current_room.cutscene is not None:
        $ cutscene_to_play = current_room.cutscene
        $ current_room.cutscene = None
        call expression cutscene_to_play

    if in_dialogue:
        return
    else:
        jump room_loop

label anim_room(anim=None, trans=None, all_screen=False, pause_time=0.4):
    """
    Applique une animation (ATL/Transform) ou une transition sur la pièce actuelle.
    
    :param anim: Transform ou animation ATL à appliquer (ex: pop_from_right).
    :param trans: Transition Ren'Py classique (ex: dissolve, fade).
    :param all_screen: Si True, applique sur tout le viewport ; si False, juste sur l'imagemap.
    :param pause_time: Temps de pause en secondes pour laisser l'animation ATL se dérouler.
    """
    if anim is not None:
        # Applique le Transform / ATL sur l'écran
        show screen room_screen(at_anim=anim, all_screen=all_screen) onlayer backgrounds
        if pause_time > 0:
            $ renpy.pause(pause_time)

    if trans is not None:
        # Applique une transition classique Ren'Py
        with trans

    return

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
    m "Mmmmh... I can't reach this room from here..."
    return