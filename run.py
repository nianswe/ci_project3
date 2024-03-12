import numpy as np
import os

ROWS = 10
COLUMNS = 10

""" Create Game Board  10 x 10 """
def create_gameboard():
    game_board = np.full((ROWS, COLUMNS), '   ')
    return game_board

""" Print Game Board """
def print_game_board(game_board):
    print(game_board)

""" Place a Piece """
def place_piece(game_board, row, column, piece):
    game_board[row][column] = piece

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

        # Player 1 Input
        if turn == 0:
            row = int(input(f"Player 1 make your choice row (0 - 9): "))
            column = int(input(f"Player 1 make your choice column (0 - 9): "))
            """ Place a game piece """
            place_piece(game_board, row, column, ' O ')
            turn += 1
            """ Print Game Board """
            print_game_board(game_board)

        else:
        # Player 2 Input    
            row = int(input(f"Player 2 make your choice row (0 - 9): "))
            column = int(input(f"Player 2 make your choice column (0 - 9): "))
            """ Place a game piece """
            place_piece(game_board, row, column, ' X ')
            turn += 1
            turn = turn % 2
            """ Print Game Board """
            print_game_board(game_board)

""" Run Game """
main()