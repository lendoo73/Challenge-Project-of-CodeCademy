#### TECHNICAL INTERVIEW PROBLEMS IN PYTHON: LISTS

# [Pair Sum: Naive](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-python-lists/exercises/tip-python-lists-pair-naive)

We’ll end with a classic interview question: 
given a list of integers and a “target” integer, return a pair of indices whose values sum to the target.
```python
nums = [4, 2, 8, 9, 6]
target = 8
 
pair_sum(nums, target)
# nums[1] + nums[4] == 8
# [1, 4]
 
pair_sum(nums, 17)
# nums[2] + nums[3] == 17
# [2, 3]
 
pair_sum(nums, 99)
# no pair sum exists...
# None
```

## Clarifying Questions:

### Are there constraints on time or space efficiency?

No! Any solution will do.

### Can the numbers be negative or 0?

Yes! Your solution should handle those inputs.

### Does the order of indices matter?

The earlier index comes first in the return list.

### Do we return all pairs that match a solution?

No! The first one that your solution finds will do!
