import spacy
word2vec = spacy.load('en')

message_nouns = ['shirts', 'weekend', 'package']

tokens = word2vec(" ".join(message_nouns))
category = word2vec("clothes")


def compute_similarity(tokens, category):
  output_list = list()
  #your code here
  for token in tokens:
    output_list.append(f"{token.text} {category.text} {token.similarity(category)}")
  return output_list

print(compute_similarity(tokens, category))

blank_spot = message_nouns[0]
bot_response = f"Hey! I just checked my records, your shipment containing {blank_spot} is en route. Expect it within the next two days!"
print(bot_response)
