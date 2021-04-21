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



