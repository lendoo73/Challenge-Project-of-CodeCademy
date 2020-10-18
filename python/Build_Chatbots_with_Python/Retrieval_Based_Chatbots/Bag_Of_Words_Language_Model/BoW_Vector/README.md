#### BAG-OF-WORDS LANGUAGE MODEL
# [BoW Vectors](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/language-and-topic-modeling-chatbots/lessons/language-model-bag-of-words/exercises/bow-vectors-i)
A feature vector is a numeric representation of an item’s important features. Each feature has its own column. If the feature exists for the item, you could represent that with a 1. If the feature does not exist for that item, you could represent that with a 0.

Turning text into a BoW vector is known as ***feature extraction*** or ***vectorization***.

## Features Dictionary
When building BoW vectors, we generally create a ***features dictionary*** of all vocabulary in our training data (usually several documents) mapped to indices.

We need a way of generating a features dictionary from a list of training documents.

`create_features_dictionary()`:  takes one argument: a training document. This will be the list of string. Returns the features dictionary and the list of tokens (words).

Using this dictionary, we can convert new documents into vectors using a vectorization function.
## BoW Vector
n Python, we can use a list to represent a vector. Each index in the list will correspond to a word and be set to its count.

