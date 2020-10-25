from user_functions import preprocess, compare_overlap, pos_tag, extract_nouns, compute_similarity
from data import responses, blank_spot
from collections import Counter
import spacy

word2vec = spacy.load('en')

class ChatBot:
  def find_intent_match(self, responses, user_message):
    bow_user_message = Counter(preprocess(user_message))
    processed_responses = [Counter(preprocess(response)) for response in responses]
    # define similarity_list here:
    similarity_list = [compare_overlap(bow_user_message, doc) for doc in processed_responses]
    # define response_index here:
    response_index = similarity_list.index(max(similarity_list))

    return responses[response_index]
    
  def find_entities(self, user_message):
    tagged_user_message = pos_tag(preprocess(user_message))
    message_nouns = extract_nouns(tagged_user_message)
    
    # execute word2vec model here:
    tokens = word2vec(" ".join(message_nouns))
    category = word2vec(blank_spot)
    word2vec_result = compute_similarity(tokens, category)
    word2vec_result.sort(key=lambda x: x[2])
    
    return word2vec_result[-1][0]

  # define .respond() here:
  def respond(self, user_message):
    best_response = self.find_intent_match(responses, user_message)
    entity =  self.find_entities(user_message)
    print(best_response.format(entity))

  def chat(self):
    user_message = input("Hi, I'm Stratus. Ask me about your local weather!\n")
    self.respond(user_message)

# create ChatBot() instance:
my_chat = ChatBot()
# call .chat() method:
my_chat.chat()

