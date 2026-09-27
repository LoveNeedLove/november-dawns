init python:
    class Room():
        def __init__(self, id, bg):
            self.id = id
            self.bg= bg
            self.hotspots = []
            self.convos = []
            self.neighbors = []
            self.cinematic = None #on mets un string pour trigger un label à l'entrée de la pièce par exemple

    class Convos():
        def __init__(self, action, chara):
            self.action = action #label vers lequel on doit jump
            self.chara = chara #image du perso associé à la convo


    class HotspotData:
        def __init__(self, rect, action):
            self.rect = rect          # Zone de collision du hotspot(x, y, width, height)
            self.action = action      # label vers lequel on doit jump quand on clique sur le hotspot

    class QuickEvent:
        def __init__(self, id, prerequisites, action, triggeredAlready):
            self.id = id
            self.prerequisites = prerequisites
            self.action = action
            self.triggeredAlready = False

        def triggerEvent(self, eventsObserved):
            if not self.triggeredAlready and self.prerequisites.issubset(eventsObserved):
                self.triggeredAlready = True
                renpy.call(self.action)

    class EventManager():
        def __init__(self):
            self.eventsObserved = set()
            self.allEvents = []

            def unlock(self, eventId):
                if eventId not in self.eventsObserved:
                    self.eventsObserved.add(eventId)
                else:
                    for event in allEvents:
                        event.triggerEvent(self.eventsObserved)

define e = Character("Eileen")

define m = Character("Maj")
define f = Character("Fransk")
define l = Character("Lou")
define s = Character("Stheno")
define p = Character("Pani")
define v = Character("Carmille")
define c = Character("Cassie")
define k = Character("Kid")
define a = Character("Agent")
define d = Character("Cassie's Dad")

# The game starts here.
label travel_to(destination):
    scene black with dissolve
    $ current_room = destination

    if current_room.cutscene is not None:
        $ cutscene = current_room.cutscene
        $ current_room.cutscene = None  # Consommée
        call expression cutscene

    jump room_loop

label room_loop:
    #show screen room_hud
    call screen room_screen
    jump room_loop

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy
    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
