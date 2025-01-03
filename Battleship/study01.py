# Inside your function, inside your for loop,
# use " " as the separator to .join the elements of each row.

board = []

for i in range(5):
  board.append(["O"] * 5)

#print(board)

def print_board(board_in):
  for row in board:
    print (" ".join(row))

print_board(board)