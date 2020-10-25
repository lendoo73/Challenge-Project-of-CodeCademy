#### GENERATING TEXT WITH DEEP LEARNING
# [The sequence-to-sequence model](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/deep-learning-and-generative-chatbots/modules/deep-learning-for-nlp/lessons/generating-text-with-deep-learning/exercises/intro-to-seq-2-seq)
One of the most common neural models used for text generation is the sequence-to-sequence model, commonly referred to as seq2seq (pronounced “seek-to-seek”). seq2seq uses recurrent neural networks (RNNs) like LSTM in order to generate output, token by token or character by character.

seq2seq networks have two parts:
* An encoder that accepts language (or audio or video) input. The output matrix of the encoder is discarded, but its state is preserved as a vector.
* A decoder that takes the encoder’s final state (or memory) as its initial state. We use a technique called “teacher forcing” to train the decoder to predict the following text (characters or words) in a target sequence given the previous text.
