#### TERM FREQUENCY–INVERSE DOCUMENT FREQUENCY
# [Inverse Document Frequency](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/language-and-topic-modeling-chatbots/lessons/language-model-tf-idf/exercises/inverse-document-frequency)
The inverse document frequency component of the tf-idf score penalizes terms that appear more frequently across a corpus.
The intuition is that words that appear more frequently in the corpus give less insight into the topic or meaning of an individual document, and should thus be deprioritized.

For example, terms like “the” or “go” are used all over the place, so in a bag-of-words model, they would be given priority even though they don’t provide much meaning; 
tf-idf would deprioritize these sorts of common words.

## Calculate inverse document frequency

![Calculate inverse document frequency](https://github.com/lendoo73/Challenge-Project-of-CodeCademy/blob/master/python/Build_Chatbots_with_Python/Retrieval_Based_Chatbots/Term_frequency_inverse_document_frequency/Inverse_document_frequency/calculate_inverse_document_frequency.jpg)

The important take away from the equation is that as the number of documents with the term t increases, the inverse document frequency decreases (due to the nature of the log function). The more frequently a term appears across the corpus, the less important it becomes to an individual document.

```
# a TfidfTransformer object is initialized:
transformer = TfidfTransformer(norm=None)

# the TfidfTransformer is fit (trained) on a term-document matrix of term frequencies:
transformer.fit(term_frequencies)

# the .idf_ attribute of the TfidfTransformer stores the inverse document frequencies of the terms as a NumPy array:
inverse_doc_frequency = transformer.idf_
```
