#Create a function that joins two lists together.
#On line 5, define a function called join_lists that has two arguments, x and y. They will both be lists.
#Inside that function, return the result of concatenating x and y together.

m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x,y): #list
  return x + y

print(join_lists(m, n))