import numpy as np
from tabulate import tabulate
import os
import sys
import time

ROWS = 10
COLUMNS = 10

""" Clear Screen """


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
   


""" Create Game Board  10 x 10 
    Used libary Numpy to build game bord grid

"""


def create_gameboard():
    game_board = np.full((ROWS, COLUMNS), ' ')
    return game_board


"""  Print textfile function
     To print textfile or ascii graphic from textfile
"""


def print_ascii(fn):
    f = open(fn, 'r')
    print(''.join([line for line in f]))

#############################
#   Start
#############################

""" Start function Start Page"""


def start():
    clear()
    print_ascii('assets/images/gomoku.txt')
    # time.sleep(2)
    # clear()
    print_ascii('assets/images/start.txt')
    time.sleep(2)
    clear()
    # print_ascii('assets/images/gomoku.txt')
    # print('\n')
    menu()
    

""" Print Logo"""


def logo():
    clear()
    print_ascii('assets/images/gomoku.txt')
    print(' [ A.  Play New Game ]  [ B.  Instructions ]  [ C.  Start Page ]')




#############################
#   Menu 
# ###########################


""" Menu """


def menu():
    loop = True
    while loop:
        clear()
        print_ascii('assets/images/gomoku.txt')
        print('\n')
        print('                         A.  Play New Game\n')
        print('                         B.  Rules and instructions\n')
        player_action = input('                         Please Enter Your Choice:\n')

        if player_action == 'a' or player_action == '11':
            home_act1()
            continue

        elif player_action == 'b' or player_action == '22':
            home_act2()
            continue
        elif player_action == 'c' or player_action == '33':
            home_act3()
            continue
        else:
            # print_ascii('assets/images/gomoku.txt')
            print("     Please type \'A\', \'B\'")
            continue


#############################
#   Hidden Menu logic
#############################


""" Menu hidden"""


def menu_hidden():
    loop = True
    while loop:
        player_action = input('')
        if player_action == 'a' or player_action == '11':
            home_act1()
            continue
        elif player_action == 'b' or player_action == '22':
            home_act2()
            continue
        elif player_action == 'c' or player_action == '33':
            home_act3()
            continue
        else:
            print("     Please type \'A\', \'B\'")
            continue
    clear()

#############################
# Menu choices functions
#############################


""" Menu choice A/11 New Game """


def home_act1():
    clear()
    # logo()
    # time.sleep(2)
    # clear()
    main()
    clear()


""" Menu choice B/22 Instruction """


def home_act2():
    clear()
    instruction()
    clear()


""" Menu choice C/33 Start Page """


def home_act3():
    clear()
    # print_ascii('assets/images/gomoku.txt')
    # print('\n')
    menu()
    clear()


#############################
# Print Game Board
#############################
""" Print Game Board """


