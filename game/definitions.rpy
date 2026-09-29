init python:
    class Room():
        def __init__(self, id, bg, neighbors=None):
            self.id = id
            self.bg= bg
            self.hotspots = []
            self.convos = []
            self.neighbors = [] if neighbors is None else neighbors
            self.cutscene = None #on mets un string pour trigger un label à l'entrée de la pièce par exemple
        
        def add_neighbor(self, nextRoom):
            self.neighbors.append(nextRoom)
        
        def remove_neighbors(self, roomToRemove):
            self.neighbors.remove(roomToRemove)

    class Convos():
        def __init__(self, action, chara):
            self.action = action #label vers lequel on doit jump
            self.chara = chara #image du perso associé à la convo


    class HotspotData:
        def __init__(self, rect, action):
            self.rect = rect          # Zone de collision du hotspot(x, y, width, height)
            self.action = action      # label vers lequel on doit jump quand on clique sur le hotspot
        def is_active(self):
            return True

    class QuickEvent:
        def __init__(self, id, prerequisites, action):
            self.id = id
            self.prerequisites = set(prerequisites)  # S'assure que c'est un set
            self.action = action
            self.triggeredAlready = False

        def triggerEvent(self, eventsObserved):
            # Déclenche l'action si les prérequis sont satisfaits et qu'elle n'a pas encore eu lieu
            if not self.triggeredAlready and self.prerequisites.issubset(eventsObserved):
                self.triggeredAlready = True
                renpy.call(self.action)

    class EventManager:
        def __init__(self):
            self.eventsObserved = set()
            self.allEvents = []

        def add_event(self, event):
            self.allEvents.append(event)

        def unlock(self, eventId):
            # 1. On n'ajoute que les nouveaux événements pour éviter les doublons
            if eventId not in self.eventsObserved:
                self.eventsObserved.add(eventId)
                
                # 2. On vérifie immédiatement si cet ajout complète les prérequis d'une scène
                for event in self.allEvents:
                    event.triggerEvent(self.eventsObserved)

    class Statement:
            def __init__(self, chara, text, correct_evidence_id=None, contradiction_label=None):
                self.chara = chara                    # Objet Character (ex: e)
                self.text = text                      # Texte de la réplique
                self.correct_evidence_id = correct_evidence_id
                self.contradiction_label = contradiction_label


    class CrossExamination:
        def __init__(self, statements):
            self.statements = statements
            self.index = 0

        def current(self):
            return self.statements[self.index]

        def has_prev(self):
            return self.index > 0

        def has_next(self):
            return self.index < len(self.statements) - 1

        def next(self):
            if self.has_next():
                self.index += 1

        def prev(self):
            if self.has_prev():
                self.index -= 1

        def present(self, evidence_id):
            curr = self.current()
            if curr.correct_evidence_id == evidence_id:
                global in_cross_examination
                in_cross_examination = False
                renpy.jump(curr.contradiction_label)
            else:
                renpy.jump("cx_penalty")

    config.window_hide_transition = None

    class PersonProfile:
        def __init__(self, chara, name, icon):
            self.id = id
            self.name = name
            self.icon = icon