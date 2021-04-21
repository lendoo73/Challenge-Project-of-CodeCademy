#### BUBBLE SORT: CONCEPTUAL

# [Bubble Sort Introduction](https://www.codecademy.com/courses/sorting-algorithms/lessons/bubble-sort-conceptual/exercises/bubble-sort-conceptual-intro)

Bubble sort is an introductory sorting algorithm that iterates through a list and compares pairings of adjacent elements.

According to the sorting criteria, the algorithm swaps elements to shift elements towards the beginning or end of the list.

By default, a list is sorted if for any element `e` and position `1` through `N`:

`e1` <= `e2` <= `e3` … `eN`, where `N` is the number of elements in the list.

For example, bubble sort transforms a list:
```python
[5, 2, 9, 1, 5]
```
to an ascending order, from lowest to highest:
```python
[1, 2, 5, 5, 9]
```
We implement the algorithm with two loops.

The first loop iterates as long as the list is unsorted and we assume it’s unsorted to start.

Within this loop, another iteration moves through the list. For each pairing, the algorithm asks:

In comparison, is the first element larger than the second element?

If it is, we swap the position of the elements. 
The larger element is now at a greater index than the smaller element.

When a swap is made, we know the list is still unsorted. 
The outer loop will run again when the inner loop concludes.

The process repeats until the largest element makes its way to the last index of the list. 
The outer loop runs until no swaps are made within the inner loop.

![boubble short](BubbleSort.webp)
