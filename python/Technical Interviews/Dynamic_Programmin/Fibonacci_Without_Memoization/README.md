#### TECHNICAL INTERVIEW PROBLEMS: DYNAMIC PROGRAMMING
# [Fibonacci Without Memoization](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-dynamic-programming/exercises/dynamic-programming-naive-fib)

Storing answers to sub-problems is an essential aspect of dynamic programming. 
Let’s explore why this is the case.

The [Fibonacci Sequence](https://en.wikipedia.org/wiki/Fibonacci_number)
is a series of numbers where the next number equals the sum of the previous two, starting with `0` and `1`.

Here’s a list of the first 10 Fibonacci numbers: 
`0, 1, 1, 2, 3, 5, 8, 13, 21`. 
The zeroth Fibonacci number is `0`.

We can express this sequence as a function:
```python
f(n) = f(n - 1) + f(n - 2)
```
We’ve written a Python function that returns the `n`th Fibonacci number.

Let’s add some print statements so we can see how often we’re repeating work in the current implementation.
