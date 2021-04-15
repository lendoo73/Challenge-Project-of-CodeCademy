#### SIGNIFICANCE THRESHOLDS

## [Introduction to Significance Thresholds](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/significance-thresholds/exercises/introduction-to-significance-thresholds)

Sometimes, when we run a hypothesis test, we simply report a p-value or a confidence interval and give an interpretation 
(eg., the p-value was 0.05, which means that there is a 5% chance of observing two or fewer heads in 10 coin flips).

In other situations, we want to use our p-value to make a decision or answer a yes/no question. 
For example, suppose that we’re developing a new quiz question at Codecademy and want learners to have a 70% chance of getting the question right 
(higher would mean the question is too easy, lower would mean the question is too hard). 
We show our quiz question to a sample of 100 learners and 60 of them get it right. 
Is this significantly different from our target of 70%? 
If so, we want to remove the question and try to rewrite it.

In order to turn a p-value, which is a probability, into a yes or no answer, data scientists often use a pre-set significance threshold. 
The **significance threshold** can be any *number between 0 and 1*, but a common choice is 0.05. **P-values** that are **less than this threshold are considered “significant”**, while **larger p-values are considered “not significant”**.
