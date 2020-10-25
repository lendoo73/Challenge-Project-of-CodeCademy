#### RETRIEVAL-BASED CHATBOTS
# [Entity Recognition with POS Tagging](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/retrieval-based-chatbots/lessons/retrieval-based-chatbots/exercises/chatbots-entity-with-pos)
After determining the best method for the classification of a user’s intent, chatbot architects set upon the task of recognizing entities within a user’s message.
There are a number of methods that can be used to locate and interpret the entities found in a user message — it is up to the system architect (you!) to critically evaluate methods and select those that are best-fit for a chatbot’s specific domain.

[**Part of speech (POS)** tagging](https://github.com/lendoo73/Challenge-Project-of-CodeCademy/tree/master/python/Build_Chatbots_with_Python/Rule-Based_Chatbots/Language_Parsing) is commonly used to identify entities within a user message, as most entities are nouns.

Automate the part-of-speech tagging process with nltk‘s pos_tag() function:
`pos_tag()` function can rapidly tag a *tokenized sentence* and return a *list of tuple* objects for use in entity recognition tasks.

We can extract words tagged as a noun, represented in nltk‘s [tagging schema](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html) as a collection of tags beginning with “NN,” by checking if the string “NN” occurs in the token tag, and then appending the token string to a list of nouns if True:
```
message_nouns = list()

for token in tagged_message:
  if "NN" in token[1]:
     message_nouns.append(token[0])
```
Once we have a list of the entities in a user message, we’re well on our way to developing a realistic chatbot response!
