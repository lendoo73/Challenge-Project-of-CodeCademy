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
We can then ***fit the tf-idf model*** with the `.fit_transform()` method and input a list of string objects. Using the vectorized results of this fitted model, we can compute the ***cosine similarity*** of the user message and a possible response with the aptly named cosine_similarity() function:
```
# fit model
tfidf_vectors = vectorizer.fit_transform(input_list)

# compute cosine similarity 
cosine_sim = cosine_similarity(user_message_vector, response_vector)
```

Most retrieval-based chatbots use multiple measures in order to rank the similarity between a user’s input and a number of possible responses. Oftentimes, different measures produce different similarity rankings.

***The selection of a similarity measure*** is one of the most important decisions chatbot architects have to make while building a system. We should always consider the relative strengths and weaknesses of different metrics.
