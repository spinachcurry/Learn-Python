# Create a new variable called guess_row and set it to int(raw_input("Guess Row: ")).
# Create a new variable called guess_col and set it to int(raw_input("Guess Col: ")).
# Click Run and then answer the prompts by typing in a number and pressing Enter
# (or Return on some computers).

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Add your code below!
guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))