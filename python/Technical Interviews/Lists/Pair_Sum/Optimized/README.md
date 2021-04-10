#### TECHNICAL INTERVIEW PROBLEMS IN PYTHON: LISTS

# [Pair Sum: Optimized](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-python-lists/exercises/tip-python-lists-pair-optimize)

We’ll explore a common trade-off: time vs. space.

Our previous solution used nested for loops to 
**iterate through each element** in the list and then 
**iterate again for each element** in the list to find their sum for a **`O(N^2)` time complexity**.

On the bright side, that solution used **`O(1)` space** because **we’re not using any additional data structures**.

If we **sort the list** before looking for pairs, we can reach **`O(N * logN)` time complexity**, 
but we’re going to go for a **`O(N)`** solution by **trading** away a little space.

Engineering is about trade-offs! This is another opportunity to communicate benefits and drawbacks to the interviewer.

As with other naive solutions, we’re doing more work than is necessary. 
Given the target integer, what information we can gather in a single iteration?
```python
# <> marks the current element
nums = [4, 2, 8, 9, 6]
target = 8
 
[<4>, 2, 8, 9, 6]
# target - 4 = 4
# we need another 4...
 
[4, <2>, 8, 9, 6]
# target - 2 = 6
# we need a 6...
 
[4, 2, <8>, 9, 6]
# target - 8 = 0
# we need a 0...
 
[4, 2, 8, <9>, 6]
# target - 9 = -1
# we need a -1...
 
[4, 2, 8, 9, <6>]
# target - 6 = 2
# we need a 2...
```
At each step of the iteration, we know the “complement” number needed to sum to the target.

Use a dictionary to store that complement at each iteration and solve this problem with **`O(N)` time complexity and `O(N)` space complexity**.
