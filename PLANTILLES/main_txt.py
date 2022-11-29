"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Text handling of a simple tic-tac-toe-like board, 2021.
Intended for Grau en Intel-ligencia Artificial, Programacio i Algorismes 1.
"""

# Import initialization of the separately programmed abstract board:
from abs_board import set_board_up

# Prepare board:
# this will set up all stones as unplayed, select a first stone to play,
# and obtain functions to handle them as follows:
#   the call stones() allows one to loop on all stones,
#   the call select_st(i, j) marks as selected the stone at these coordinates,
#   the call move_st(i, j) 
#     if the square at these coordinates is free, moves the selected  
#     stone there, changes player, unselects the stone and checks for 
#     end of game; otherwise, does nothing, leaving the stone selected;
#     returns: bool "stone still selected", next player (may be the same), 
#     and bool "end of game"
#   the call to draw_txt(end) prints a text-based version of the board
stones, select_st, move_st, draw_txt = set_board_up()

# set_board_up() already selects a first stone
stone_selected = True

# Loop until game ends
end = False
draw_txt(False)

while not end:
    while not stone_selected:
        i, j = input("Select stone coordinates: ").split()
        stone_selected = select_st(int(i), int(j))
        draw_txt(end)
    while stone_selected and not end:
        i, j = input("Select destination coordinates: ").split()
        stone_selected, curr_player, end = move_st(int(i), int(j))
        draw_txt(end)

# Wait for the user to look at the screen before ending the program.
input('\nGame over.') 









