import numpy as np
import os

ROWS = 10
COLUMNS = 10

""" Create Game Board  10 x 10 """
def create_gameboard():
    game_board = np.full((ROWS, COLUMNS), '.')
    return game_board

""" Print Game Board """
def print_board(game_board):
    game_board = create_gameboard()
    print(game_board)

""" Main Function """
def main():
    game_board = create_gameboard()
    print_board(game_board)

""" Run Game """
main()