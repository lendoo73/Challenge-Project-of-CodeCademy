#### RADIX SORT: PYTHON

# [Finding the Max Exponent](https://www.codecademy.com/courses/sorting-algorithms/lessons/radix-sort-python/exercises/finding-max-exponent)

In our version of least significant digit radix sort, we’re going to utilize the string representation of each integer. 
This, combined with negative indexing, will allow us to count each digit in a number from right-to-left.

Some other implementations utilize integer division and modular arithmetic to find each digit in a radix sort, but our goal here is to build an intuition for how the sort works.

Our first step is going to be finding the `max_exponent`, which is the number of digits long the largest number is. 
We’re going to find the largest number, cast it to a string, and take the length of that string.
```python
def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))
```

# [Setting Up For Sorting](https://www.codecademy.com/courses/sorting-algorithms/lessons/radix-sort-python/exercises/setting-up-for-sorting)

In this implementation, we’re going to build the radix sort naturally, from the inside out. 
The first step we’re going to take is going to be our inner-most loop, so that we know we’ll be solid when we’re iterating through each of the exponents.
```python
def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))

  # create copy of to_be_sorted here
  being_sorted = to_be_sorted[:]

  digits = [ [] for num in range(10)]

  return digits

print(radix_sort([1, 2]))
```

# [Bucketing Numbers](https://www.codecademy.com/courses/sorting-algorithms/lessons/radix-sort-python/exercises/bucketing-numbers)

The least significant digit radix sort algorithm takes each number in the input list, looks at the digits of that number in order from right to left, 
and incrementally stuffs each number into the bucket corresponding to the value of that digit.

First we’re going to write this logic for the least significant digit, then we’re going to loop over the code we write to do that for every digit.
```python
ef radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))

  being_sorted = to_be_sorted[:]
  digits = [[] for i in range(10)]

  # create for loop here:
  for number in being_sorted:
    number_as_a_string = str(number)
    digit = number_as_a_string[-1]
    digit = int(digit)
    
    digits[digit].append(number)
```

# [Rendering the List](https://www.codecademy.com/courses/sorting-algorithms/lessons/radix-sort-python/exercises/rendering-the-list)

For every iteration, radix sort renders a version of the input list that is sorted based on the digit that was just looked at. 
At first pass, only the ones digit is sorted. 
At the second pass, the tens and the ones are sorted. 
This goes on until the digits in the largest position of the largest number in the list are all sorted, and the list is sorted at that time.

Here we’ll be rendering the list, at first, it will just return the list sorted so just the ones digit is sorted.
```python
def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))

  being_sorted = to_be_sorted[:]
  digits = [[] for i in range(10)]

  for number in being_sorted:
    number_as_a_string = str(number)
    digit = number_as_a_string[-1]
    digit = int(digit)
    
    digits[digit].append(number)

  # reassign being_sorted here:
  being_sorted = []
  for numeral in digits:
    being_sorted.extend(numeral)

  return being_sorted
```

# [Iterating through Exponents](https://www.codecademy.com/courses/sorting-algorithms/lessons/radix-sort-python/exercises/iterating-through-exponents)

We have the interior of our radix sort, which right now goes through a list and sorts it by the first digit in each number. 
That’s a pretty great start actually. 
It won’t be hard for us to go over every digit in a number now that we can already sort by a given digit.
```python
def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))
  being_sorted = to_be_sorted[:]

  # Add new for-loop here:
  for exponent in range(max_exponent):
    position = exponent + 1
    index = - position
    digits = [[] for i in range(10)]

    for number in being_sorted:
      number_as_a_string = str(number)
      digit = number_as_a_string[index]
      digit = int(digit)
      
      digits[digit].append(number)

    being_sorted = []
    for numeral in digits:
      being_sorted.extend(numeral)

  return being_sorted
```

# [Review (and Bug Fix!)](https://www.codecademy.com/courses/sorting-algorithms/lessons/radix-sort-python/exercises/bugfix-and-reveiw)

```python
def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))
  being_sorted = to_be_sorted[:]

  for exponent in range(max_exponent):
    position = exponent + 1
    index = -position

    digits = [[] for i in range(10)]

    for number in being_sorted:
      number_as_a_string = str(number)
      try:
        digit = number_as_a_string[index]
      except IndexError:
        digit = 0
      digit = int(digit)

      digits[digit].append(number)

    being_sorted = []
    for numeral in digits:
      being_sorted.extend(numeral)

  return being_sorted

unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 355, 689, 621, 183, 182, 524, 1]

print(radix_sort(unsorted_list))

```




