#### HYPOTHESIS TESTING: ASSOCIATIONS

# [Multiple Tests]

In the previous exercise, we used a two-sample t-test to investigate an association between 
* a quantitative variable (time spent on a website) 
* and a binary categorical variable (an old color scheme or a new color scheme).

In some circumstances, we might instead care about an association between 
* a quantitative variable 
* and a non-binary categorical variable (non-binary means more than two categories).

For example, suppose that we own a chain of stores that sell ants, called VeryAnts. 
There are three different locations: A, B, and C. 
We want to know whether customers are spending a significantly different amount per order at any of the locations.

There are three different comparisons we could make: 
* A vs. B, 
* B vs. C, 
* and A vs. C. 

One way to answer our question is to simply run three separate 2-sample t-tests.
