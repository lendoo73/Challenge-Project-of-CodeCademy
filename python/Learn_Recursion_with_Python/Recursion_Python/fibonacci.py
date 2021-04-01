# define the fibonacci() function below...
def fibonacci(n):
  # base cases:
  if n == 1:
    return 1
  if n == 0:
    return 0
  
  # recursive step:
  print("n: ", n)
  return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(7))
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "2^N"
