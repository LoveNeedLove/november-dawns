init python:
    def createAndAddProofToInventory(name, description, icon, room, posX, posY): # Créé un objet preuve, et l'ajoute dans l'inventaire
        inventory.append(Proof(name, description, icon, room, posX, posY))
        return
    
    def addProofToInventory(proof):
        inventory.append(proof)
        return

    def toggle_Inventory(): # Ouvre ou ferme l'inventaire
        if (store.inventory_open):
            store.inventory_open = False
            renpy.hide_screen("inventory")
        else:
            store.inventory_open = True
            renpy.show_screen("inventory")

    def toggle_Minimap(): # Ouvre ou ferme la minimap
        if (store.minimap_open):
            store.minimap_open = False
            renpy.hide_screen("minimap")
            renpy.hide_screen("proofs_on_minimap")
        else:
            store.minimap_open = True
            renpy.show_screen("minimap")
            renpy.show_screen("proofs_on_minimap")

    def toggle_Proof_Info(proofToShow): # Ouvre ou ferme la proof Info
        if (not store.proof_open):
            renpy.show_screen("proof_info", proofToShow)
            store.proof_open = True
        else:
            store.proof_open = False
            print("hiding screen here", None)
            renpy.hide_screen("proof_info")
            

    def minimap_Travel(destination): # Pour passer d'une salle à une autre, en utilisant la minimap
        if destination in current_room.neighbors:
            renpy.call("travel_to", destination)
        else:
            renpy.call("room_not_neighbor")

screen livre(): # Bouton basique pour récupérer un objet dans son inventaire
    imagebutton:
        xpos 90
        ypos 450
        idle "Gray_book.png"
        at custom_zoom
        action [Hide("coucou"),
                Function(createAndAddProofToInventory, "le livre", "cest un beau livre", "Gray_book.png", "Salon", 10, 10),
                Call("recuperer_item", "livregris")]

transform custom_zoom:
    zoom 0.35

transform main_buttons_zoom:
    zoom 0.5

screen inventory: # Montre tous les objets de l'inventaire
    frame:
        xpadding 20 ypadding 20
        vbox:
            for i in inventory:
                frame:
                    xmargin 10
                    ymargin 10
                    xpadding 10 ypadding 10
                    add i.icon size(100, 100)

screen inventory_toggle: # Ouvre et ferme l'inventaire
    imagebutton:
        xalign 1.0
        idle "Gray_book.png"
        at main_buttons_zoom
        action Function(toggle_Inventory)

screen minimap_toggle: # Ouvre et ferme la minimap
    imagebutton:
        xalign 1.0
        ypos 200
        idle "Gray_book.png"
        at main_buttons_zoom
        action Function(toggle_Minimap)

screen minimap() layer 'front_sprites': # Montre la minimap
    zorder 2
    frame:
        xalign 0.5 yalign 0.5
        xmargin 10 ymargin 10
        imagemap:
            ground "minimapTest.png"
            hotspot (171, 361, 207, 406) action [Function(toggle_Minimap), Function(minimap_Travel, R_entryHallway)]
            hotspot (378, 363, 506, 315) action [Function(toggle_Minimap), Function(minimap_Travel, R_livingRoom)]
            hotspot (887, 427, 268, 254) action [Function(toggle_Minimap), Function(minimap_Travel, R_kitchen)]
            hotspot (1154, 431, 275, 379) action [Function(toggle_Minimap), Function(minimap_Travel, R_garage)]
            hotspot (888, 135, 542, 293) action [Function(toggle_Minimap), Function(minimap_Travel, R_garden)]
            hotspot (174, 222, 502, 138) action [Function(toggle_Minimap), Function(minimap_Travel, R_F1hallway)]
            hotspot (174, 47, 207, 173) action [Function(toggle_Minimap), Function(minimap_Travel, R_F1bathroom)]
            hotspot (381, 48, 300, 171) action [Function(toggle_Minimap), Function(minimap_Travel, R_F1parentsRoom)]
            hotspot (683, 96, 204, 266) action [Function(toggle_Minimap), Function(minimap_Travel, R_F1fransksRoom)]

screen proofs_on_minimap() layer 'front_sprites':
    zorder 3
    for proof in store.inventory:
        imagebutton:
            idle proof.icon
            at custom_zoom
            action Function(proof.showInfo)
            xpos proof.posX
            ypos proof.posY

screen proof_info(proof) layer 'front_sprites':
    zorder 4
    if proof is not None:
        frame:
            xalign 1.0
            xmargin 10 ymargin 10
            vbox:
                text proof.name
                text proof.description
                text proof.room.id
                if store.in_cross_examination:
                    textbutton "Present":
                        action Function(lambda: renpy.notify("Preuve présentée !"))
                        text_color "#d82883"
                        text_hover_color "#3428d8"
                        text_size 50