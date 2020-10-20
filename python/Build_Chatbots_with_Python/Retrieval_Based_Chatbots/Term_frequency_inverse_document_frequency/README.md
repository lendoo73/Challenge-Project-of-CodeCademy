# [Term frequency-inverse document frequency](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/language-and-topic-modeling-chatbots/lessons/language-model-tf-idf/exercises/what-is-tfidf)
Term frequency-inverse document frequency is a numerical statistic used to indicate how important a word is to each document in a collection of documents, or a corpus.

When applying tf-idf to a corpus, each word is given a tf-idf score for each document, representing the relevance of that word to the particular document.
A higher tf-idf score indicates a term is more important to the corresponding document.

Tf-idf has many similarities with the bag-of-words language model, which if you recall is concerned with word count — how many times each word appears in a document.

While tf-idf can be used in any situation bag-of-words can be used, there is a key difference in how it is calculated.

Tf-idf relies on two different metrics in order to come up with an overall score:
* ***term frequency***: how often a word appears in a document. This is the same as bag-of-words’ word count.
* ***inverse document frequency***: a measure of how often a word appears in the overall corpus.

Tf-idf can give better insight into how important a word is to a particular document of a corpus.
## [Calculate tf-idf](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/language-and-topic-modeling-chatbots/lessons/language-model-tf-idf/exercises/term-frequency-inverse-document-frequency)
Tf-idf scores are calculated on a term-document basis. there is a tf-idf score for each word, for each document.

The tf-idf score for some term t in a document d in some corpus is calculated as follows:
### *tfidf(t, d) = tf(t, d) ∗ idf(t, corpus)*
* `tf(t,d)` is the term frequency of term `t` in document `d`
* `idf(t,corpus)` is the inverse document frequency of a term `t` across `corpus`
 
```
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(norm=None)

tfidf_vectorizer = vectorizer.fit_transform(corpus)
```
* a `TfidfVectorizer` object is initialized. The `norm=None` keyword argument prevents scikit-learn from modifying the multiplication of term frequency and inverse document frequency
* the `TfidfVectorizer` object is fit and transformed on the corpus of data, returning the tf-idf scores for each term-document pair
