from user_functions import preprocess, compare_overlap, pos_tag, extract_nouns, word2vec, compute_similarity
from collections import Counter

user_message = "Good morning... will it rain in Chicago later this week?"

blank_spot = "illinois city"
response_a = "The average temperature this weekend in {} with be 88 degrees. Bring your sunglasses!"
response_b = "Forget about your umbrella; there is no rain forecasted in {} this weekend."
response_c = "This weekend, a warm front from the southeast will keep skies near {} clear."
responses= [response_a, response_b, response_c]

#preprocess documents
bow_user_message = Counter(preprocess(user_message))
processed_responses = [Counter(preprocess(response)) for response in responses]

#determine intent with BoW
similarity_list = [compare_overlap(doc, bow_user_message) for doc in processed_responses]


#extract entities with word2vec 
tagged_user_message = pos_tag(preprocess(user_message))
message_nouns = extract_nouns(tagged_user_message)

#execute word2vec below
tokens = word2vec(" ".join(message_nouns))
category = word2vec(blank_spot)
word2vec_result = compute_similarity(tokens, category)


#select final response below
response_index = similarity_list.index(max(similarity_list))
#print(word2vec_result)
entity = word2vec_result[2][0]

final_response = responses[response_index].format(entity)
print(final_response)
