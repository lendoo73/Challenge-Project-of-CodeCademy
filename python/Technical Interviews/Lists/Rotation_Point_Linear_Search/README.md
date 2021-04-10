#### [TECHNICAL INTERVIEW PROBLEMS IN PYTHON: LISTS]

# [Rotation Point: Linear Search](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-python-lists/exercises/tip-python-lists-count-linear)

We’ll continue our theme of list rotation by flipping the problem: given a **sorted list** rotated `k` times, return the index where the “unrotated” list would begin.
```python
rotated_list = ['c', 'd', 'e', 'f', 'a']
rotation_point(rotated_list)
# index 4
# a sorted list would start with 'a'
 
another_rotated_list = [13, 8, 9, 10, 11] 
rotation_point(rotated_list)
# index 1
# a sorted list would start with 8
```
## Clarifying Questions:

### Are there constraints on time or space efficiency?

No! Any solution will do.

### Does the rotation direction matter?

This won’t affect the return value.

### What if the input isn’t rotated?

Return 0.
