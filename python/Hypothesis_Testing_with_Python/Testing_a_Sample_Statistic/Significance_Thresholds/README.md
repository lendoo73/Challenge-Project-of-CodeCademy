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

# [Interpreting a P-Value based on a Significance Threshold](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/significance-thresholds/exercises/interpreting-a-p-value-based-on-a-significance-threshold)

Let’s return to the quiz question example from the previous exercise 
— we want to remove our quiz question from our website if the probability of a correct response is different from 70%. 
Suppose we collected data from 100 learners and ran a binomial hypothesis test with the following null and alternative hypotheses:
* **Null**: The probability that a learner gets the question correct is 70%.
* **Alternative**: The probability that a learner gets the question correct is not 70%.

Assuming that we set a significance threshold of 0.05 for this test:
* If the p-value is less than 0.05, the p-value is significant. 
We will “reject the null hypothesis” and conclude that the probability of a correct answer is significantly different from 70%. 
This would lead us to re-rewrite the question.
* If the p-value is greater than 0.05, the p-value is not significant. 
We will not be able to reject the null hypothesis, and will conclude that the probability of a correct answer is not significantly different from 70%. 
This would lead us to leave the question on the site.

# [Error Types](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/significance-thresholds/exercises/error-types)

Whenever we run a hypothesis test using a significance threshold, we expose ourselves to making two different kinds of mistakes: 
***type I errors (false positives)** and ***type II errors (false negatives)***:

| Null hypothesis: |	is true |	is false
| --- | --- | ---
| P-value significant |	Type I Error |	Correct!
| P-value not significant |	Correct! |	Type II error

Consider the quiz question hypothesis test described in the previous exercises:
* **Null**: The probability that a learner answers a question correctly is 70%.
* **Alternative**: The probability that a learner answers a question correctly is not 70%.

Suppose, for a moment, that the true probability of a learner answering the question correctly is 70% 
(if we showed the question to ALL learners, exactly 70% would answer it correctly). 
This puts us in the first column of the table above (the null hypothesis “is true”). 
If we run a test and calculate a significant p-value, we will make type I error 
(also called a false positive because the p-value is falsely significant), leading us to remove the question when we don’t need to.

On the other hand, if the true probability of getting the question correct is not 70%, the null hypothesis “is false” 
(the right-most column of our table). 
If we run a test and calculate a non-significant p-value, we make a type II error, leading us to leave the question on our site when we should have taken it down.













