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

For instance, suppose we are rolling a pair of dice, and want to know the probability of rolling two sixes.
Each die has six sides, so the probability of rolling a six is 1/6.
Each die is independent: rolling one six does not increase or decrease our chance of rolling a second six. 

![probability of pair of dice](images/probability_pair_of_dice.jpg)

## [Testing for a Rare Disease](https://www.codecademy.com/paths/machine-learning/tracks/advanced-supervised-learning-skill-path/modules/naive-bayes-classifier-skill-path/lessons/bayes-theorem/exercises/bayes-theorem-i)

Suppose you are a doctor and you need to test if a patient has a certain rare disease.
The test is very accurate: it’s correct 99% of the time. The disease is very rare: only 1 in 100,000 patients have it.

You administer the test and it comes back positive, so your patient must have the disease, right?

Not necessarily. 
If we just consider the test, there is only a 1% chance that it is wrong, but we actually have more information: we know how rare the disease is.

Given that the test came back positive, there are two possibilities:
1. The patient had the disease, and the test correctly diagnosed the disease.
2. The patient didn’t have the disease and the test incorrectly diagnosed that they had the disease.

## [Bayes' Theorem](https://www.codecademy.com/paths/machine-learning/tracks/advanced-supervised-learning-skill-path/modules/naive-bayes-classifier-skill-path/lessons/bayes-theorem/exercises/bayes-theorem-ii)

In the previous exercise, we determined two probabilities:
1. The patient had the disease, and the test correctly diagnosed the disease ≈ 0.00001
2. The patient didn’t have the disease and the test incorrectly diagnosed that they had the disease ≈ 0.01

Both events are rare, but we can see that it was about 1,000 times more likely that the test was incorrect than that the patient had this rare disease.

We’re able to come to this conclusion because we had more information than just the accuracy of the test; we also knew the prevalence of this disease. 
That extra information about how we expect the world to work is called a **prior**.

When we only use the first piece of information (the result of the test), it’s called a **Frequentist Approach** to statistics. 
When we incorporate our prior, it’s called a **Bayesian Approach**.

In statistics, if we have two events (`A` and `B`), we write the probability that event `A` will happen, given that event `B` already happened as `P(A|B)`. 
In our example, we want to find `P(rare disease | positive result)`. 
In other words, we want to find the probability that the patient has the disease given the test came back positive.

We can calculate `P(A|B)` using **Bayes’ Theorem**:

![event A will happen, event B already happend](images/a_will_happen_b_happend.jpg)

So in this case, we’d say: (rare disease will happen | positive test happend])

![rare disease will happen positive test happend](images/rare_disease_will_happen_positive_test_happend.jpg)

## [Spam Filters](https://www.codecademy.com/paths/machine-learning/tracks/advanced-supervised-learning-skill-path/modules/naive-bayes-classifier-skill-path/lessons/bayes-theorem/exercises/bayes-theorem-iii)

Email spam filters use Bayes’ Theorem to determine if certain words indicate that an email is [spam](https://en.wikipedia.org/wiki/Email_spam).

Let’s a take word that often appears in spam: “enhancement”.

With just 3 facts, we can make some preliminary steps towards a good spam filter:
1. “enhancement” appears in just 0.1% of non-spam emails
2. “enhancement” appears in 5% of spam emails
3. Spam emails make up about 20% of total emails

Given that an email contains “enhancement”, what is the probability that the email is spam?

In this example, we are dealing with two probabilities:
* `P(enhancement)` - the probability that the word “enhancement” appears in an email.
* `P(spam)` - the probability that an email is spam.

Using Bayes’ Theorem to answer our question means that we want to calculate `P(A|B)`.

But what are `A` and `B` referring to in this case?
(spam will happen | "enhancement" already happend)
`A`: spam
`B`: "enhancement" appears in the email

What is `P(spam)`? `P(spam) = 0.2`

What is `P(enhancement | spam)`? `P(enhancement | spam) = 0.05`

We want to know the overall probability that any email (spam or non-spam) contains “enhancement”.

Because we know the probability of “enhancement” occurring in both spam (`0.05`) and non-spam (`0.001`) emails, we can use a weighted average to calculate the probability of “enhancement” occurring in an email:

![probability of email contain enhancement](images/email_contain_enhancement.jpg)


