num_in_fibonacci = 10
arguments_count = {}

def fibonacci(num):
  count = arguments_count.get(num, 0)
  if num < 0:
    print("Not a valid number")
  if num <= 1:
    return num
  else:
    count += 1
    arguments_count[num] = count
    return fibonacci(num - 1) + fibonacci(num - 2)
  

print("Number {0} in the fibonacci sequence is {1}.".format(num_in_fibonacci, fibonacci(num_in_fibonacci)))
      
for num, count in arguments_count.items():
  print("Argument {0} seen {1} time(s)!".format(num, count))

print("Fibonacci function called {0} total times!".format(sum(arguments_count.values())))
