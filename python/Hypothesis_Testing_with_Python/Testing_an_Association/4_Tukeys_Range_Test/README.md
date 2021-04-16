#### HYPOTHESIS TESTING: ASSOCIATIONS

# [Tukey's Range Test](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/hypothesis-testing-associations/exercises/tukeys-range-test)

Let’s say that we have performed an ANOVA to compare sales at the three VeryAnts stores. 
We calculated a p-value less than 0.05 and concluded that there is a significant difference between at least one pair of stores.

Now, we want to find out which pair of stores are different. 
This is where Tukey’s range test comes in handy!

In Python, we can perform Tukey’s range test using the `statsmodels` function `pairwise_tukeyhsd()`. 
For example, suppose we are again comparing video-game scores for math majors, writing majors, and psychology majors. 
We have a dataset named `data` with two columns: 
* `score` 
* and `major`. 

We could run Tukey’s range test with a type I error rate of 0.05 as follows:
```python
from statsmodels.stats.multicomp import pairwise_tukeyhsd

tukey_results = pairwise_tukeyhsd(data.score, data.major, 0.05)
print(tukey_results)
```
Output:
```python
Multiple Comparison of Means - Tukey HSD,FWER=0.05
==========================================
group1 group2 meandiff lower upper reject
------------------------------------------ 
  math  psych    3.32 -0.11  6.74  False 
  math  write    5.23  2.03  8.43  True
 psych  write   -2.12 -5.25  1.01  False 
------------------------------------------
```
Tukey’s range test is similar to running three separate 2-sample t-tests, except that it runs all of these tests simultaneously in order to preserve the type I error rate.

The function output is a table, with one row per pair-wise comparison. 
For every comparison where `reject` is `True`, we “reject the null hypothesis” and conclude **there is a significant difference between those two groups**. 
For example, in the output above, we would conclude that there is a significant difference between scores for math and writing majors, 
but no significant difference in scores for the other comparisons.
