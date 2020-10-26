#### GENERATING TEXT WITH DEEP LEARNING
# [Setup for Testing](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/deep-learning-and-generative-chatbots/modules/deep-learning-for-nlp/lessons/generating-text-with-deep-learning/exercises/setup-for-testing)
To generate some original output text, we need to redefine the seq2seq architecture in pieces. 

The model we used for training our network only works when we already know the target sequence. This time, we have no idea what the Spanish should be for the English we pass in!
We need a model that will decode step-by-step instead of using teacher forcing. To do this, we need a seq2seq network in individual pieces.

We’ll build an encoder model with our encoder inputs and the placeholders for the encoder’s output states:
```
encoder_model = Model(encoder_inputs, encoder_states)
```
