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
    jump cx_display

label force_present_proof(target_proof_id):
    $ store.expected_proof_id = target_proof_id
    $ store.in_proof_present = True

    # Ouvre automatiquement la minimap et les preuves si elles ne sont pas déjà ouvertes
    if not store.minimap_open:
        $ toggle_Minimap()

    # Pause interactive : attend que le joueur clique sur une preuve puis sur "Present"
    $ renpy.pause(hard=True)

label after_proof_presented:
    if store.proof_presentation_result:
        # Succès : on nettoie et on continue le dialogue
        $ store.expected_proof_id = None
        $ store.proof_presentation_result = None
        return
    else:
        # Échec : réplique d'erreur puis on redemande
        "No, that doesn't prove anything right now."
        call force_present_proof(store.expected_proof_id) from _call_force_present_proof

# Pour avoir des choix de type "menu" qui bouclent. Attention, bonne_reponse est un index qui commence à 0
label menu_choice_loop(question, choice, good_answer, fail_text="No, this doesn't make sense. I have to think again."):
    while True:
        $ items = [(question, None)] + [(text, index) for index, text in enumerate(choice)]
        $ chosen_answer = renpy.display_menu(items, screen="choice")
        if chosen_answer == good_answer:
            return
        "[fail_text]"