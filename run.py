import numpy as np
from tabulate import tabulate
import os
import time

ROWS = 10
COLUMNS = 10


def clear():
    """
    Clear Screen
    credit: https://www.altcademy.com/blog/how-to-clear-screen-in-python/
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def create_gameboard():
    """
    Create Game Board  10 x 10
    Used libary Numpy to build game bord grid
    credit: https://www.youtube.com/watch?v=UYgyRArKDEs
            https://www.youtube.com/@KeithGalli

    """
    game_board = np.full((ROWS, COLUMNS), ' ')
    return game_board


def print_ascii(fn):
    """
    Print textfile, ascii art function
    To print textfile or ascii graphic from textfile
     print_ascii('assets/images/textfile.txt')
    credit: https://learnlearn.uk/python/ascii-art/
    """
    f = open(fn, 'r')
    print(''.join([line for line in f]))

#############################
#   Start
#############################


def start():
    """
    Start function Start Page,
    Print, Logo,
    Print sample gameplan at start, clear screen
    and print logo and game board.
    """
    clear()
    print_ascii('assets/images/gomoku.txt')
    print_ascii('assets/images/start.txt')
    time.sleep(2)
    clear()
    menu()


def logo():
    """ Print Logo and small horizontal menu  """
    clear()
    print_ascii('assets/images/gomoku.txt')
    print(' [ A.  Play New Game ]  [ B.  Instructions ]  [ C.  Start Page ]')


#############################
#   Menu
# ###########################


def menu():
    """
    Print Menu,
    Play New Game, Rules and instructions,
    with input A or B, C is available in the logic to
    use C or 33 to get to Start page
    credit: https://stackoverflow.com/questions
    /49226804/python-input-menu-function
    """
    loop = True
    while loop:
        clear()
        print_ascii('assets/images/gomoku.txt')
        print('\n')
        print('                         A.  Play New Game\n')
        print('                         B.  Rules and instructions\n')
        player_action = input('                \
        Please Enter Your Choice:\n')

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


def menu_hidden():
    """ Menu hidden, Logic for sm all horizontal menu """
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


def home_act1():
    """ Menu choice A/11 New Game """
    clear()
    # logo()
    # time.sleep(2)
    # clear()
    main()
    clear()


def home_act2():
    """ Menu choice B/22 Instruction  """
    clear()
    instruction()
    clear()


def home_act3():
    """ Menu choice C/33 Start Page """
    clear()
    # print_ascii('assets/images/gomoku.txt')
    # print('\n')
    menu()
    clear()


#############################
# Print Game Board
#############################

def print_game_board(game_board):
    """ Print Game Board """
    clear()
    print_ascii('assets/images/gomoku.txt')
    print('    [ 11.  Play New Game ]\
    [ 22.  Instructions ]    [ 33.  Start Page ]\n')
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
# Game functions
#############################


""" Game Functions

    Credit: https://www.youtube.com/@KeithGalli
            https://www.youtube.com/watch?v=UYgyRArKDEs
    - Place a piece
    - Check if position is available
    - Check for winner 5 in a row positions
"""


def place_piece(game_board, row, column, piece):
    """
    Place a Piece,
    Puts players piece O for Player 1
    or X for Player 2 on the board
    """
    game_board[row][column] = piece


def check_valid_position(game_board, row, column):
    """ Check if position/column/row is available """
    return game_board[row][column] == ' '


def check_winner(game_board, piece):
    """ Check for winner, if player has 5 pieces in a row """

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


def main():
    """ Main Function,  Starts the game for Player 1 """

    """ Call Create Game Board Function """
    game_board = create_gameboard()
    """ Call Print Game Board Function """
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

    """ Player input row and column """
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
############################


def instruction():
    """ Instruction page """
    clear()
    print_ascii('assets/images/gomoku.txt')
    print('\n')
    print_ascii('assets/images/instructions.txt')
    menu_hidden()


""" Run Game """
start()
