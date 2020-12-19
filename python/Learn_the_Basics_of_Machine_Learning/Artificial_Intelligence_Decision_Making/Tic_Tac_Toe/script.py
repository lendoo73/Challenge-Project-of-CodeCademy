from tic_tac_toe import *

my_board = [
	["1", "2", "3"],
	["4", "5", "6"],
	["7", "8", "9"]
]

while not game_is_over(my_board):
  select_space(my_board, minimax(my_board, True)[1], "X")
  print_board(my_board)
  if not game_is_over(my_board):
    select_space(my_board, minimax(my_board, False)[1], "O")
    print_board(my_board)  
