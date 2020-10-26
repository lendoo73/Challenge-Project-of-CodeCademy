#### GENERATING TEXT WITH DEEP LEARNING
# [Build and Train seq2seq](Build and Train seq2seq)
We define the seq2seq model using the Model() function we imported from Keras.

To make it a seq2seq model, we feed it the encoder and decoder inputs, as well as the decoder output:
```
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
```
Our model is ready to train. First, we compile everything. Keras models demand two arguments to compile:
* An optimizer (we’re using RMSprop, which is a fancy version of the widely-used gradient descent) to help minimize our error rate (how bad the model is at guessing the true next word given the previous words in a sentence).
A loss function (we’re using the logarithm-based cross-entropy function) to determine the error rate.
