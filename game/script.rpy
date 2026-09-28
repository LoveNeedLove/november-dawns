label travel_to(destination):
    scene black with dissolve
    $ current_room = destination

    if current_room.cutscene is not None:
        $ cutscene = current_room.cutscene
        $ current_room.cutscene = None  # Consommée
        call expression cutscene

    jump room_loop

label room_loop:
    window hide None
    scene onlayer front_sprites
    show screen room_screen
    call screen room_hud
    jump room_loop


label start:
    call initialisation

    $ current_room = R_livingRoom

    image Eileen = Solid("#4a6fa5", xsize=400, ysize=900, xalign=0.8, yalign=1.0)

    # Affiche le bouton pour toggle la minimap
    show screen minimap_toggle
    
    # Affiche la pièce en fond
    show screen room_screen

    # Dialogue de test par-dessus
    show Eileen
    e "Feur 67 ?"

    hide Eileen with dissolve
    e "tout ca tout ca #tu as la dalle"

    show Eileen
    e "Très bien, voici ma déposition sur ce qui s'est passé hier soir !"
    window hide None
    # On configure les énoncés
    $ s1 = Statement(e,"J'étais seule dans le salon toute la soirée jusqu'à minuit.")
    $ s2 = Statement(e,"À 22h, j'ai entendu quelqu'un courir dans les archives.")
    
    # Phrase clé : si on présente "preuve", ça débloque la suite
    $ s3 = Statement(e,"Je n'ai jamais vu la victime toucher à ce vieux tiroir.", 
                    correct_evidence_id="preuve", 
                    contradiction_label="objection_reussie")
                     
    $ s4 = Statement(e,"Voilà, c'est tout ce que j'ai vu et entendu.")

    # Initialisation du contre-interrogatoire
    $ current_cx = CrossExamination([s1, s2, s3, s4])

    $ in_cross_examination = True
    # Lancement de la phase d'interrogatoire
    jump cx_display

label room_not_neighbor:
    image Banane = Solid("#e1ea61", xsize=500, ysize=100, xalign=0.5, yalign=1.0)
    hide Eileen
    show Banane
    e "OMG.... Cette room n'existe PAAAAAAAAS"
    return