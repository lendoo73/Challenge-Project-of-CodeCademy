from training import encoder_inputs, decoder_inputs, encoder_states, decoder_lstm, decoder_dense

from tensorflow import keras
from keras.layers import Input, LSTM, Dense
from keras.models import Model, load_model

training_model = load_model('training_model.h5')
# These next lines are only necessary
# because we're using a saved model:
encoder_inputs = training_model.input[0]
encoder_outputs, state_h_enc, state_c_enc = training_model.layers[2].output
encoder_states = [state_h_enc, state_c_enc]

# Building the encoder test model:
encoder_model = Model(encoder_inputs, encoder_states)

latent_dim = 256
# Building the two decoder state input layers:
decoder_state_input_hidden = Input(shape=(latent_dim,))

decoder_state_input_cell = Input(shape=(latent_dim,))

# 1. Put the state input layers into a list:
decoder_states_inputs = [decoder_state_input_hidden, decoder_state_input_cell]

# 2. Call the decoder LSTM:
decoder_outputs, state_hidden, state_cell = decoder_lstm(decoder_inputs, initial_state=decoder_states_inputs)

decoder_states = [state_hidden, state_cell]
# 3. Redefine the decoder outputs:
decoder_outputs = decoder_dense(decoder_outputs)

# 4. Build the decoder test model:
decoder_model = Model(
  [decoder_inputs] + decoder_states_inputs,
  [decoder_outputs] + decoder_states
)


