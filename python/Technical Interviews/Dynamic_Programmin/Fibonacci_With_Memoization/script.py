num_in_fibonacci = 998
function_calls = []

def fibonacci(num, memo):
  function_calls.append(1)
  if num < 0:
    print("Not a valid number")
  if num <= 1:
    return num
  elif memo.get(num):
    return memo.get(num)
  else:
    memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo)
    return memo[num]
  
  
fibonacci_result = fibonacci(num_in_fibonacci, {})
print("Number {0} in the fibonacci sequence is {1}.".format(num_in_fibonacci, fibonacci_result))

print("Fibonacci function called {0} total times!".format(len(function_calls)))
