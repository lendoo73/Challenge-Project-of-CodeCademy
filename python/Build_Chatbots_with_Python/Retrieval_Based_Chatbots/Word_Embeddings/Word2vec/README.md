#### WORD EMBEDDINGS
# [Word2vec](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/nlp-word-embeddings/lessons/word-embeddings/exercises/word-2-vec)

Word2vec is a statistical learning algorithm that develops word embeddings from a corpus of text.

Word2vec uses one of ***two different model*** architectures to come up with the values that define a collection of word embeddings.

## Continuous bag-of-words (CBOW)
The word2vec model goes through each word in the training corpus, in order, and tries to predict what word comes at each position based on applying bag-of-words to the words that surround the word in question. 
The order of the words does not matter!

## Continuous skip-grams
Skip-grams function similarly to n-grams, except instead of looking at groupings of n-consecutive words in a text, we can look at sequences of words that are separated by some specified distance between them.

When using continuous skip-grams, the order of context is taken into consideration! Because of this, the time it takes to train the word embeddings is slower than when using continuous bag-of-words. The results, however, are often much better!

<hr />
With either the continuous bag-of-words or continuous skip-grams representations as training data, word2vec then uses a shallow, 2-layer neural network to come up with the values that place words with a similar context in vectors near each other and words with different contexts in vectors far apart from each other.
