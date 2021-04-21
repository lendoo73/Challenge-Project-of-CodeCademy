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


