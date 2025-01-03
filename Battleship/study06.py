# Add an else under the if we wrote in the previous step.
# Print out "You missed my battleship!"
# Set the list element at guess_row, guess_col to "X".
# As the last line in your else statement, call print_board(board) again so you can see the "X".
# In the terminal, make sure to enter a column and row that is on the board and press Enter!

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
  print ("You missed my battleship!")
  board[guess_row][guess_col] = "X"
  print_board(board)
