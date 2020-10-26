from tensorflow import keras
import numpy as np
import re
from preprocessing import input_docs, target_docs, input_tokens, target_tokens, num_encoder_tokens, num_decoder_tokens, max_encoder_seq_length, max_decoder_seq_length

input_features_dict = dict(
    [(token, i) for i, token in enumerate(input_tokens)])
target_features_dict = dict(
    [(token, i) for i, token in enumerate(target_tokens)])

reverse_input_features_dict = dict(
    (i, token) for token, i in input_features_dict.items())
reverse_target_features_dict = dict(
    (i, token) for token, i in target_features_dict.items())

encoder_input_data = np.zeros(
    (len(input_docs), max_encoder_seq_length, num_encoder_tokens),
    dtype='float32')
decoder_input_data = np.zeros(
    (len(input_docs), max_decoder_seq_length, num_decoder_tokens),
    dtype='float32')
decoder_target_data = np.zeros(
    (len(input_docs), max_decoder_seq_length, num_decoder_tokens),
    dtype='float32')

for line, (input_doc, target_doc) in enumerate(zip(input_docs, target_docs)):

  for timestep, token in enumerate(re.findall(r"[\w']+|[^\s\w]", input_doc)):

    print("Encoder input timestep & token:", timestep, token)
    print(input_features_dict[token])
    # 1. Assign 1. for the current line, timestep, & word in encoder_input_data:
    encoder_input_data[line, timestep, input_features_dict[token]] = 1

  for timestep, token in enumerate(target_doc.split()):

    # decoder_target_data is ahead of decoder_input_data by one timestep
    print("Decoder input timestep & token:", timestep, token)
    # 2. Assign 1. for the current line, timestep, & word in decoder_input_data:
    decoder_input_data[line, timestep, target_features_dict[token]] = 1

    if timestep > 0:
      # decoder_target_data is ahead by 1 timestep
      # and doesn't include the start token.
      print("Decoder target timestep:", timestep)
      # 3. Assign 1. for the current line, timestep, & word in decoder_target_data:
      decoder_target_data[line, timestep - 1, target_features_dict[token]] = 1
           
