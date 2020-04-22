the_board = {'top-l':' ', 'top-m':' ', 'top-r':' ', 'mid-l':' ', 'mid-m':' ', 'mid-r':' ', 'low-l': ' ', 'low-m':' ', 
'low-r':' '}

import pprint
pprint.pprint(the_board) # sorted
print(list(the_board)) # ordered in sequence of entry

def print_board(board):
    print('|' + board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'] + '|')
    print('+-' *3 + '+')
    print('|' + board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'] + '|')
    print('+-' *3 + '+')
    print('|' + board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'] + '|')
    
print_board(the_board)