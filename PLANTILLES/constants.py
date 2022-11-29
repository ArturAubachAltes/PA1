
BSIZ = 3 # board side size

ST_PLAYER = 4 # stones per player

# Define the game window width and height and the slot size and separation in pixels
SLOT = 100        # squares size
SEP = 20          # squares separation
ROOM = SLOT + SEP # extra room at sides 
HEIGHT = BSIZ * SLOT + (BSIZ + 1) * SEP + ROOM # room for 3 squares with margin and internal separators and extra below
WIDTH = HEIGHT + ROOM              # extra at both sides
RAD = SLOT / 3                     # circle radius

NO_PLAYER = -1
