#### RECURSION: PYTHON
# [Building Our Own Call Stack](https://www.codecademy.com/courses/learn-recursion-python/lessons/recursion-python/exercises/recursion-python-intro)
Before we dive into recursion, let’s replicate what’s happening in the call stack with an **iterative function**.

Let’s write a function that sums every number from 1 to the given input.
```
sum_to_one(4)
# 10
sum_to_one(11)
# 66
```
The **call stack** stores each function (with its internal variables) until those functions resolve in a *last in*, *first out order*.
```
call_stack = []
recursive_func()
call_stack = [recursive_func_1]
 
# within the body of recursive_func, another call to recursive_func()
call_stack = [recursive_func_1, recursive_func_2]
# the body of the second call to recursive_func resolves...
call_stack = [recursive_func_1]
# the body of the original call to recursive_func resolves...
call_stack = [] 
```
Execution contexts are a mapping between variable names and their values within the function during execution. 
We can use a list for our call stack and a dictionary for each execution context.

# [Sum to One with Recursion](https://www.codecademy.com/courses/learn-recursion-python/lessons/recursion-python/exercises/recursion-python-sum)
We want a function that takes an integer as an input and returns the sum of all numbers from the input down to 1.
```
sum_to_one(4)
# 4 + 3 + 2 + 1
# 10
```
Here’s how this function would look if we were to write it iteratively:
```
def sum_to_one(n):
  result = 0
  for num in range(n, 0, -1):
    result += num
  return result
 
sum_to_one(4)
# num is set to 4, 3, 2, and 1
# 10
```
We can think of each recursive call as an iteration of the loop above. In other words, we want a recursive function that will produce the following function calls:
```
recursive_sum_to_one(4)
recursive_sum_to_one(3)
recursive_sum_to_one(2)
recursive_sum_to_one(1)
```
Every recursive function needs a ***base case*** when the function does not recurse, and a ***recursive step***, when the recursing function moves towards the base case.

**Base case:** The integer given as input is 1.

**Recursive step:** The recursive function call is passed an argument 1 less than the last function call.











