default cx_index = 0

label cx_display:
    $ _history = False
    
    # 1. Récupère la phrase active selon l'index
    $ curr = current_cx.statements[cx_index]
    
    # 2. Affiche la réplique
    $ renpy.say(curr.chara, curr.text)

    # 3. Ce bloc n'est atteint QUE si le joueur avance au clic standard
    if cx_index < len(current_cx.statements) - 1:
        $ cx_index += 1
    jump cx_display

# Navigation directe pour les boutons
label cx_nav_prev:
    $ cx_index -= 1
    jump cx_display

label cx_nav_next:
    $ cx_index += 1
    jump cx_display

label cx_penalty:
    "No, this doesn't make sense. I have to think again."
    jump cx_loop
