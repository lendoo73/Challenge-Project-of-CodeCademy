#### TECHNICAL INTERVIEW PROBLEMS: DYNAMIC PROGRAMMING

# Knapsack With Memoization

## [Building the Grid](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-dynamic-programming/exercises/dynamic-programming-memo-knapsack-i)

Our brute force approach is inefficient! 
We’re compounding work by creating many different combinations that contain the same items. 
Just like with Fibonacci, we’re repeating computations that won’t change.

With the Fibonacci Sequence, we had one variable to store: the number itself. 
We could place that number in a Python dictionary and look it up as needed.

Now we’re dealing with multiple variables: the item’s weight and value as well as the capacity of the knapsack. 
A dictionary’s key-value pairs won’t be sufficient to store all the answers to our subproblems.

We’ll start tackling this problem by building a grid which can store all our sub-answers.

The **columns** of our grid represent **each possible capacity** up to the weight limit.

The **rows** of our grid represent **each possible item** we can fit into a knapsack.

Why do we want each possible capacity? 
Because finding the optimal capacity for a knapsack of weight `4` will be much more efficient if we already know the optimal capacities for knapsacks of weight `3` and `1`!

## [Filling in the Grid](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-dynamic-programming/exercises/dynamic-programming-memo-knapsack-ii)

With our grid built, we only need to fill it in to find our optimal value. 
Remember: each **column** is the **capacity of a knapsack** and each **row** is an **item** we can add. 
The first row is “no item” and the first column is “no capacity”.

We’ll consider the diamond first. 
It weighs 1 pound and is worth $7. For each capacity after 0 (our first column), we can place the diamond in that location. 
Some capacities have spare weight, but that’s okay.
```python
           # Capacity: 0| 1| 2| 3| 4|
#____________________________________
# first row: no item! [0, 0, 0, 0, 0]
# second row: Diamond [0, 7, 7, 7, 7]
```
Let’s add a trophy worth $6 and weighing 2 lbs.

The trophy doesn’t fit in a 1lb. knapsack, so we look at the previous row and fill this section with that value.
```python
           # Capacity: 0| 1| 2| 3| 4|
#____________________________________
# first row: no item! [0, 0, 0, 0, 0]
# second row: Diamond [0, (7), 7, 7, 7]
# third row: Trophy   [0, (7), ?, ?, ?]
```
The trophy fits in the 2lb. knapsack; we have two options:
1. Trophy plus value stored at the remaining weight
2. The previous best in the 2lb. sub-knapsack.

Adding the 2 lb. trophy would mean 0 remaining capacity. 
This is why “no capacity”, “no item” values live in our grid.

Option 1 = 6 (trophy value) + 0 (“no capacity” value)

Option 2 = 7 (the previous best)

By weighing our options, we see this section should store the diamond value even though there’s spare weight. 
We’re maximizing for value!
```python
           # Capacity: 0| 1| 2| 3| 4|
#____________________________________
# first row: no item! [0, 0, 0, 0, 0]
# second row: Diamond [0, 7, 7, 7, 7]
# third row: Trophy   [0, 7, 7, ?, ?]
```
We repeat this process with the 3lb. sub-knapsack:

Option 1 = 6 (trophy value) + 7 (1lb. sub-knapsack value)  
Option 2 = 7 (the previous best)
```python
           # Capacity: 0| 1| 2| 3| 4|
#____________________________________
# first row: no item! [0, 0, 0, 0, 0]
# second row: Diamond [0, 7, 7, 7, 7]
# third row: Trophy   [0, 7, 7, 13, ?]
```
One last time for the 4lb. knapsack:

Option 1 = 6 (trophy value) + 7 (2lb. sub-knapsack value)  
Option 2 = 7 (the previous best)
```python
           # Capacity: 0| 1| 2| 3| 4|
#____________________________________
# first row: no item! [0, 0, 0, 0, 0]
# second row: Diamond [0, 7, 7, 7, 7]
# third row: Trophy   [0, 7, 7, 13, 13]
```
Note that the best value is stored in our bottom-right section. 
This is true no matter how many items we add.

The order we consider items is irrelevant for the final value. 
Here’s how the grid would look trophy-first:
```python
           # Capacity: 0| 1| 2| 3| 4|
#____________________________________
# first row: no item! [0, 0, 0, 0, 0]
# second row: Trophy  [0, 0, 6, 6, 6]
# third row: Diamond  [0, 7, 7, 13, 13]
```
