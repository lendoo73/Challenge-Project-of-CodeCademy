from data import spam_data

training_spam_docs = spam_data[0]
training_doc_tokens = spam_data[1]
training_labels = spam_data[2]
test_labels = spam_data[3]
test_spam_docs = spam_data[4]
raw_test_clean = spam_data[5]
raw_training_clean = spam_data[6]

training_docs = [doc[1] for doc in raw_training_clean]
test_docs = [doc[1] for doc in raw_test_clean]

