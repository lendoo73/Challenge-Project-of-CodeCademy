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

# [Setting the Type I Error Rate](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/significance-thresholds/exercises/setting-the-type-i-error-rate)

It turns out that, when we run a hypothesis test with a significance threshold, the significance threshold is equal to the type I error (false positive) rate for the test. 
To see this, we can use a simulation.

Recall our quiz question example: the null hypothesis is that the probability of getting a quiz question correct is equal to 70%. 
We’ll make a type I error if the null hypothesis is correct (the true probability of a correct answer is 70%), but we get a significant p-value anyways.

Now, consider the following simulation code:
```python
false_positives = 0
sig_threshold = 0.05
 
for i in range(1000):
    sim_sample = np.random.choice(
        ['correct', 'incorrect'], 
        size = 100, 
        p = [0.7, 0.3]
    )
    num_correct = np.sum(sim_sample == 'correct')
    p_val = binom_test(num_correct, 100, 0.7)
    if p_val < sig_threshold:
        false_positives += 1
 
print(false_positives/1000) #Output: 0.0512
```
This code does the following:
* Set the significance threshold equal to 0.05 and a counter for false positives equal to zero.
* Repeat these steps 1000 times:
    * Simulate 100 learners, where each learner has a 70% chance of answering a quiz question correctly.
    * Calculate the number of simulated learners who answered the question correctly. 
    Note that, because each learner has a 70% chance of answering correctly, this number will likely be around 70, but will vary every time by random chance.
    * Run a binomial test for the simulated sample where the null hypothesis is that the probability of a correct answer is 70% (0.7). 
    Note that, every time we run this test, the null hypothesis is true because we simulated our data so that the probability of a correct answer is 70%.
    * Add `1` to our false positives counter every time we make a type I error (the p-value is significant).
* Print the proportion of our 1000 tests (on simulated samples) that resulted in a false positive.

Note that the proportion of false positive tests is very similar to the value of the significance threshold (0.05).











