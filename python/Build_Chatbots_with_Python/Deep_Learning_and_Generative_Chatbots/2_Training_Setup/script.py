from tensorflow import keras
import numpy as np
from preprocessing import input_docs, target_docs, input_tokens, target_tokens, num_encoder_tokens, num_decoder_tokens, max_encoder_seq_length, max_decoder_seq_length

print('Number of samples:', len(input_docs))
print('Number of unique input tokens:', num_encoder_tokens)
print('Number of unique output tokens:', num_decoder_tokens)
print('Max sequence length for inputs:', max_encoder_seq_length)
print('Max sequence length for outputs:', max_decoder_seq_length)

input_features_dict = dict(
    [(token, i) for i, token in enumerate(input_tokens)])

# 1. Build out target_features_dict:
target_features_dict = dict(
   [(token, i) for i, token in enumerate(target_tokens)]
)

# Reverse-lookup token index to decode sequences back to
# something readable.
reverse_input_features_dict = dict(
    (i, token) for token, i in input_features_dict.items())
# 2. Build out reverse_target_features_dict:
reverse_target_features_dict = dict(
  [(i, token) for token, i in target_features_dict.items()]
)

encoder_input_data = np.zeros(
    (len(input_docs), max_encoder_seq_length, num_encoder_tokens),
    dtype='float32')
#print("\nHere's the first item in the encoder input matrix:\n", encoder_input_data[0], "\n\nThe number of columns should match the number of unique input tokens and the number of rows should match the maximum sequence length for input sentences.")

# 3. Build out the decoder_input_data matrix:
decoder_input_data = np.zeros(
  (
    len(input_docs),
    max_decoder_seq_length,
    num_decoder_tokens
  ), dtype = "float32"
)

# 3. Build out the decoder_target_data matrix:
decoder_target_data = np.zeros(
  (
    len(target_docs),
    max_decoder_seq_length,
    num_decoder_tokens
  ), dtype = "float32"
)
