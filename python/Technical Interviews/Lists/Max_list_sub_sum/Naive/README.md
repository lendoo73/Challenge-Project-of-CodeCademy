#### TECHNICAL INTERVIEW PROBLEMS IN PYTHON: LISTS

# [Max list sub-sum: Naive](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-python-lists/exercises/tip-python-lists-mass-naive)

Our next problem calculates sums within a list.

Given a list of integers, return the maximum sum possible from a contiguous sub-list. 
A sub-list is an uninterrupted portion of the list (up to and including the entire list).
```python
nums = [1, -7, 2, 15, -11, 2]
 
maximum_sub_sum(nums)
# 17
# The sum of sub-list nums[2:4]
```

## Clarifying Questions:

### Are there constraints on time or space efficiency?

No! Any solution will do.

### Are all the numbers positive?

No! Negative numbers can be in the input.

### How big or small can the sub-list be?

From a single element to the entire list.

