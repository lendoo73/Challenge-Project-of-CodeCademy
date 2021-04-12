#### TECHNICAL INTERVIEW PROBLEMS: DYNAMIC PROGRAMMING

# [Fibonacci With Memoization](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-dynamic-programming/exercises/dynamic-programming-memo-fib)

The Fibonacci sequence is a perfect case to apply dynamic programming. 
Each Fibonacci number relies on two previous numbers, and those **numbers never change**. 
We have overlapping sub-problems!

We’ll store the answers to sub-problems using *memoization*. 
Think of it like jotting notes down on a memo.

With each sub-problem, we’ll check if we have a note in our memo. 
If we do, then we can use that information, otherwise, we’ll need to do a calculation and then store that calculation in our memo pad!

Remember these notes are possible because the answer will always be the same: 
the `n`th Fibonacci number will never change. 
Just like the `1 + 1 + 1 + 1` example, 
we don’t need to recompute the 3rd and 4th Fibonacci number to calculate the 5th Fibonacci number if we already know the 3rd and 4th number.