def print_game_board(game_board):
    clear()
    print_ascii('assets/images/gomoku.txt')
    print('      [ 11.  Play New Game ]  [ 22.  Instructions ]  [ 33.  Start Page ]\n')
    """ Add header """
    y = np.array([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]])
    x = np.array([['', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']])
    """ Add header column on left """
    game_board = np.append(y, game_board, axis=1)
    """ Add header at bottom """
    game_board = np.append(x, game_board, axis=0)
    """ Flip gamebord vertical (numpy libery) """
    """ Create grid with Tabulate """
    print(tabulate(np.flip(game_board, 0), tablefmt='simple_grid'))

#############################
# Game Functions
#############################


""" Place a Piece """


def place_piece(game_board, row, column, piece):
    game_board[row][column] = piece


""" Check if position/column/row is available """


def check_valid_position(game_board, row, column):
    return game_board[row][column] == ' '


""" Check for winner, if player has 5 pieces in a row """


def check_winner(game_board, piece):
    """ Check for five horizontal winning positions in a row """
    for c in range(COLUMNS - 4):
        for r in range(ROWS):
            if game_board[r][c] == piece and \
                game_board[r][c + 1] == piece and \
                game_board[r][c + 2] == piece and \
                game_board[r][c + 3] == piece and \
                    game_board[r][c + 4] == piece:
                return True
    """ Check for five vertical winning positions in a row """
    for c in range(COLUMNS):
        for r in range(ROWS - 4):
            if game_board[r][c] == piece and \
                game_board[r + 1][c] == piece and \
                game_board[r + 2][c] == piece and \
                game_board[r + 3][c] == piece and \
                    game_board[r + 4][c] == piece:
                return True
    """ Check for five diagonal winning positions in a row positive """
    for c in range(COLUMNS - 4):
        for r in range(ROWS-4):
            if game_board[r][c] == piece and \
                game_board[r+1][c+1] == piece and \
                game_board[r+2][c+2] == piece and \
                game_board[r+3][c+3] == piece and \
                    game_board[r+4][c+4] == piece:
                return True
    """ Check for five diagonal winning positions in a row negative """
    for c in range(COLUMNS-4):
        for r in range(ROWS):
            if game_board[r][c] == piece and \
                game_board[r-1][c+1] == piece and \
                game_board[r-2][c+2] == piece and \
                game_board[r-3][c+3] == piece and \
                    game_board[r-4][c+4] == piece:
                return True

#############################
#  Main
#############################


""" Main Function """


def main():
    """ Call Create Game Board Function """
    game_board = create_gameboard()
    """ Call Print Game Board Function """
    #clear()
    logo()
    print('\n')
    print_game_board(game_board)

    """ Reset Game Over to False """
    game_over = False
    """ Reset Player turn to 0 for Player 1 to start next round """
    turn = 0

#############################
# Player Input
#############################
    while not game_over:
        if turn == 0:
            """ Player 1 Input """
            """ Verify input is number 0 - 9 """
            while True:
                try:
                    """ Input row Player 1 """
                    row = int(input(f"Player 1 make your choice row (0 - 9):"))
                    """ Numeric menu 11, 22, 33 isted of A, B, C """
                    if row == 11:
                        home_act1()
                    elif row == 22:
                        home_act2()
                    elif row == 33:
                        home_act3()
                    elif row <= 9:
                        break
                    raise ValueError()
                except ValueError:
                    clear()
                    print_game_board(game_board)
                    print("Input must be a number between 0 - 9.")

            """ Verify input is number 0 - 9 """
            while True:
                try:
                    """ Input column Player 1 """
                    column = int(
                        input(f"Player 1 make your choice column (0 - 9):"))
                    if row == 11:
                        home_act1()
                    elif row == 22:
                        home_act2()
                    elif row == 33:
                        home_act3()
                    elif column <= 9:
                        break
                    raise ValueError()
                except ValueError:
                    clear()
                    print_game_board(game_board)
                    print("Input must be a number between 0 - 9.")

            """ Check if position/column/row is available """
            if check_valid_position(game_board, row, column):
                """ Place a game piece """
                place_piece(game_board, row, column, 'O')
                """ Check for winner Player 1, if 5 pieces are in row """
                if check_winner(game_board, 'O'):
                    clear()
                    print_game_board(game_board)
                    print("PLAYER 1 WINS with 5 in a row!!")
                    print('\n')
                    print(' [ A.  Play New Game ]  [ B.  Instructions ]  [ C.  Start Page ]')
                    time.sleep(2)
                    clear()
                    print_ascii('assets/images/winner1.txt')
                    time.sleep(2)
                    game_over = True
                turn += 1
                """ Print Game Board """
                clear()
                print_game_board(game_board)
            else:
                print("Position is not available, try again!")
                continue
        else:
            """ Player 2 Input """
            """ Verify input is number 0 - 9 """
            while True:
                try:
                    """ Input row Player 2 """
                    row = int(input(f"Player 2 make your choice row (0 - 9):"))
                    if row == 11:
                        home_act1()
                    elif row == 22:
                        home_act2()
                    elif row == 33:
                        home_act3()
                    elif row <= 9:
                        break
                    raise ValueError()
                except ValueError:
                    clear()
                    print_game_board(game_board)
                    print("Input must be a number between 0 - 9.")

            """ Verify input is number 0 - 9 """
            while True:
                try:
                    """ Input column Player 2 """
                    column = int(
                        input(f"Player 2 make your choice column (0 - 9): "))
                    if row == 11:
                        home_act1()
                    elif row == 22:
                        home_act2()
                    elif row == 33:
                        home_act3()
                    elif row <= 9:
                        break
                    raise ValueError()
                except ValueError:
                    clear()
                    print_game_board(game_board)
                    print("Input must be a number between 0 - 9.")

            """ Check if position/column/row is available """
            if check_valid_position(game_board, row, column):
                """ Place a game piece """
                place_piece(game_board, row, column, 'X')
                """ Check for winner Player 2, if 5 pieces are in row """
                if check_winner(game_board, 'X'):
                    clear()
                    print_game_board(game_board)
                    print("PLAYER 2 WINS with 5 in a row!!")
                    print('\n')
                    print(' [ A.  Play New Game ]  [ B.  Instructions ]  [ C.  Start Page ]')
                    time.sleep(2)
                    clear()
                    print_ascii('assets/images/winner2.txt')
                    time.sleep(2)
                    game_over = True
                turn += 1
                turn = turn % 2
                """ Print Game Board """
                clear()
                print_game_board(game_board)
            else:
                print("Position is not available, try again!")
                continue


#############################
#   Instruction page
# ###########################


""" Instruction page """


def instruction():
    clear()
    print_ascii('assets/images/gomoku.txt')
    print('\n')
    print_ascii('assets/images/instructions.txt')
    menu_hidden()


""" Run Game """
start()
