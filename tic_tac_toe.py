"""
Tic-Tac-Toe stdio (terminal version) by mutwiri-2
For user move, use the following words for valid inputs:
top-l for top left cell
top-m for top middle cell
top-r for top right cell
mid-l for middle left cell
mid-m for middle mid cell
mid-r for middle right cell
low-l for bottom left cell
low-m for bottom middle cell
low-r for bottom right cell

"""

the_board = {'top-l':' ', 'top-m':' ', 'top-r':' ', 'mid-l':' ', 'mid-m':' ', 'mid-r':' ', 'low-l': ' ', 'low-m':' ', 
'low-r':' '}

# import pprint
# pprint.pprint(the_board) # sorted
# print(list(the_board)) # ordered in sequence of entry

def print_board(board):
    print('|' + board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'] + '|')
    print('+-' *3 + '+')
    print('|' + board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'] + '|')
    print('+-' *3 + '+')
    print('|' + board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'] + '|')

import random
for i in range(9):
    print_board(the_board)

    # get user input plus move
    choice = input("X or O ? ")
    move = input("Which position on the board? ")
    the_board[move] = choice.upper()

    # computer's move
    comp_choice = random.choice(['X', 'O'])
    comp_move = random.choice(list(the_board.keys()))
    the_board[comp_move] = comp_choice