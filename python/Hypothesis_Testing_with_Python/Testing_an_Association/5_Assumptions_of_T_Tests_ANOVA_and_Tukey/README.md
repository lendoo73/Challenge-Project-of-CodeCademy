####

# [Assumptions of T-Tests, ANOVA, and Tukey](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/hypothesis-testing-associations/exercises/assumptions-of-the-test)

Before we use a two sample t-test, ANOVA, or Tukey’s range test, we need to be sure that the following things are true:

## 1. The observations should be independently randomly sampled from the population
Suppose the population we are interested in is all visitors to a website. 
Random sampling will help ensure that our sample is representative of the population we care about. 
For example, if we only sample site visitors on Halloween, those visitors may behave differently from the general population. 
In practice, this can be a challenging assumption to meet, but it’s important to be aware of.

## 2. The standard deviations of the groups should be equal
For example, if we’re comparing time spent on a website for two versions of a homepage, 
we first want to make sure that the standard deviation of time spent on version 1 is roughly equal to the standard deviation of time spent on version 2. 
To check this assumption, it is normally sufficient to divide one standard deviation by the other and see if the ratio is “close” to 1. 
Generally, a **ratio between 0.9 and 1.1** should suffice.

That said, there is also a way to run a 2-sample t-test without assuming equal standard deviations — for example, 
by setting the `equal_var` parameter in the `scipy.stats.ttest_ind()` function equal to `False`. 
Running the test in this way has some disadvantages (it essentially makes it harder to reject the null hypothesis even when there is a true difference between groups), 
so it’s important to check for equal standard deviations before running the test.

## 3. The data should be normally distributed…ish
Data analysts in the real world often still perform these tests on data that are not normally distributed. 
This is usually not a problem if sample size is large, but it depends on how non-normal the data is. 
In general, the bigger the sample size, the safer you are!

## 4. The groups created by the categorical variable must be independent
Here are some examples where the groups are not independent:
* the number of goals scored per soccer player before, during, and after undergoing a rigorous training regimen 
(not independent because the same players are measured in each category)
* years of schooling completed by a group of adults compared to their parents (not independent because kids and their parents can influence one another)
