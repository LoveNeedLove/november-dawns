init python:
    def create_Proof(name, description, icon): # Créé un objet preuve, et l'ajoute dans l'inventaire
        inventory.append(Proof(name, description, icon))
        return
    
    def toggle_Inventory():
        if (store.inventory_open):
            store.inventory_open = False
            renpy.hide_screen("inventory")
        else:
            store.inventory_open = True
            renpy.show_screen("inventory")

    def toggle_Minimap():
        if (store.minimap_open):
            store.minimap_open = False
            renpy.hide_screen("minimap")
        else:
            store.minimap_open = True
            renpy.show_screen("minimap")

screen livre: # Bouton basique pour récupérer un objet dans son inventaire
    imagebutton:
        xpos 90
        ypos 450
        idle "Gray_book.png"
        at custom_zoom
        action [Hide("coucou"),
                Function(create_Proof, "le livre", "cest un beau livre", "Gray_book.png"),
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

screen minimap: # Montre la minimap
    frame:
        xalign 0.5 yalign 0.5
        xmargin 10 ymargin 10
        imagemap:
            ground "minimapTest.png"
            hotspot (0, 0, 240, 139) action [Function(toggle_Minimap), Jump("map_cuisine")]
            hotspot (0, 136, 251, 127) action [Function(toggle_Minimap),Jump("map_salon")]
            hotspot (246, 0, 120, 265) action [Function(toggle_Minimap),Jump("map_couloir")]