#### GENERATING TEXT WITH DEEP LEARNING
# [Decoder Training Setup](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/deep-learning-and-generative-chatbots/modules/deep-learning-for-nlp/lessons/generating-text-with-deep-learning/exercises/decoder-training-setup)
The decoder looks a lot like the encoder, with an input layer and an LSTM layer that we use together:
```
decoder_inputs = Input(shape=(None, num_decoder_tokens))
decoder_lstm = LSTM(100, return_sequences=True, return_state=True)
# This time we care about full return sequences
```
However, with our decoder, we pass in the state data from the encoder, along with the decoder inputs. This time, we’ll keep the output instead of the states:
```
# The two states will be discarded for now
decoder_outputs, decoder_state_hidden, decoder_state_cell = decoder_lstm(decoder_inputs, initial_state=encoder_states)
```
We also need to run the output through a final activation layer, using the Softmax function, that will give us the probability distribution — where all probabilities sum to one — for each token. The final layer also transforms our LSTM output from a dimensionality of whatever we gave it (in our case, 10) to the number of unique words within the hidden layer’s vocabulary (i.e., the number of unique target tokens, which is definitely more than 10!).
```
decoder_dense = Dense(num_decoder_tokens, activation='softmax')

decoder_outputs = decoder_dense(decoder_outputs)
```
Keras’s implementation could work with several layer types, but Dense is the least complex, so we’ll go with that. We also need to modify our import statement to include it before running the code:
```
from keras.layers import Input, LSTM, Dense
```
