#### RETRIEVAL-BASED CHATBOTS
# [Intent with Bag-of-Words](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/retrieval-based-chatbots/lessons/retrieval-based-chatbots/exercises/chatbots-intent-with-bag-of-words)
One way we can begin parsing a user’s message to a retrieval-based chatbot is to consider a user’s intent word by word.
Bag-of-Words (BoW) is one of the most common models used to understand human language at the individual word level.
BoW results in a mapping of a word to its frequency in a text.

## Build word-to-frequency mapping:
```
from collections import Counter

word_counts = Counter(preprocess("Wheels on the bus go round and round, round and round, round and round."))

print(word_counts)
#Counter({'round': 6, 'wheels': 1, 'bus': 1, 'go': 1})
```
We can use the results of this mapping to construct a measure of the intent of a user’s message.
Then we’ll use this measure to retrieve the most similar answer from our collection of **predefined chatbot responses**.
