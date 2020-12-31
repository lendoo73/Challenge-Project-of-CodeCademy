# [The Naive Bayes Classifier](https://www.codecademy.com/paths/machine-learning/tracks/advanced-supervised-learning-skill-path/modules/naive-bayes-classifier-skill-path/lessons/naive-bayes-classifier/exercises/naive-bayes)

A Naive Bayes classifier is a supervised machine learning algorithm that leverages Bayes’ Theorem to make predictions and classifications. 
Recall Bayes’ Theorem:

![event A will happen, event B already happend](Bayes'_Theorem/images/a_will_happen_b_happend.jpg)

This equation is finding the probability of `A` given `B`. 
This can be turned into a classifier if we replace `B` with a data point and `A` with a class. 
For example, let’s say we’re trying to classify an `email` as either `spam` or `not spam`. 
We could calculate `P(spam | email)` and `P(not spam | email)`. 
Whichever probability is higher will be the classifier’s prediction. 
Naive Bayes classifiers are often used for text classification.

So why is this a supervised machine learning algorithm? 
In order to compute the probabilities used in Bayes’ theorem, we need previous data points. 
For example, in the spam example, we’ll need to compute `P(spam)`. 
This can be found by looking at a tagged dataset of emails and finding the ratio of spam to non-spam emails.

## [Investigate the Data](https://www.codecademy.com/paths/machine-learning/tracks/advanced-supervised-learning-skill-path/modules/naive-bayes-classifier-skill-path/lessons/naive-bayes-classifier/exercises/intro)

We are going to create a Naive Bayes classifier that can predict whether a review for a product is positive or negative. 
This type of classifier could be extremely helpful for a company that is curious about the public reaction to a new product. 
Rather than reading thousands of reviews or tweets about the product, you could feed those documents into the Naive Bayes classifier and instantly find out how many are positive and how many are negative.

The dataset we will be using for this lesson contains Amazon product reviews for baby products. 
The original dataset contained many different features including the reviewer’s name, the date the review was made, and the overall score. 
We’ve removed many of those features; the only features that we’re interested in are the text of the review and whether the review was “positive” or “negative”. 
We labeled all reviews with a score less than 4 as a negative review.

## [Bayes Theorem I](https://www.codecademy.com/paths/machine-learning/tracks/advanced-supervised-learning-skill-path/modules/naive-bayes-classifier-skill-path/lessons/naive-bayes-classifier/exercises/bayes-theorem-i)

We’re going to write a classifier that can predict whether the review “This crib was amazing” is a positive or negative review. 
We want to compute both `P(positive | review)` and `P(negative | review)` and find which probability is larger. 
To do this, we’ll be using Bayes’ Theorem. 
Let’s look at Bayes’ Theorem for `P(positive | review)`.

![is the review positive](Bayes'_Theorem/images/is_positive_review.jpg)








