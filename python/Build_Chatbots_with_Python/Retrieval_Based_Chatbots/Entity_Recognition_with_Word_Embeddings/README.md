#### RETRIEVAL-BASED CHATBOTS
# [Entity Recognition with Word Embeddings](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/retrieval-based-chatbots/lessons/retrieval-based-chatbots/exercises/chatbots-entity-with-embeddings)
While POS tagging allows us to extract key entities in a user message, it does not provide context that allows a chatbot to believably integrate an entity reference into a predefined response.

A retrieval-based chatbot is a collection of predefined responses. Each response is a complete sentence, but with many key words replaced with blank spots. These blanks is labeled with a reference to a broad kind of entity. 

A predefined response for a weather report chatbot might look like:
`"Good Morning! Yous should see sunny skies this {weekday} around the greater Chicago area, including in {neighborhood-chicago}"`
