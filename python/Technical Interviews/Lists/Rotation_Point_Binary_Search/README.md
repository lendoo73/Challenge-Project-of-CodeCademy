#### TECHNICAL INTERVIEW PROBLEMS IN PYTHON: LISTS

# [Rotation Point: Binary Search](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-python-lists/exercises/tip-python-lists-count-binary)

Our last problem had a sorted dataset as the input. 
Sure, it was rotated, but it started out sorted.

A sorted list gives us ways to leverage that ordering. 
After all, someone went through a lot of work putting that data in order!

Binary search is an algorithm which finds a target value in sorted datasets in `O(logN)` time using knowledge of the dataset to guide the search.

We check the middle value. 
If it matches our target, we’ve found the value. 
If the middle value is greater than our target, we can safely ignore everything with a larger index because those values will also be greater. 
This cuts the problem in half.

Our target is the element with a unique property: the values at the previous and following index both have a greater value.

This is only true at the index where the rotation “finished” because it marks the beginning of a sorted list.
```python
rotated = ['c', 'd', 'e', 'f', 'a', 'b']
# rotation index is 4
 
'a' < 'b'
# True
'a' < 'f'
# True
```
Use a modified binary search algorithm to improve our solution’s time efficiency from `O(N)` to `O(logN)`.
