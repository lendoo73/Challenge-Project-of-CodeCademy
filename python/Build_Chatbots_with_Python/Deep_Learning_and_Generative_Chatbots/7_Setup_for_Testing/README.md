#### GENERATING TEXT WITH DEEP LEARNING
# [Setup for Testing](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/deep-learning-and-generative-chatbots/modules/deep-learning-for-nlp/lessons/generating-text-with-deep-learning/exercises/setup-for-testing)
To generate some original output text, we need to redefine the seq2seq architecture in pieces. 

The model we used for training our network only works when we already know the target sequence. This time, we have no idea what the Spanish should be for the English we pass in!
We need a model that will decode step-by-step instead of using teacher forcing. To do this, we need a seq2seq network in individual pieces.

We’ll build an encoder model with our encoder inputs and the placeholders for the encoder’s output states:
```
encoder_model = Model(encoder_inputs, encoder_states)
```
Next up, we need placeholders for the decoder’s input states, which we can build as input layers and store together.
We don’t know what we want to decode yet or what hidden state we’re going to end up with, so we need to do everything step-by-step.
We need to pass the encoder’s final hidden state to the decoder, sample a token, and get the updated hidden state back.
Then we’ll be able to (manually) pass the updated hidden state back into the network:
```
latent_dim = 256
decoder_state_input_hidden = Input(shape=(latent_dim,))

decoder_state_input_cell = Input(shape=(latent_dim,))

decoder_states_inputs = [decoder_state_input_hidden, decoder_state_input_cell]
```
Using the decoder LSTM and decoder dense layer (with the activation function) that we trained earlier, we’ll create new decoder states and outputs:
```
decoder_outputs, state_hidden, state_cell = 
    decoder_lstm(decoder_inputs, 
    initial_state=decoder_states_inputs)

# Saving the new LSTM output states:
decoder_states = [state_hidden, state_cell]

# Below, we redefine the decoder output
# by passing it through the dense layer:
decoder_outputs = decoder_dense(decoder_outputs)
```
Finally, we can set up the decoder model. 
```
decoder_model = Model(
  [decoder_inputs] + decoder_states_inputs,
  [decoder_outputs] + decoder_states
)
```

