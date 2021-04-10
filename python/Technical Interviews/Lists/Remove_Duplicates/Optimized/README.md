#### TECHNICAL INTERVIEW PROBLEMS IN PYTHON: LISTS

# [Remove Duplicates: Optimized](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-python-lists/exercises/tip-python-lists-duplicates-no-space)

For the last problem our suggested solutions had **`O(N)` time** and/or **`O(N)` space complexity**.

We can’t improve the time complexity. 
We have to visit each value to determine whether or not it is a duplicate.

We can reduce the space complexity to **`O(1)` with an in-place solution**.

We’ll adjust the problem to allow for this space complexity. 
Now we want to alter a sorted input list with all duplicates moved to the end of the list.

The return value will be the index of the final unique value.
```python
duplicates = ['a', 'a', 'g', 't', 't', 'x', 'x', 'x']
remove_dups(duplicates)
# 3, index of the last unique value: 'x'
duplicates
# ['a', 'g', 't', 'x' 'a', 'x', 't', 'x']
```

## Clarifying Questions:

### Does the ordering of the duplicate(s) matter?

No! They can be in any order.
