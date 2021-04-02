def multiplication(num1, num2, result = 0):
  # Base case: 
  if num2 < 1:
    return result
  # Recursive step:
  result += num1
  return multiplication(num1, num2 - 1, result)


# test cases
print(multiplication(3, 7) == 21)
print(multiplication(5, 5) == 25)
print(multiplication(0, 4) == 0)
