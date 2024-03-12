import numpy as np
import os

ROWS = 10
COLUMNS = 10

""" Clear Screen """
def clear():
    os.system('clear')

""" Create Game Board  10 x 10 """
def create_gameboard():
    game_board = np.full((ROWS, COLUMNS), '   ')
    return game_board

""" Print Game Board """
def print_game_board(game_board):
    clear()
    print(game_board)
    

""" Place a Piece """
def place_piece(game_board, row, column, piece):
    game_board[row][column] = piece

""" Check if position/column/row is available """
def check_valid_position(game_board, row, column):
    return game_board[row][column] == '   '

""" Main Function """
def main():
    """ Call Create Game Board Function """
    game_board = create_gameboard()
    """ Call Print Game Board Function """
    print_game_board(game_board)

    """ Reset GameOver to False """
    game_over = False
    """ Reset Player turn to 0 or Player 1 to startt next round """
    turn = 0

    while not game_over:
        if turn == 0:
        # Player 1 Input
            """ Verify input is number 0 - 9 """
            while True:
                try: 
                    """ Input row Player 1 """
                    row = int(input(f"Player 1 make your choice row (0 - 9): "))
                    if row <= 9:
                        break
                    raise ValueError()
                except ValueError:
                    print("Input must be a number between 0 - 9.")
                    
            """ Verify input is number 0 - 9 """
            while True:
                try:        
                    """ Input column Player 1 """
                    column = int(input(f"Player 1 make your choice column (0 - 9): "))
                    if column <= 9:
                        break
                    raise ValueError()
                except ValueError:
                    print("Input must be a number between 0 - 9.")

            """ Check if position/column/row is available """
            if check_valid_position(game_board, row, column):
                """ Place a game piece """
                place_piece(game_board, row, column, ' O ')
                turn += 1
                """ Print Game Board """
                print_game_board(game_board)
            else:
                print("Position is not available, try again!")
                continue
        else:
        # Player 2 Input    
            """ Verify input is number 0 - 9 """
            while True:
                try:  
                    """ Input row Player 2 """
                    row = int(input(f"Player 2 make your choice row (0 - 9): "))
                    if row <= 9:
                        break
                    raise ValueError()
                except ValueError:
                    print("Input must be a number between 0 - 9.")
            
            """ Verify input is number 0 - 9 """
            while True:
                try:
                    """ Input column Player 2 """
                    column = int(input(f"Player 2 make your choice column (0 - 9): "))
                    if column <= 9:
                        break
                    raise ValueError()
                except ValueError:
                    print("Input must be a number between 0 - 9.")


            """ Check if position/column/row is available """
            if check_valid_position(game_board, row, column):
                """ Place a game piece """
                place_piece(game_board, row, column, ' X ')
                turn += 1
                turn = turn % 2
                """ Print Game Board """
                print_game_board(game_board)
            else:
                print("Position is not available, try again!")
                continue

""" Run Game """
main()