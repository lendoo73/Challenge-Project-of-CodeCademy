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

# [Recursion and Big O](https://www.codecademy.com/courses/learn-recursion-python/lessons/recursion-python/exercises/recursion-python-big-o)
We’d like a function `factorial` that, given a positive integer as input, returns the product of every integer from 1 up to the input. 
**If the input is less than 2, return 1**.
```
factorial(4)
# 4 * 3 * 2 * 1
# 24
```
Since this function is similar to the previous problem, we’ll add an additional wrinkle. 
You’ll need to evaluate the big O runtime of the function.

With an iterative function, we would consider how the number of iterations grows in relation to the size of the input.

For example you may ask yourself, are we looping once more for each new element in the list?

That’s ***linear*** or ***`O(N)`***.

Are we looping an additional number of elements in the list for each new element in the list?

That’s ***quadratic*** or ***`O(N^2)`***.

With recursive functions, the thought process is similar but we’re replacing loop iterations **with recursive function calls**.

In other words, are we recursing once more for each new element in the list?

That’s ***linear*** or ***`O(N)`***.

Let’s analyze our previous function, `sum_to_one()`.
```
sum_to_one(4)
# recursive call to sum_to_one(3)
# recursive call to sum_to_one(2)
# recursive call to sum_to_one(1)
 
# Let's increase the input...
 
sum_to_one(5)
# recursive call to sum_to_one(4)
# recursive call to sum_to_one(3)
# recursive call to sum_to_one(2)
# recursive call to sum_to_one(1)
```
What do you think? We added one to the input, how many more recursive calls were necessary?

If you chose an input large enough, you should see a **`RecursionError`**.

# [Stack Over-Whoa!](https://www.codecademy.com/courses/learn-recursion-python/lessons/recursion-python/exercises/recursion-python-stack-overflow)
The previous exercise ended with a *stack overflow*, which is a reminder that recursion has costs that iteration doesn’t. 
We saw in the first exercise that **every recursive call spends time on the call stack**.

Put enough function calls on the call stack, and eventually there’s no room left.

Even when there is room for any reasonable input, recursive functions tend to be at least a little less efficient than comparable iterative solutions because of the call stack.

The beauty of recursion is how it can reduce complex problems into an elegant solution of only a few lines of code. 
Recursion forces us to distill a task into its smallest piece, the base case, and the smallest step to get there, the recursive step.

Let’s compare two solutions to a single problem: producing a power set. 
A power set is a list of all subsets of the values in a list.
```
power_set(['a', 'b', 'c'])
# [
#   ['a', 'b', 'c'], 
#   ['a', 'b'], 
#   ['a', 'c'], 
#   ['a'], 
#   ['b', 'c'], 
#   ['b'], 
#   ['c'], 
#   []
# ]
```
Our input length was 3, and the list returned had a length of 8.

Producing subsets **requires** a runtime of at least `O(2^N)`, we’ll never do better than that because a set of `N` elements creates a power set of `2^N` elements.

Binary, [a number system of base 2](https://en.wikipedia.org/wiki/Binary_number#Binary_counting)
, can represent `2^N` numbers for `N` binary digits. 
For example:
```
# 1 binary digit, 2 numbers
# 0 in binary
0
# 1 in binary
1
 
# 2 binary digits, 4 numbers
# 00 => 0
# 01 => 1
# 10 => 2
# 11 => 3
```
The iterative approach uses this insight for a very clever solution by including an element in the subset if its “binary digit” is `1`.
```
set = ['a', 'b', 'c']
binary_number = "101"
# produces the subset ['a', 'c']
# 'b' is left out because its binary digit is 0
```
That process is repeated **for all `O(2^N)` numbers!**

Here is the complete solution. 
You’re not expected to understand every line, just take in the level of complexity.
```
def power_set(set):
  power_set_size = 2**len(set)
  result = []
 
  for bit in range(0, power_set_size):
    sub_set = []
    for binary_digit in range(0, len(set)):
      if((bit & (1 << binary_digit)) > 0):
        sub_set.append(set[binary_digit])
    result.append(sub_set)
  return result
```
Very clever but not very intuitive! Let’s try recursion.

Consider the **base case**, where the problem has become so simple we can solve it without doing any work.

What’s the simplest power set possible? 
An empty list!
```
power_set([])
# [[]]
```
Now the **recursive step**. 
We need to progress towards our base case, an empty list, so **we’ll be removing an element from the input**.

Examine the simplest powerset that isn’t the base case:
```
power_set(['a'])
# [[], ['a']]
```
A power set in the recursive step requires:
* all subsets which contain the element
  * in this case `"a"`
* all subsets which don’t contain the element
  * in this case `[]`.

With the recursive approach, we’re able to articulate the problem **in terms of itself**. 
No need to bring in a whole number system to find the solution!

Here’s the recursive solution in its entirety:
```
def power_set(my_list):
  if len(my_list) == 0:
    return [[]]
  power_set_without_first = power_set(my_list[1:])
  with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
  return with_first + power_set_without_first
```
Neither of these solutions is simple, this is a complicated algorithm, but the recursive solution is almost half the code and more directly conveys what this algorithm does.

`O(2^N)` runtime!

# [No Nested Lists Anymore, I Want Them to Turn Flat](https://www.codecademy.com/courses/learn-recursion-python/lessons/recursion-python/exercises/recursion-python-flatten)
Let’s use recursion to solve another problem involving lists: `flatten()`.

We want to write a function that removes nested lists within a list **but keeps the values contained**.
```
nested_planets = [
    'mercury', 
    'venus', [
        'earth'
    ], 
    'mars', [
        [
            'jupiter', 
            'saturn'
        ]
    ], 
    'uranus', [
        'neptune', 
        'pluto'
    ]
]
 
flatten(nested_planets)
# ['mercury', 
#  'venus', 
#  'earth', 
#  'mars', 
#  'jupiter', 
#  'saturn', 
#  'uranus', 
#  'neptune', 
#  'pluto']
```
We want to identify a **base case**, and we need to think about a **recursive step** that takes us closer to achieving the base case.

For this problem, we have two scenarios as we move through the list.
* The element in the list **is a list itself**.
    * We have more work to do!
* The element in the list is not a list.
    * All set!
Which is the base case and which is the recursive step?








