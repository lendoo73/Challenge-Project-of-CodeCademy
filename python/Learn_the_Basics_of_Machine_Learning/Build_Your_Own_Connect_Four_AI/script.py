from connect_four import *
import numpy as np

def two_ai_game():
    my_board = make_board()
    while not game_is_over(my_board):
      #The "X" player finds their best move.
      result = minimax(
        my_board, 
        True, 
        3, 
        -float("Inf"), 
        float("Inf"), 
        impoved_evaluate_board
      )
      print( "X Turn\nX selected ", result[1])
      print(result[1])
      select_space(my_board, result[1], "X")
      print_board(my_board)

      if not game_is_over(my_board):
        #The "O" player finds their best move
        result = minimax(
          my_board, 
          False, 
          4, 
          -float("Inf"), 
          float("Inf"), 
          codecademy_evaluate_board
        )
        print( "O Turn\nO selected ", result[1])
        print(result[1])
        select_space(my_board, result[1], "O")
        print_board(my_board)
    if has_won(my_board, "X"):
        print("X won!")
    elif has_won(my_board, "O"):
        print("O won!")
    else:
        print("It's a tie!")

def impoved_evaluate_board(board):
  board = np.array(board)

  def check_streak(player, row):
    #check triple streak
    double = player * 2
    triple = player * 3
    if  f" {triple}" in row or f"{triple} " in row or f"{player} {double}" in row or f"{double} {player}" in row:
      return 2
    #check double streak
    if  f"  {double}" in row or f" {double} " in row or f"{double}  " in row or f"{player} {player} " in row or f" {player} {player}" in row:
      #print(f"{double} streak found")
      return 1
    return 0

  def get_all_way(arr2d):
    max_col = len(arr2d[0])
    max_row = len(arr2d)
    cols = [[] for _ in range(max_col)]
    rows = [[] for _ in range(max_row)]
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1

    for x in range(max_col):
      for y in range(max_row):
        cols[x].append(arr2d[y][x])
        rows[y].append(arr2d[y][x])
        fdiag[x+y].append(arr2d[y][x])
        bdiag[x-y-min_bdiag].append(arr2d[y][x])

    return cols, rows, fdiag, bdiag
  
  def counter(arr, x_streak, o_streak):
    if len(arr) < 4:
      return x_streak, o_streak
    for row in arr:
      row = "".join(row)
      x_streak += check_streak("X", row)
      o_streak += check_streak("O", row)
    return x_streak, o_streak

  if has_won(board, "X"):
    return float("Inf")
  if has_won(board, "O"):
    return -float("Inf")

  rows, cols, fdiag, bdiag = get_all_way(board)

  x_streak, o_streak = counter(rows, 0, 0)
  x_streak, o_streak = counter(cols, x_streak, o_streak)
  x_streak, o_streak = counter(fdiag, x_streak, o_streak)
  x_streak, o_streak = counter(bdiag, x_streak, o_streak)

  return x_streak - o_streak


two_ai_game()

"""
new_board = make_board()
select_space(new_board, 1, "X")
select_space(new_board, 2, "O")
select_space(new_board, 2, "X")
select_space(new_board, 3, "O")
select_space(new_board, 3, "X")
select_space(new_board, 4, "X")
print_board(new_board)
print(impoved_evaluate_board(new_board))
"""
