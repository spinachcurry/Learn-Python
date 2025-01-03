
# Create a function called flatten that takes a single list and concatenates all the sublists that are part of it into a single list.
# On line 3, define a function called flatten with one argument called lists.
# Make a new, empty list called results.
# Iterate through lists. Call the looping variable numbers.
# Iterate through numbers.
# For each number, .append() it to results.
# Finally, return results from your function.


n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
  results = []
  for numbers in lists:
    for i in numbers:
      results.append(i)
  return results

print(flatten(n))