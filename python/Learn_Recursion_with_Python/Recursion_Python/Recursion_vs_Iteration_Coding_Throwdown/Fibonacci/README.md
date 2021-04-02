# [`fibonacci()`](https://www.codecademy.com/courses/learn-recursion-python/lessons/iteration-recursion-python/exercises/iteration-recursion-python-fib)
`fibonacci()` should return the `n`th Fibonacci number, where `n` is the number given as input. 
The first two numbers of a Fibonacci Sequence start with `0` and `1`. 
Every subsequent number is the sum of the previous two.

Our recursive implementation:
```
# runtime: Exponential - O(2^N)
 
def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)
 
fibonacci(3)
# 2
fibonacci(7)
# 13
fibonacci(0)
# 0
```
