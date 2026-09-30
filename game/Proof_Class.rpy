default in_cross_examination = False
default in_proof_present = False
default expected_proof_id = None
default proof_presentation_result = None
default current_proof = None

init python:
    
    
    class Proof:
        def __init__(self, name, description, icon, room, posX, posY, id=None):
            self.id = id if id is not None else name
            self.name = name
            self.description = description
            self.icon = icon
            self.room = room
            self.posX = posX
            self.posY = posY
        
        def showInfo(self):
            store.current_proof = self
            toggle_Proof_Info(self)

        def present(self):
            # 1. Ferme la fenêtre d'info de la preuve et la minimap
            if store.proof_open:
                toggle_Proof_Info(None)
            if store.minimap_open:
                toggle_Minimap()

            # 2. Cas A : Contre-interrogatoire (Cross-Examination)
            if store.in_cross_examination:
                # Appelle la logique de vérification du statement actuel
                if hasattr(store, "current_cx") and store.current_cx:
                    statement = store.current_cx.statements[store.cx_index]
                    if statement.correct_evidence_id == self.id:
                        store.in_cross_examination = False
                        store._history = True
                        renpy.jump(statement.contradiction_label)
                    else:
                        renpy.jump("cx_penalty")

            # 3. Cas B : Présentation hors cross-examination (in_proof_present)
            elif store.in_proof_present:
                store.in_proof_present = False
                if self.id == store.expected_proof_id:
                    store.proof_presentation_result = True
                else:
                    store.proof_presentation_result = False
                # Débloque l'attente du label
                renpy.jump("after_proof_presented")