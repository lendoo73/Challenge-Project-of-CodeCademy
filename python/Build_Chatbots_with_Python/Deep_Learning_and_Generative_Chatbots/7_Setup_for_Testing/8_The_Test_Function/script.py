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
  # 1. Encode the input as state vectors:
  encoder_states_value = encoder_model.predict(test_input)
  # Set decoder states equal to encoder final states
  decoder_states_value = encoder_states_value

  # 2. Generate empty target sequence of length 1:
  target_seq = np.zeros((1, 1, num_decoder_tokens))
  
  # 3. Populate the first token of target sequence with the start token:
  target_seq[0, 0, target_features_dict['<START>']] = 1.
  
  decoded_sentence = ''

  return decoded_sentence

for seq_index in range(10):
  test_input = encoder_input_data[seq_index: seq_index + 1]
  decoded_sentence = decode_sequence(test_input)
  print('-')
  print('Input sentence:', input_docs[seq_index])
  print('Decoded sentence:', decoded_sentence)
