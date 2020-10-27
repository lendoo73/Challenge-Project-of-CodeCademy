from training import encoder_inputs, decoder_inputs, encoder_states, decoder_lstm, decoder_dense, encoder_input_data, num_decoder_tokens

from prep import target_features_dict, reverse_target_features_dict, max_decoder_seq_length, input_docs, target_docs, target_tokens

from tensorflow import keras
from keras.layers import Input, LSTM, Dense
from keras.models import Model, load_model
import numpy as np

training_model = load_model('training_model.h5')
encoder_inputs = training_model.input[0]
encoder_outputs, state_h_enc, state_c_enc = training_model.layers[2].output
encoder_states = [state_h_enc, state_c_enc]
encoder_model = Model(encoder_inputs, encoder_states)

latent_dim = 256
decoder_state_input_hidden = Input(shape=(latent_dim,))
decoder_state_input_cell = Input(shape=(latent_dim,))
decoder_states_inputs = [decoder_state_input_hidden, decoder_state_input_cell]
decoder_outputs, state_hidden, state_cell = decoder_lstm(decoder_inputs, initial_state=decoder_states_inputs)
decoder_states = [state_hidden, state_cell]
decoder_outputs = decoder_dense(decoder_outputs)
decoder_model = Model([decoder_inputs] + decoder_states_inputs, [decoder_outputs] + decoder_states)

def decode_sequence(test_input):
  encoder_states_value = encoder_model.predict(test_input)
  decoder_states_value = encoder_states_value
  target_seq = np.zeros((1, 1, num_decoder_tokens))
  target_seq[0, 0, target_features_dict['<START>']] = 1.
  decoded_sentence = ''
  
  stop_condition = False
  while not stop_condition:
    # 1. Run the decoder model to get possible 
    # output tokens (with probabilities) & states
    output_tokens, new_decoder_hidden_state, new_decoder_cell_state = decoder_model.predict(
      [target_seq] + decoder_states_value
    )
    
    # 2.
    sampled_token_index = np.argmax(output_tokens[0, -1, :])

    # Choose token with highest probability
    sampled_token = reverse_target_features_dict[sampled_token_index]
    decoded_sentence += " " + sampled_token

    # Exit condition: either hit max length
    # or find stop token.
    if (sampled_token == '<END>' or len(decoded_sentence) > max_decoder_seq_length):
      stop_condition = True

    # 3. Update the target sequence (of length 1).
    target_seq = np.zeros((1, 1, num_decoder_tokens))
    target_seq[0, 0, sampled_token_index] = 1.

    # Update states
    decoder_states_value = [new_decoder_hidden_state, new_decoder_cell_state]

  return decoded_sentence

for seq_index in range(10):
  test_input = encoder_input_data[seq_index: seq_index + 1]
  decoded_sentence = decode_sequence(test_input)
  print('-')
  print('Input sentence:', input_docs[seq_index])
  print('Decoded sentence:', decoded_sentence)
