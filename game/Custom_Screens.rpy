init python:
    def addProofToInventory(name, description, icon, room, posX, posY): # Créé un objet preuve, et l'ajoute dans l'inventaire
        inventory.append(Proof(name, description, icon, room, posX, posY))
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
        else:
            store.minimap_open = True
            renpy.show_screen("minimap")

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
                Function(addProofToInventory, "le livre", "cest un beau livre", "Gray_book.png", "Salon", 10, 10),
                Call("recuperer_item", "livregris")]

transform custom_zoom:
    zoom 0.2

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
