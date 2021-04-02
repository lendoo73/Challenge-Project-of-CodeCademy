def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n

  prev = [0, 1]
  
  for x in range(1, n):
    result = sum(prev)
    prev[0], prev[1] = prev[1], result
  
  return result




# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)
