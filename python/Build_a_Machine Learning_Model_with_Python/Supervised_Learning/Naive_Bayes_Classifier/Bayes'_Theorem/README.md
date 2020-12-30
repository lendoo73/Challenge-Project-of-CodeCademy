# Bayes' Theorem

## [Introduction to Bayes' Theorem](https://www.codecademy.com/paths/machine-learning/tracks/advanced-supervised-learning-skill-path/modules/naive-bayes-classifier-skill-path/lessons/bayes-theorem/exercises/intro)

Bayes’ Theorem is the basis of a branch of statistics called Bayesian Statistics, where we take prior knowledge into account before calculating new probabilities.

This allows us to find narrow solutions from a huge universe of possibilities.
British mathematician Alan Turing used it to crack the German Enigma code during WWII.
And now it is used in:
* Machine Learning
* Statistical Modeling
* A/B Testing
* Robotics

## [Independent Events](https://www.codecademy.com/paths/machine-learning/tracks/advanced-supervised-learning-skill-path/modules/naive-bayes-classifier-skill-path/lessons/bayes-theorem/exercises/independence)

The ability to determine whether two events are **independent** is an important skill for statistics.

If two events are independent, then the occurrence of one event does not affect the probability of the other event.
Here are some examples of independent events:
* I wear a blue shirt; my coworker wears a blue shirt
* I take the subway to work; I eat sushi for lunch
* The NY Giants win their football game; the NY Rangers win their hockey game

If two events are **dependent**, then when one event occurs, the probability of the other event occurring changes in a predictable way.
Here are some examples of dependent events:
* It rains on Tuesday; I carry an umbrella on Tuesday
* I eat spaghetti; I have a red stain on my shirt
* I wear sunglasses; I go to the beach

## [Conditional Probability](https://www.codecademy.com/paths/machine-learning/tracks/advanced-supervised-learning-skill-path/modules/naive-bayes-classifier-skill-path/lessons/bayes-theorem/exercises/conditional-probability)

***Conditional probability*** is the probability that two events happen. 
It’s easiest to calculate conditional probability when the two events are independent.

For the rest of this lesson, we’ll be using the statistical convention that the probability of an event is written as `P(event)`.

If the probability of event `A` is `P(A)` and the probability of event `B` is `P(B)` and the two events are independent, then the probability of both events occurring is the product of the probabilities:

![probability of independent event A - B](images/independent_probability_A_B.jpg)

The symbol ∩ just means “and”, so `P(A ∩ B)` means the probability that both `A` and `B` happen.





