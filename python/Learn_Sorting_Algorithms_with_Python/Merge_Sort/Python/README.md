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

# [Partitions](https://www.codecademy.com/courses/sorting-algorithms/lessons/merge-sort-python/exercises/partition)

How do we break up the data in a merge sort? 
We split it in half until there’s no more data to split. 
Our first step is to break down all of the items of the list into their own list.

# [Creating the Merge Function](https://www.codecademy.com/courses/sorting-algorithms/lessons/merge-sort-python/exercises/creating-the-merge-function)

Our `merge_sort()` function so far only separates the input list into many different parts — pretty much the opposite of what you’d expect a merge sort to do. 
To actually perform the merging, we’re going to define a helper function that joins the data together.

# [Merging](https://www.codecademy.com/courses/sorting-algorithms/lessons/merge-sort-python/exercises/performing-the-merge)

Now we need to build out our result list. 
When we’re merging our lists together, we’re creating ordered lists that combine the elements of two lists.

# [Finishing the Merge](https://www.codecademy.com/courses/sorting-algorithms/lessons/merge-sort-python/exercises/finishing-the-merge)

Since we’ve only technically depleted one of our two inputs to `merge()`, 
we want to add in the rest of the values to finish off our `merge()` function and return the sorted list.










