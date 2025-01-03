# First, delete your existing print statement.
# Then, define a function named print_board with a single argument, board_in.
# Inside the function, write a for loop to iterates through each row in board and print it to the screen.
# Call your function with board to make sure it works.

board = []

for i in range(5):
  board.append(["O"] * 5)

#print(board)

def print_board(board_in):
  for row in board:
    print (row)

print_board(board)