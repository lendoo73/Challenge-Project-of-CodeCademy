import pickle

input_docs, target_docs, input_tokens, target_tokens, num_encoder_tokens, num_decoder_tokens, max_encoder_seq_length, max_decoder_seq_length, input_features_dict, target_features_dict, reverse_input_features_dict, reverse_target_features_dict, encoder_input_data, decoder_input_data, decoder_target_data = pickle.load(open("seq2seq_prep.p", "rb"))
