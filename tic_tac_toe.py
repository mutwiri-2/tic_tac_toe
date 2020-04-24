"""
Tic-Tac-Toe using just std i/o (terminal version) by mutwiri-2
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

next_board = {'top-l':' ', 'top-m':' ', 'top-r':' ', 'mid-l':' ', 'mid-m':' ', 'mid-r':' ', 'low-l': ' ', 'low-m':' ', 
'low-r':' '}


def print_board(board):
    print(f"|{board['top-l']}|{board['top-m']}|{board['top-r']}|")
    print(f"{'+-'*3}+")
    print(f"|{board['mid-l']}|{board['mid-m']}|{board['mid-r']}|")
    print(f"{'+-'*3}+")
    print(f"|{board['low-l']}|{board['low-m']}|{board['low-r']}|")
# computer only player

import random, copy, time

current_board = copy.copy(next_board)

while True:
    print_board(next_board)
    print("#" * 7)
    time.sleep(3)
    if current_board == {}:
        break
    else:
        comp_choice = random.choice(['X', 'O'])
        comp_move = random.choice(list(current_board.keys()))
        next_board[comp_move] = comp_choice
        del(current_board[comp_move])

