#### GENERATING TEXT WITH DEEP LEARNING
# [The Test Function](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/deep-learning-and-generative-chatbots/modules/deep-learning-for-nlp/lessons/generating-text-with-deep-learning/exercises/the-seq2seq-test-function)
Finally, we can get to testing our model! To do this, we need to build a function that:
* accepts a NumPy matrix representing the test English sentence input
* uses the encoder and decoder we’ve created to generate Spanish output

Inside the test function, we’ll run our new English sentence through the encoder model. The `.predict()` method takes in new input (as a NumPy matrix) and gives us output states that we can pass on to the decoder:
```
# test_input is a NumPy matrix
# representing an English sentence
states = encoder.predict(test_input)
```
Next, we’ll build an empty NumPy array for our Spanish translation, giving it three dimensions:
```
# batch size: 1
# number of tokens to start with: 1
# number of tokens in our target vocabulary
target_sequence = np.zeros((1, 1, num_decoder_tokens))
```
We already know the first value in our Spanish sentence — "<Start>"! So we can give "<Start>" a value of 1 at the first timestep:
```
target_sequence[0, 0, target_features_dict['<START>']] = 1.
```
Before we get decoding, we’ll need a string where we can add our translation to, word by word:
```
decoded_sentence = ''
```
This is the variable that we will ultimately return from the function.

