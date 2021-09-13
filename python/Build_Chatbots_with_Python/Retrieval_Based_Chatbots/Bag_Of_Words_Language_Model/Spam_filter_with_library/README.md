#### BAG-OF-WORDS LANGUAGE MODEL
## [BoW Dictionaries](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/language-and-topic-modeling-chatbots/lessons/language-model-bag-of-words/exercises/bow-dictionaries)
For `text_to_bow()`, you can approximate the functionality with the `collections` module’s `Counter()` function:
```py
from collections import Counter

tokens = ['another', 'five', 'fish', 'find', 'another', 'faraway', 'fish']
print(Counter(tokens))

# Counter({'fish': 2, 'another': 2, 'find': 1, 'five': 1, 'faraway': 1})
```
## [BoW Vectors](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/language-and-topic-modeling-chatbots/lessons/language-model-bag-of-words/exercises/bow-vectors-i)
For vectorization, you can use CountVectorizer from the machine learning library scikit-learn. You can use fit() to train the features dictionary and then transform() to transform text into a vector:
```py
from sklearn.feature_extraction.text import CountVectorizer

training_documents = ["Five fantastic fish flew off to find faraway functions.", "Maybe find another five fantastic fish?", "Find my fish with a function please!"]
test_text = ["Another five fish find another faraway fish."]
bow_vectorizer = CountVectorizer()
bow_vectorizer.fit(training_documents)
bow_vector = bow_vectorizer.transform(test_text)
print(bow_vector.toarray())
# [[2 0 1 1 2 1 0 0 0 0 0 0 0 0 0]]
```
