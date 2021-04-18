#### A/B TESTING: SAMPLE SIZE CALCULATORS

# [Introduction](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/a-b-test-sample-size-calculator/exercises/introduction)

An A/B Test is a scientific method of choosing between two options (Option A and Option B). 
Some examples of A/B tests include:
* What number of sale items on a website makes customers most likely to purchase something: 25 or 50?
* What color button are customers more likely to click on: blue or green?
* Do people spend more time on a website if the background is green or orange?

For **A/B tests** where the outcome of interest (eg., whether or not a customer makes a purchase) is **categorical**, 
an A/B test is conducted using a **Chi-Square hypothesis test**. 
In order **to determine the sample size** necessary for this kind of test, a sample size calculator requires three numbers:
* Baseline conversion rate
* Minimum detectable effect (also called the minimum desired lift)
* Statistical significance threshold

In this lesson, we will discuss each of these numbers and how a data scientist might choose them.

# [Baseline Conversion Rate](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/a-b-test-sample-size-calculator/exercises/baseline-conversion-rate)

A/B tests usually compare an option that we’re currently using to a new option that we suspect might be better. 
In order to compare the two options, we need a metric. 
Often, our metric will be the percent of users who take a certain action after interacting with one of our options. 
For instance:
* The percent of customers who buy a t-shirt after visiting one of two versions of a website
* The percent of users who click on one of two versions of an ad

In the t-shirt example above, the baseline conversion rate is our estimate for the percent of people who will buy a shirt under the current website design.

We can generally calculate a **baseline** by looking at **historical data for the option that we’re currently using**. 
For example, suppose that 2000 people visited a website over the past three months and 320 of those visitors purchased a shirt. 
We could estimate the baseline rate as follows:
```python
baseline = 320 / 2000 * 100
print(baseline) #output: 16.0
```
This number may be written as a **proportion** (eg., 0.16) **or** a **percent** (eg., 16%).

# [Minimum Detectable Effect](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/a-b-test-sample-size-calculator/exercises/minimum-detectable-effect)

Suppose we’re running an A/B Test to find out if a new website layout drives more subscriptions than the current one. 
If the new layout is only a tiny percent better, would we really care?

In order to detect precise differences, we need a very large sample size. 
In order to choose a sample size, we need to know the smallest difference that we actually care to measure. 
This “smallest difference” is our desired minimum detectable effect. 
This is also sometimes referred to as desired lift.

**Minimum detectable effect or lift** is generally expressed as a *percent of the baseline conversion rate*. 
Suppose that 6% of customers currently subscribe to our website (that’s our baseline conversion rate). 
Changing a website layout is hard, so we only think that it’s worth doing if at least 8% of our customers would subscribe with the new layout. 
To calculate this as a percentage of our baseline:
```python
baseline = 6
new = 8
min_detectable_effect = (new - baseline) / baseline * 100
print(min_detectable_effect) #output: 33.0
```
Our minimum detectable effect/desired lift is 33%.

# [Significance Threshold](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/a-b-test-sample-size-calculator/exercises/significance-threshold)

When we run an A/B test, we usually want to use the results of the test to make a decision: use version A or B? 
In order to make that decision, many data scientists use a pre-determined significance threshold for their hypothesis test. 
For example, if we set a **significance threshold** of 0.05 (a commonly chosen value), 
we’ll **“reject the null hypothesis”** and conclude that the conversion rate for version B is significantly different from version A **if** we get a **p-value less** than 0.05.

It turns out that this **significance threshold is the false positive rate for the test**: 
*the probability of finding a significant difference when there really is none*. 
As a business owner, we don’t want to make this kind of mistake, because then we might invest money in a change that doesn’t actually make a difference!

Unfortunately, there’s a trade-off between false positives and false negatives. 
A **false negative** occurs *when there is a difference between version A and B, but the test doesn’t detect it*. 
This is a potential missed opportunity for a business owner!

Most A/B test sample size calculators estimate the sample size needed for a 20% false negative rate; 
while a data scientist needs to choose the false positive rate they are comfortable with. 
The lower the false positive rate, the larger the sample size will need to be!

# [Don't Interfere With Your Tests](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/a-b-test-sample-size-calculator/exercises/dont-interfere-with-your-tests)

Suppose that a Product Manager is running an A/B Test for a redesign of a landing page. 
Before starting the test, she used a sample size calculator to determine the sample size: 2,200 total website visitors. 
After reaching 2,200 visits, she ran a Chi-Square Test. 
The new website design performed slightly better, but the results were not statistically significant.

It might be tempting to run the test for another week to see if the difference becomes significant, but that would be a big mistake! 
By choosing to extend the A/B test past the original sample size, the project manager would introduce personal bias to the results of the test; 
she will be more likely to get the results she wants, regardless if these results reflect reality.

Here are two important rules for making sure that A/B tests remain unbiased:
* Don’t continue to run the test after the predetermined sample size, until “significant” results are found.
* Don’t stop a test before reaching the predetermined sample size, just because your results reach significance early (unless there are ethical reasons that require you to stop, like a prescription drug trial).

Test data is sensitive to changes in sample size, which is why it is important to calculate beforehand.

![]()












