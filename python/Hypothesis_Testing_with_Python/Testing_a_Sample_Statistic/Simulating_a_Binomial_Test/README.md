#### SIMULATING A BINOMIAL TEST

# [Introduction](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/simulating-a-binomial-test/exercises/introduction)

Binomial tests are useful for comparing the frequency of some outcome in a sample to the expected probability of that outcome. 
For example, if we expect 90% of ticketed passengers to show up for their flight but only 80 of 100 ticketed passengers actually show up, 
we could use a binomial test to understand whether 80 is significantly different from 90.

Binomial tests are similar to one-sample t-tests in that they test a sample statistic against some population-level expectation. 
The difference is that:
* binomial tests are used for binary categorical data to compare a sample frequency to an expected population-level probability
* one-sample t-tests are used for quantitative data to compare a sample mean to an expected population mean.

In Python, as in many other programming languages used for statistical computing, 
there are a number of libraries and functions that allow a data scientist to run a hypothesis test in a single line of code. 
However, a data scientist will be much more likely to spot and fix potential errors and interpret results correctly 
if they have a conceptual understanding of how these functions work.

# [Summarizing the Sample](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/simulating-a-binomial-test/exercises/summarizing-the-sample)

The marketing department at Live-it-LIVE reports that, during this time of year, about 10% of visitors to Live-it-LIVE.com make a purchase.

The monthly report shows every visitor to the site and whether or not they made a purchase. 
The checkout page had a small bug this month, so the business department wants to know whether the purchase rate dipped below expectation. 
They’ve asked us to investigate this question.

In order to run a hypothesis test to address this, we’ll first need to know two things from the data:
* The number of people who visited the website
* The number of people who made a purchase on the website

Assuming each row of our dataset represents a unique site visitor, 
we can calculate the number of people who visited the website by finding the number of rows in the data frame. 
We can then find the number who made a purchase by using a conditional statement to add up the total number of rows where a purchase was made.

For example, suppose that the dataset `candy` contains a column named `chocolate` with `'yes'` recorded for every candy that has chocolate in it and `'no'` otherwise. 
The following code calculates the sample size (the number of candies) and the number of those candies that contain chocolate:
```python
## sample size (number of rows): 
samp_size = len(candy)
 
## number with chocolate: 
total_with_chocolate = np.sum(candy.chocolate == 'yes')
