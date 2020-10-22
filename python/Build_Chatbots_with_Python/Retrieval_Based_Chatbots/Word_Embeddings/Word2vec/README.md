#### WORD EMBEDDINGS
# [Word2vec](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/nlp-word-embeddings/lessons/word-embeddings/exercises/word-2-vec)

Word2vec is a statistical learning algorithm that develops word embeddings from a corpus of text.

Word2vec uses one of ***two different model*** architectures to come up with the values that define a collection of word embeddings.

## Continuous bag-of-words (CBOW)
The word2vec model goes through each word in the training corpus, in order, and tries to predict what word comes at each position based on applying bag-of-words to the words that surround the word in question. 
The order of the words does not matter!

## Continuous skip-grams
Skip-grams function similarly to n-grams, except instead of looking at groupings of n-consecutive words in a text, we can look at sequences of words that are separated by some specified distance between them.
