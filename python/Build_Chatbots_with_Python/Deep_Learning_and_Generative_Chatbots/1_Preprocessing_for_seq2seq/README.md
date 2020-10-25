#### GENERATING TEXT WITH DEEP LEARNING
# [Preprocessing for seq2seq](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/deep-learning-and-generative-chatbots/modules/deep-learning-for-nlp/lessons/generating-text-with-deep-learning/exercises/preprocessing-for-seq-2-seq)

We can import Keras from Tensorflow:
```
from tensorflow import keras
```
The code we’ll be using is mostly derived from [Keras’s own tutorial on the seq2seq model](https://blog.keras.io/a-ten-minute-introduction-to-sequence-to-sequence-learning-in-keras.html).

We’ll need the following for our Keras implementation:
* vocabulary sets for both our input (English) and target (Spanish) data
* the total number of unique word tokens we have for each set
* the maximum sentence length we’re using for each language

We also need to mark the start and end of each document (sentence) in the target samples so that the model recognizes where to begin and end its text generation.

One way to do this is adding "<START>" at the beginning and "<END>" at the end of each target document (in our case, this will be our Spanish sentences). For example, "Estoy feliz." becomes "<START> Estoy feliz. <END>".
