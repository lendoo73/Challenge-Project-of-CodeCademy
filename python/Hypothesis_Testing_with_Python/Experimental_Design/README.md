# [How to Choose a Hypothesis Test](https://www.codecademy.com/courses/hypothesis-testing-python/articles/how-to-choose-a-hypothesis-test)

Learn how to choose an appropriate hypothesis test for your data and questions.

## Introduction

In this module we’ll cover some of the key considerations for designing an experiment. 
One of the first things to consider is which statistical test is appropriate for the question you are trying to answer. 
Sometimes this will depend on the data you have available, and sometimes you will have the opportunity to decide this before starting to collect data.

There are many different types of hypothesis tests that should be used in different situations. 
In this article, we are going to briefly review some of them and when they are appropriate.

Here is a summary table of some of the hypothesis tests we’ll cover:

![table of hypothesi tests](article_graphic.webp)

## Comparing a sample statistic to a hypothesized population value

In some situations, we may want to compare a sample statistic to a hypothesized population value. 
In this scenario, we have a sample of data from some population and have calculated a sample statistic (eg., a sample mean, frequency, or proportion). 
Based on this observed sample statistic, we then want to know whether the sample was likely to be drawn from a population with some hypothesized or target value of that same statistic.

For example, suppose we hypothesize that 5% of all people who access a website will buy a product. 
In order to understand if this is the case, we might find a sample of people who accessed that website and calculate that 4.3% of our sample bought a product. 
Finally, we can use a hypothesis test to determine the likelihood that, if we could observe ALL people who ever access the website, 5% of them will buy a product (even though only 4.3% of our sample did).

If we have a sample of **quantitative data**, such as *height*, *weight*, or *amount spent*, we should use a **one-sample t-test**. 
If we have a sample of **binary data**, such as *whether or not someone made a purchase* or *clicked a link*, we should use a **binomial test**.

### Example: one sample t-test

Suppose we want to compare exam scores for students who attended a test prep program to the global average score of 35 points. 
Do students who attend this program score higher than 35 points? 
The global average is the hypothesized population value and the average of the exam scores of students who attended the program is the sample statistic 
(in this case, sample mean).

Below is the code to run a one-sample t-test to address the above question. 
In this example the **alternative hypothesis** is that *the sample mean is significantly different than 35*, and the **null hypothesis** is that *the sample mean is 35*.
```pythom
from scipy.stats import ttest_1samp
 
global_average_score = 35
sample_scores = [12, 42, 37, 18, 23, 39, 45, … , 52]
 
t_stat, p_value = ttest_1samp(sample_scores, global_average_score)
```

### Example: binomial test

If we instead have a sample of **binary data** and want to compare a sample proportion/frequency to an underlying probability (population value), a binomial test is appropriate. 
The classic example of a binomial test is tossing a coin to determine if it’s fair (fair means that the probability of either heads or tails is exactly 50%).

For example, suppose that you collect sample data from a coin by tossing it 100 times, and find that 45 flips result in heads. 
Based on this sample, what is the probability that the coin is actually fair (if you flipped it infinitely many times, exactly half those flips would be heads)? 
The following code runs the binomial test to answer this question:
```python
from scipy.stats import binom_test
 
p_value = binom_test(45, 100, p = 0.50)
```
The **alternative hypothesis** for this test is that the *probability is different than p = 0.50*, and the **null** is that it is *equal to 0.50*.

Here are some other examples of situations where a binomial test would be useful
* Is the number of passengers who show up for a flight fewer than normal?
* Is the open rate on a marketing email different from the company target?











