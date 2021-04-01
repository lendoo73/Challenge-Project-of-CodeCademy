# Define sum_to_one() below...
def sum_to_one(n):
  # base case:
  if n == 1:
    return n
  
  # recursive step:
  print(f"Recursing with input: {n}")
  return n + sum_to_one(n - 1)


# uncomment when you're ready to test
print(sum_to_one(7))

