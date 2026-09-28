
# Variables globales
default minimap_open = False
default inventory_open = False

# Instanciation de toutes les Rooms
default R_livingRoom = Room("livingRoom", "backgrounds/living_room_1.png")
default R_entryHallway = Room("entryHallway", "backgrounds/entry_hallway_1.png")
default R_kitchen = Room("kitchen", "backgrounds/kitchen.png")
default R_garage = Room("garage", "backgrounds/garage.png")
default R_garden = Room("garden", "backgrounds/garden.png")
default R_F1hallway = Room("floor1Hallway", "backgrounds/floor_1_hallway.png")
default R_F1bathroom = Room("upstairsBathroom", "backgrounds/upstairs_bathroom.png")
default R_F1parentsRoom = Room("parentsRoom", "backgrounds/parents_room.png")
default R_F1fransksRoom = Room("fransksRoom", "backgrounds/fransks_room.png")    

label initialisation:
# Ajout de tous les liens entre toutes les Rooms (neighbors)
    # --- RDC ---
    # - Living Room
    $ R_livingRoom.add_neighbor(R_entryHallway)
    $ R_livingRoom.add_neighbor(R_kitchen)
    # - EntryHallway
    $ R_entryHallway.add_neighbor(R_livingRoom)
    $ R_entryHallway.add_neighbor(R_F1hallway)
    # - Kitchen
    $ R_kitchen.add_neighbor(R_livingRoom)
    $ R_kitchen.add_neighbor(R_garden)
    $ R_kitchen.add_neighbor(R_garage)
    # - Garage
    $ R_garage.add_neighbor(R_kitchen)
    # - Garden
    $ R_garden.add_neighbor(R_kitchen)
    # --- FLOOR 1 --- 
    # - F1 Hallway
    $ R_F1hallway.add_neighbor(R_entryHallway)
    $ R_F1hallway.add_neighbor(R_F1bathroom)
    $ R_F1hallway.add_neighbor(R_F1parentsRoom)
    $ R_F1hallway.add_neighbor(R_F1fransksRoom)
    # - F1 Bathroom
    $ R_F1bathroom.add_neighbor(R_F1hallway)
    # - F1 Parents Room
    $ R_F1parentsRoom.add_neighbor(R_F1hallway)
    # - F1 Fransk Room
    $ R_F1fransksRoom.add_neighbor(R_F1hallway)
    return 
