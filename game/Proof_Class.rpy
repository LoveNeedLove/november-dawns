init python:
    class Proof:
        def __init__(self, name, description, icon, room, posX, posY):
            self.name = name
            self.description = description
            self.icon = icon # Le path de l'icone
            self.room = room # La pièce dans laquelle cette preuve se situe
            self.posX = posX # Position X exacte dans la minimap
            self.posY = posY # Position Y exacte dans la minimap
        
        def showInfo(self):
            toggle_Proof_Info(self)