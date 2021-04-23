#### RADIX SORT: PYTHON

# [Finding the Max Exponent](https://www.codecademy.com/courses/sorting-algorithms/lessons/radix-sort-python/exercises/finding-max-exponent)

In our version of least significant digit radix sort, we’re going to utilize the string representation of each integer. This, combined with negative indexing, will allow us to count each digit in a number from right-to-left.

Some other implementations utilize integer division and modular arithmetic to find each digit in a radix sort, but our goal here is to build an intuition for how the sort works.

Our first step is going to be finding the max_exponent, which is the number of digits long the largest number is. We’re going to find the largest number, cast it to a string, and take the length of that string.
