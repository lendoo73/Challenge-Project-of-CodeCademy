#### BUBBLE SORT: PYTHON

# [Bubble Sort: Swap](https://www.codecademy.com/courses/sorting-algorithms/lessons/bubble-sort-python/exercises/bubble-sort-python-swap)

The Bubble Sort algorithm works by comparing a pair of neighbor elements and shifting the larger of the two to the right. 
Bubble Sort completes this by swapping the two elements’ positions if the first element being compared is larger than the second element being compared.

Below is a quick pseudocode example of what we will create:
```python
for each pair(elem1, elem2):
  if elem1 > elem2:
    swap(elem1, elem2)
  else:
    # analyze next set of pairs
```
This `swap()` sub-routine is an essential part of the algorithm. 
Bubble sort swaps elements repeatedly until the largest element in the list is placed at the greatest index. 
This looping continues until the list is sorted.

# [Bubble Sort: Compare](https://www.codecademy.com/courses/sorting-algorithms/lessons/bubble-sort-python/exercises/bubble-sort-python-compare)

Now that we know how to swap items in an array, we need to set up the loops which check whether a swap is necessary.

Recall that Bubble Sort compares neighboring items and if they are out of order, they are swapped.

What does it mean to be “out of order”? 
Since bubble sort is a comparison sort, we’ll use a comparison operator: <.

We’ll have two loops:
1. One loop will iterate through each element in the list.
2. Within the first loop, we’ll have another loop for each element in the list.

Inside the second loop, we’ll take the index of the loop and compare the element at that index with the element at the next index. 
If they’re out of order, we’ll make a swap!

# [Bubble Sort: Optimized](https://www.codecademy.com/courses/sorting-algorithms/lessons/bubble-sort-python/exercises/bubble-sort-python-review)

As you were writing Bubble Sort, you may have realized that we were doing some unnecessary iterations.

Consider the first pass through the outer loop. 
We’re making `n-1` comparisons.
```python
nums = [5, 4, 3, 2, 1]
# 5 element list: N is 5
bubble_sort(nums)
# 5 > 4
# [4, 5, 3, 2, 1]
# 5 > 3
# [4, 3, 5, 2, 1]
# 5 > 2
# [4, 3, 2, 5, 1]
# 5 > 1
# [4, 3, 2, 1, 5]
# four comparisons total
```
We know the last value in the list is in its correct position, so we never need to consider it again. 
The second time through the loop, we only need `n-2` comparisons.

As we correctly place more values, fewer elements need to be compared. 
An optimized version doesn’t make `n^2-n` comparisons, it does `(n-1) + (n-2) + ... + 2 + 1` comparisons, which can be simplified to `(n^2-n) / 2` comparisons.

This is fewer than `n^2`-n comparisons but the algorithm still has a big O runtime of `O(N^2)`.

As the input, `N`, grows larger, the division by two has less significance. 
Big O considers inputs as they reach infinity so the higher order term `N^2` completely dominates.

We can’t make Bubble Sort better than `O(N^2)`, but let’s take a look at the optimized code and compare iterations between implementations!

We’re also taking advantage of parallel assignment in Python and abstracting away the `swap()` function!
