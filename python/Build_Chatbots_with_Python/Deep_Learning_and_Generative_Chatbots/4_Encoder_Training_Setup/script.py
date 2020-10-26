from tensorflow import keras
from keras.layers import Input, LSTM
from keras.models import Model
#from prep import num_encoder_tokens
num_encoder_tokens = 18

# 1. Create the input layer:
encoder_inputs = Input(shape=(None, num_encoder_tokens))

# 2. Create the LSTM layer:
encoder_lstm = LSTM(256, return_state=True)

# 3. Retrieve the outputs and states:
encoder_outputs, state_hidden, state_cell = encoder_lstm(encoder_inputs)

# Put the states together in a list:
encoder_states = [state_hidden, state_cell]
