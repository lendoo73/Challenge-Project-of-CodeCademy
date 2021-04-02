def factorial(n):
  if n < 0:    
    ValueError("Inputs 0 or greater only") 
  result = 1
  for x in range(2, n + 1):
    result *= x
  
  return result

# test cases
print(factorial(3) == 6)
print(factorial(0) == 1)
print(factorial(5) == 120)
