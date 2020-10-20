#### TERM FREQUENCY–INVERSE DOCUMENT FREQUENCY
# [Converting Bag-of-Words to Tf-idf](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/language-and-topic-modeling-chatbots/lessons/language-model-tf-idf/exercises/bag-of-words-to-tfidf)
You can also convert a bag-of-words model you have already created into tf-idf scores.

You begin by initializing a TfidfTransformer object:
```
from sklearn.feature_extraction.text import TfidfTransformer

tf_idf_transformer = TfidfTransformer(norm = False)
```
You can now multiply the term frequencies by their inverse document frequency to get the tf-idf scores:
```
tf_idf_scores = tfidf_transformer.fit_transform(count_matrix)
```
