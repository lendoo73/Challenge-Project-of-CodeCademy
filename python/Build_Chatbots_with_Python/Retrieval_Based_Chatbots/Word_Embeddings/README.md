# [Word Embedding](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/nlp-word-embeddings/lessons/word-embeddings/exercises/what-is-a-word-embedding)
Word embeddings are **vector representations of a word**.

They allow us to take all the information that is stored in a word, like its meaning and its part of speech, and convert it into a numeric form that is more understandable to a computer.

We can load a basic English word embedding model using spaCy:
```
import spacy

nlp = spacy.load('en')
```
To get the vector representation of a word, we call the model with the desired word as an argument and can use the .vector attribute.
```
nlp('love').vector
```

Here “love” is represented by a 96-dimension vector. Each dimension of the vector is capturing some information about how the word “love” is used.

By converting the words into their numeric vector representations, we are able to have a computer more easily compare the vectors and understand their similarities and differences.
