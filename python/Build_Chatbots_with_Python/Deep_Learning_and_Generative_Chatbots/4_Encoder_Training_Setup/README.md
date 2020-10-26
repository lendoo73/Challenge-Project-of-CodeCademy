#### GENERATING TEXT WITH DEEP LEARNING
# [Encoder Training Setup](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/deep-learning-and-generative-chatbots/modules/deep-learning-for-nlp/lessons/generating-text-with-deep-learning/exercises/encoder-training-setup)
Deep learning models in Keras are built in layers, where each layer is a step in the model.

Our encoder requires two layer types from Keras:
* An input layer, which defines a matrix to hold all the one-hot vectors that we’ll feed to the model.
* An LSTM layer, with some output dimensionality.

We can import these layers as well as the model we need:
```
from keras.layers import Input, LSTM
from keras.models import Model
```
Next, we set up the input layer, which requires some number of dimensions that we’re providing.
```
# the shape specifies the input matrix sizes
encoder_inputs = Input(shape=(None, num_encoder_tokens))

encoder_lstm = LSTM(100, return_state=True)
# we're using a dimensionality of 100
# so any LSTM output matrix will have shape [batch_size, 100]
```
The only thing we want from the encoder is its final states.
```
encoder_outputs, state_hidden, state_cell = encoder_lstm(encoder_inputs)
```
`encoder_outputs` isn’t really important for us, so we can just discard it. However, the states, we’ll save in a list:
```
encoder_states = [state_hidden, state_cell]
```
