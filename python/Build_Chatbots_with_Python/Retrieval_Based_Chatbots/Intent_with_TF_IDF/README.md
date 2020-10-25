#### RETRIEVAL-BASED CHATBOTS
# [Intent with TF-IDF](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/retrieval-based-chatbots/lessons/retrieval-based-chatbots/exercises/chatbots-intent-tfidf)
While the number of shared words is an intuitive way to think about the *similarity between two documents*, a number of other methods are also commonly used to determine the *best match between the user input and a pre-defined response*.

The **term frequency–inverse document frequency (tf-idf)** puts emphasis on the relative frequency in which a term occurs within a possible response and the user message. 

[Tf-idf](https://github.com/lendoo73/Challenge-Project-of-CodeCademy/tree/master/python/Build_Chatbots_with_Python/Retrieval_Based_Chatbots/Term_frequency_inverse_document_frequency) is best suited for domains where the most important terms in an input or response are mentioned repeatedly.

In Python, the sklearn package has a handy TfidfVectorizer() object:
```
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
```
