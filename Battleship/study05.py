# On line 29, add an if to check if guess_row equals ship_row and guess_col equals ship_col.

# If that is the case, please print out "Congratulations! You sank my battleship!"

# When you run this code, be sure to enter integer guesses in the panel where it asks for “Guess Row” and then “Guess Col”.

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)
print (ship_col)

guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
  print ("Congratulations! You sank my battleship!")
else:
  print ("Wrong guess")
