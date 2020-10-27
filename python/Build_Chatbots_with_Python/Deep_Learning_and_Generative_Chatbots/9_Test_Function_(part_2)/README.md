#### GENERATING TEXT WITH DEEP LEARNING
# [Test Function (part 2)](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/deep-learning-and-generative-chatbots/modules/deep-learning-for-nlp/lessons/generating-text-with-deep-learning/exercises/seq2seq-test-function-2)
Inside the test function, we’ll decode the sentence word by word using the output state that we retrieved from the encoder (which becomes our decoder’s initial hidden state).
We’ll also update the decoder hidden state after each word so that we use previously decoded words to help decode new ones.

To tackle one word at a time, we need a while loop that will run until one of two things happens 
* The current token is "<END>".
* The decoded Spanish sentence length hits the maximum target sentence length.

Inside the while loop, the decoder model can use the current target sequence (beginning with the "<START>" token) and the current state (initially passed to us from the encoder model) to get a bunch of possible next words and their corresponding probabilities. In Keras, it looks something like this:
```
output_tokens, new_decoder_hidden_state, new_decoder_cell_state = 
    decoder_model.predict(
    [target_seq] + decoder_states_value)
```
Next, we can use NumPy’s .argmax() method to determine the token (word) with the highest probability and add it to the decoded sentence:
```
# slicing [0, -1, :] gives us a
# specific token vector within the
# 3d NumPy matrix
sampled_token_index = np.argmax(
    output_tokens[0, -1, :])

# The reverse features dictionary
# translates back from index to Spanish
sampled_token = reverse_target_features_dict[
    sampled_token_index]

decoded_sentence += " " + sampled_token
```
Our final step is to update a few values for the next word in the sequence:
```
# Move to the next timestep 
# of the target sequence:
target_seq = np.zeros((1, 1, num_decoder_tokens))
target_seq[0, 0, sampled_token_index] = 1.

# Update the states with values from
# the most recent decoder prediction:
decoder_states_value = [
    new_decoder_hidden_state,
    new_decoder_cell_state]
```
