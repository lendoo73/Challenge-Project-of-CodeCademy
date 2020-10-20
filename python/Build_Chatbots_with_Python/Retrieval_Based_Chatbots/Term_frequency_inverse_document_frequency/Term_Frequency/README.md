#### TERM FREQUENCY–INVERSE DOCUMENT FREQUENCY
# [Term Frequency](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/language-and-topic-modeling-chatbots/lessons/language-model-tf-idf/exercises/term-frequency)
The first component of tf-idf is term frequency, or how often a word appears in a document within the corpus.

The value for the term frequency is the same as if applying the bag-of-words language model to a document.

The intuition for including term frequency in the tf-idf calculation is that the ***more frequently a word*** appears in a single document, the ***more important*** that ***term*** is to the document.

## Calculate term frequency
```
from sklearn.feature_extraction.text import CountVectorizer

# A CountVectorizer object is initialized:
vectorizer = CountVectorizer()

# The CountVectorizer object is fit (trained) and transformed (applied) on the corpus of data, returning the term frequencies for each term-document pair
term_frequencies = vectorizer.fit_transform(corpus_of_data)
```
