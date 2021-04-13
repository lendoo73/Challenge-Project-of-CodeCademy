#### ONE-SAMPLE T-TESTS IN SCIPY

# [Introduction](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/t-tests-in-scipy/exercises/introduction)

One-sample t-tests are used for comparing a sample average to a hypothetical population average. 
For example, a one-sample t-test might be used to address questions such as:
* Is the average amount of time that visitors spend on a website different from 5 minutes?
* Is the average amount of money that customers spend on a purchase more than 10 USD?
As an example, let’s imagine the fictional business BuyPie, which sends ingredients for pies to your household so that you can make them from scratch. 
Suppose that a product manager wants online BuyPie orders to cost around 1000 Rupees on average. 
In the past day, 50 people made an online purchase and the average payment per order was less than 1000 Rupees. 
Are people really spending less than 1000 Rupees on average? 
Or is this the result of chance and a small sample size?

# [Implementing a One-Sample T-Test](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/t-tests-in-scipy/exercises/implementing-a-t-test)

In the last exercise, we inspected a sample of 50 purchase prices at BuyPie and saw that the average was 980 Rupees. 
Suppose that we want to run a one-sample t-test with the following null and alternative hypotheses:
* **Null**: The average cost of a BuyPie order is 1000 Rupees
* **Alternative**: The average cost of a BuyPie order is not 1000 Rupees.

SciPy has a function called `ttest_1samp()`, which performs a one-sample t-test for you. 
`ttest_1samp()` requires two inputs, a sample distribution (eg. the list of the 50 observed purchase prices) and a mean to test against (eg. `1000`):
```
tstat, pval = ttest_1samp(sample_distribution, expected_mean)
```
The function uses your sample distribution to determine the sample size and estimate the amount of variation in the population — which are used to estimate the null distribution. 

It returns two outputs: 
* the t-statistic (which we won’t cover in this course), 
* and the p-value.

# [Assumptions of a One Sample T-Test](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/t-tests-in-scipy/exercises/assumptions-of-a-t-test)

When running any hypothesis test, it is important to know and verify the assumptions of the test. 
The assumptions of a one-sample t-test are as follows:
* The sample was randomly selected from the population
  * For example, if you only collect data for site visitors who agree to share their personal information, this subset of visitors was not randomly selected and may differ from the larger population.
* The individual observations were independent
  * For example, if one visitor to BuyPie loves the apple pie they bought so much that they convinced their friend to buy one too, those observations were not independent.
* The data is normally distributed without outliers OR the sample size is large (enough)
  * There are no set rules on what a “large enough” sample size is, but a common threshold is around 40. 
  For sample sizes smaller than 40, and really all samples in general, it’s a good idea to make sure to plot a histogram of your data and check for outliers, multi-modal distributions (with multiple humps), or skewed distributions. 
  If you see any of those things for a small sample, a t-test is probably not appropriate.

In general, if you run an experiment that violates (or possibly violates) one of these assumptions, you can still run the test and report the results — but you should also report assumptions that were not met and acknowledge that the test results could be flawed.

# [Review](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/t-tests-in-scipy/exercises/review)

* One-sample t-tests are used for comparing a sample mean to an expected population mean
* A one-sample t-test can be implemented in Python using the SciPy `ttest_1samp()` function
* Assumptions of a one-sample t-test include:
 * The sample was randomly drawn from the population of interest
 * The observations in the sample are independent
 * The sample size is large “enough” or the sample data is normally distributed
