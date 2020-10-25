#### RETRIEVAL-BASED CHATBOTS
# [Entity Recognition with Word Embeddings](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/retrieval-based-chatbots/lessons/retrieval-based-chatbots/exercises/chatbots-entity-with-embeddings)
While POS tagging allows us to extract key entities in a user message, it does not provide context that allows a chatbot to believably integrate an entity reference into a predefined response.

A retrieval-based chatbot is a collection of predefined responses. Each response is a complete sentence, but with many key words replaced with blank spots. These blanks is labeled with a reference to a broad kind of entity. 

A predefined response for a weather report chatbot might look like:
```
"Good Morning! Yous should see sunny skies this {weekday} around the greater Chicago area, including in {neighborhood-chicago}"
```
In order to produce a coherent response, the chatbot must ***insert entities from a user message*** into these blank spots.
Chatbot architects often use [word embedding models](https://github.com/lendoo73/Challenge-Project-of-CodeCademy/tree/master/python/Build_Chatbots_with_Python/Retrieval_Based_Chatbots/Word_Embeddings), like word2vec, to rank the similarity of user-provided entities and the broad category associated with a response “blank spot”. The spacy package provides a pre-trained word2vec model which can be called on a string of entities and the responses category:
```
import spacy

# load word2vec model
word2vec = spacy.load('en')

# call model on data
tokens = word2vec("wednesday, dog, boots, flower")
response_category = word2vec("weekday")
```
After the model has been applied, we can use spacy’s `.similarity()` method to compute the *cosine similarity between user-provided entities and a response category*:
```
output_list = list()
for token in tokens:
    output_list.append(f"{token.text} {response_category.text} {token.similarity(response_category)}")

# output:
# wednesday weekday 0.453354920245737
# dog weekday 0.21911001129423147
# boots weekday 0.15690609198936833
# flower weekday 0.17118961389940174
```
The resulting output above shows that the word2vec model found “wednesday” to have the greatest similarity to “weekday. A chatbot system can select the token with the highest similarity score and insert it into the “blank spot” in a predefined response in order to continue a coherent conversation with a user.
