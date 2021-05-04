#### INTRODUCTION TO PROBABILITY DISTRIBUTIONS

# [Random Variables](https://www.codecademy.com/courses/probability-mssp/lessons/introduction-to-probability-distributions/exercises/random-variables)

A random variable is, in its simplest form, a function. 
It can equal any possible outcome from the sample space of an event.

Random variables must be numeric, meaning they always take on a number rather than a characteristic or quality. 
For example, when rolling a six-sided fair die, the random variable would be the number (between 1 and 6) from the resulting roll.

If the observed event does not have a numeric outcome, we can assign the random variable to equal 1 if there is a specific outcome and 0 otherwise. 
For example, when observing a fair coin flip, we can assign a “heads” to be the value 1 and a “tails” to be the value 0.

We will be using `random.choice(a, size = size, replace = True/False)` from the `numpy` library to simulate random variables in python. 
In this method:
* `a` is a list or other object that has values we are sampling from
* `size` is a number that represents how many values to  choose
* `replace` will equal either `True` or `False` to represent whether 
  * we will keep a value in a after drawing it (`replace = True`) 
  * or if we remove it from the pool (`replace = False`). 
If we were to roll a die multiple times, we would use `replace = True` because we don’t remove a value after observing it. 
But if we were to draw a card and leave it out of the deck before drawing again, we would do `replace = False`.

The following code simulates the outcome of rolling a fair die twice using `np.random.choice()`:
```py
import numpy as np
 
# 7 is not included in the range function
die_6 = range(1, 7)
 
rolls = np.random.choice(die_6, size = 2, replace = True)
 
print(rolls)
Output:

# [2, 5]
```
