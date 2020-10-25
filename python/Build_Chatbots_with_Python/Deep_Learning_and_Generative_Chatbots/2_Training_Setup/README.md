#### GENERATING TEXT WITH DEEP LEARNING
# [Training Setup (part 1)](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/deep-learning-and-generative-chatbots/modules/deep-learning-for-nlp/lessons/generating-text-with-deep-learning/exercises/training-setup-part-1)
For each sentence, Keras expects a NumPy matrix containing one-hot vectors for each token.

## one-hot vector
In a one-hot vector, every token in our set is represented by a 0 except for the current token which is represented by a 1.

For example given the vocabulary `["the", "dog", "licked", "me"]`, a one-hot vector for “dog” would look like `[0, 1, 0, 0]`.

In order to vectorize our data and later translate it from vectors, it’s helpful to have a features dictionary (and a reverse features dictionary) to easily translate between all the 1s and 0s and actual words. We’ll build out the following:
* a features dictionary for English
* a features dictionary for Spanish
* a reverse features dictionary for English (where the keys and values are swapped)
* a reverse features dictionary for Spanish

Once we have all of our features dictionaries set up, it’s time to vectorize the data! We’re going to need vectors to input into our encoder and decoder, as well as a vector of target data we can use to train the decoder.

Because each matrix is almost all zeros, we’ll use numpy.zeros() from the NumPy library to build them out.
```
import numpy as np

encoder_input_data = np.zeros(
    (
      # the shape of the matrix
      len(input_docs),          # the number of documents (sentences)
      max_encoder_seq_length,   # the maximum token sequence length (the longest sentence we want to see) 
      num_encoder_tokens        # the number of unique tokens (or words)
    ),
    dtype = 'float32'           # the data type we want
)
```
