#### WORD EMBEDDINGS
# [Gensim](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/nlp-word-embeddings/lessons/word-embeddings/exercises/gensim)

Depending on the corpus of text we select to train a word embedding model, different word embeddings will be created according to the context of the words in the given corpus. 

When we want to train our own word2vec model on a corpus of text, we can use the [gensim package](https://radimrehurek.com/gensim/)!

With gensim we are able to build our own word embeddings on any corpus of text we like.

To easily train a word2vec model on our own corpus of text, we can use gensim’s `Word2Vec()` function.
```
model = gensim.models.Word2Vec(
  corpus, 
  size = 100, 
  window = 5, 
  min_count = 1, 
  workers = 2, 
  sg = 1
)
```
* `corpus`:  a list of lists, where each inner list is a document in the corpus and each element in the inner lists is a word token
* `size`: determines how many dimensions our word embeddings will include. Word embeddings often have upwards of 1,000 dimensions!

To view the entire vocabulary used to train the word embedding model, we can use the `.wv.vocab.items()` method.
```
vocabulary_of_model = list(model.wv.vocab.items())
```

When we train a word2vec model on a smaller corpus of text, we pick up on the unique ways in which words of the text are used.

For example, if we were using scripts from the television show Friends as a training corpus, the model would pick up on the unique ways in which words are used in the show. While the generalized vectors in a spaCy model might not place the vectors for “Ross” and “Rachel” close together, a gensim word embedding model trained on Friends’ scrips would place the vectors for words like “Ross” and “Rachel”, two characters that have a continuous on and off-again relationship throughout the show, very close together!

To easily find which vectors gensim placed close together in its word embedding model, we can use the `.most_similar()` method.
```
model.most_similar("my_word_here", topn = 100)
```
* `"my_word_here"`: the target word token we want to find most similar words to
* `topn`: a keyword argument that indicates how many similar word vectors we want returned

The `.doesnt_match()` method:
```
model.doesnt_match(["asia", "mars", "pluto"])
```
When given a list of terms in the vocabulary as an argument, .doesnt_match() returns which term is furthest from the others.
