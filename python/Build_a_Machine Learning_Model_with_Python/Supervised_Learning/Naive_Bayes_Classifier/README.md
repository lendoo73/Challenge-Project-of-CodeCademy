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

The first part of Bayes’ Theorem that we are going to tackle is `P(positive)`. 
This is the probability that any review is positive. 
To find this, we need to look at all of our reviews in our dataset - both positive and negative - and find the percentage of reviews that are positive.  
`P(Positive) = total_positive / total_reviews`

## [Bayes Theorem II](https://www.codecademy.com/paths/machine-learning/tracks/advanced-supervised-learning-skill-path/modules/naive-bayes-classifier-skill-path/lessons/naive-bayes-classifier/exercises/bayes-theorem-ii)

Let’s continue to try to classify the review “This crib was amazing”.

We now want to compute `P(review | positive)`.

In other words, if we assume that the review is positive, what is the probability that the words “This”, “crib”, “was”, and “amazing” are the only words in the review?

To find this, we have to assume that each word is conditionally independent. 
This means that one word appearing doesn’t affect the probability of another word from showing up. 
This is a pretty big assumption!

##### P(“This crib was amazing" ∣ positive) = P(“This" ∣ positive) * P(“crib" ∣ positive) * P(“was" ∣ positive) * P(“amazing" ∣ positive)

`P("crib"|positive)` is the probability that the word “crib” appears in a positive review.
To find this, we need to count up the total number of times “crib” appeared in our dataset of positive reviews.
If we take that number and divide it by the total number of words in our positive review dataset, we will end up with the probability of “crib” appearing in a positive review.
If we do this for every word in our review and multiply the results together, we have `P(review | positive)`.
```
for word in review_words:
  if word in pos_counter:
    word_in_pos = pos_counter[word]
    pos_probability = pos_probability * word_in_pos / total_pos
```


## [Smoothing](https://www.codecademy.com/paths/machine-learning/tracks/advanced-supervised-learning-skill-path/modules/naive-bayes-classifier-skill-path/lessons/naive-bayes-classifier/exercises/smoothing)

What happens if “crib” was never in any of the positive reviews in our dataset? 
This fraction would then be 0, and since everything is multiplied together, the entire probability `P(review | positive)` would become 0.
If the unclassified review has a typo in it, it is very unlikely that that same exact typo will be in the dataset, and the entire probability will be 0. 
To solve this problem, we will use a technique called ***smoothing***.

In this case, we smooth by adding 1 to the numerator of each probability and `N` to the denominator of each probability. `N` is the number of unique words in our review dataset.
```
pos_probability = 1
neg_probability = 1

review_words = review.split()

for word in review_words:
  word_in_pos = pos_counter[word]
  word_in_neg = neg_counter[word]
  
  pos_probability *= (word_in_pos + 1) / (total_pos + len(pos_counter))
  neg_probability *= (word_in_neg + 1) / (total_neg + len(neg_counter))
```

## [Classify](https://www.codecademy.com/paths/machine-learning/tracks/advanced-supervised-learning-skill-path/modules/naive-bayes-classifier-skill-path/lessons/naive-bayes-classifier/exercises/classify)

We’ve now completed both parts of the numerator. We now need to multiply them together.  
`P(review | positive) * P(positive)`

Let’s now consider the denominator `P(review)`. In our small example, this is the probability that “This”, “crib”, “was”, and “amazing” are the only words in the review. 
Notice that this is extremely similar to `P(review | positive)`. 
The only difference is that we don’t assume that the review is positive.

However, before we start to compute the denominator, let’s think about what our ultimate question is. 
We want to predict whether the review “This crib was amazing” is a positive or negative review. 
In other words, we’re asking whether `P(positive | review)` is greater than `P(negative | review)`. 
If we expand those two probabilities, we end up with the following equations:

![is the review positive](Bayes'_Theorem/images/is_positive_review.jpg)

![is the review negative](Bayes'_Theorem/images/is_negative_review.jpg)

Notice that P(review) is in the denominator of each. 
That value will be the same in both cases! 
Since we’re only interested in comparing these two probabilities, there’s no reason why we need to divide them by the same value. 
We can completely ignore the denominator!

Let’s see if our review was more likely to be positive or negative!
```
percent_pos = 0.5
percent_neg = 0.5

total_pos = sum(pos_counter.values())
total_neg = sum(neg_counter.values())

pos_probability = 1
neg_probability = 1

review_words = review.split()

for word in review_words:
  word_in_pos = pos_counter[word]
  word_in_neg = neg_counter[word]
  
  pos_probability *= (word_in_pos + 1) / (total_pos + len(pos_counter))
  neg_probability *= (word_in_neg + 1) / (total_neg + len(neg_counter))

final_pos = pos_probability * percent_pos 
final_neg = neg_probability * percent_neg

if final_pos > final_neg:
  print("The review is positive")
else:
  print("The review is negative")
```



