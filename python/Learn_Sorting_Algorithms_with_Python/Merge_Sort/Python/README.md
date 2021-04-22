#### MERGE SORT: PYTHON

# [Separation](https://www.codecademy.com/courses/sorting-algorithms/lessons/merge-sort-python/exercises/separation)

What is sorted by a sort? 
A sort takes in a list of some data. 
The data can be words that we want to sort in dictionary order, or people we want to sort by birth date, or really anything else that has an order. 
For the simplicity of this lesson, we’re going to imagine the data as just numbers.

The first step in a merge sort is to separate the data into smaller lists. 
Then we break those lists into even smaller lists. 
Then, when those lists are all single-element lists, something amazing happens! 
Well, kind of amazing. 
Well, you might have expected it, we do call it a “merge sort”. 
We merge the lists.
```python
def merge_sort(items):
  
  if len(items) < 2:
    return items
```

# [Partitions](https://www.codecademy.com/courses/sorting-algorithms/lessons/merge-sort-python/exercises/partition)

How do we break up the data in a merge sort? 
We split it in half until there’s no more data to split. 
Our first step is to break down all of the items of the list into their own list.
```python
def merge_sort(items):
  
  if len(items) <= 1:
    return items
  
  middle_index = len(items) // 2
  left_split = items[ : middle_index]
  right_split = items[middle_index : ]
```

# [Creating the Merge Function](https://www.codecademy.com/courses/sorting-algorithms/lessons/merge-sort-python/exercises/creating-the-merge-function)

Our `merge_sort()` function so far only separates the input list into many different parts — pretty much the opposite of what you’d expect a merge sort to do. 
To actually perform the merging, we’re going to define a helper function that joins the data together.
```python
def merge(left, right):
  result = []

  return result
```

# [Merging](https://www.codecademy.com/courses/sorting-algorithms/lessons/merge-sort-python/exercises/performing-the-merge)

Now we need to build out our result list. 
When we’re merging our lists together, we’re creating ordered lists that combine the elements of two lists.
```python
def merge(left, right):
  result = []

  while left and right:
    if left[0] < right[0]:
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))

  return result
```

# [Finishing the Merge](https://www.codecademy.com/courses/sorting-algorithms/lessons/merge-sort-python/exercises/finishing-the-merge)

Since we’ve only technically depleted one of our two inputs to `merge()`, 
we want to add in the rest of the values to finish off our `merge()` function and return the sorted list.
```python
def merge(left, right):
  result = []

  while (left and right):
    if left[0] < right[0]:
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))

  result += left if left else right

  return result
```

# [Finishing the Sort](https://www.codecademy.com/courses/sorting-algorithms/lessons/merge-sort-python/exercises/finishing-the-sort)

Let’s update our `merge_sort()` function so that it returns a sorted list finally!
```python
def merge_sort(items):

  # base case:
  if len(items) <= 1:
    return items

  # recursive step:
  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]

  left_sorted = merge_sort(left_split)
  right_sorted = merge_sort(right_split)

  return merge(left_sorted, right_sorted)
```

# [Testing the Sort](https://www.codecademy.com/courses/sorting-algorithms/lessons/merge-sort-python/exercises/testing-the-sort)

We’ve written our merge sort! 
The whole sort takes up two functions:
* **`merge_sort()`** which is called recursively breaks down an input list to smaller, more manageable pieces. 
* **`merge()`** which is a helper function built to help combine those broken-down lists into ordered combination lists.

`merge_sort()` continues to break down an input list until it only has one element and then it joins that with other single element lists to create sorted 2-element lists. 
Then it combines 2-element sorted lists into 4-element sorted lists. 
It continues that way until all the items of the lists are sorted!

Only one thing left to do, test it out!
