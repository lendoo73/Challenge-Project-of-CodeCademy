#### RETRIEVAL-BASED CHATBOTS
# [Entity Recognition with Word Embeddings](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/retrieval-based-chatbots/lessons/retrieval-based-chatbots/exercises/chatbots-entity-with-embeddings)
While POS tagging allows us to extract key entities in a user message, it does not provide context that allows a chatbot to believably integrate an entity reference into a predefined response.

A retrieval-based chatbot is a collection of predefined responses. Each response is a complete sentence, but with many key words replaced with blank spots. These blanks is labeled with a reference to a broad kind of entity. 

A predefined response for a weather report chatbot might look like:
```
"Good Morning! Yous should see sunny skies this {weekday} around the greater Chicago area, including in {neighborhood-chicago}"
```
In order to produce a coherent response, the chatbot must ***insert entities from a user message*** into these blank spots.
Chatbot architects often use [word embedding models](https://github.com/lendoo73/Challenge-Project-of-CodeCademy/tree/master/python/Build_Chatbots_with_Python/Retrieval_Based_Chatbots/Word_Embeddings), like word2vec, to rank the similarity of user-provided entities and the broad category associated with a response “blank spot”.
