#Before the lines prompting the user for input:
# Print the value of ship_row.
# Print the value of ship_col.

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
print (ship_row)
ship_col = random_col(board)
print (ship_col)
# Add your code below!


guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))