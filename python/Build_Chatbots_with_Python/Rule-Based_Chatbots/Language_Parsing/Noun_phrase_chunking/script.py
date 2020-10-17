from nltk import RegexpParser
from pos_tagged_oz import pos_tagged_oz
from np_chunk_counter import np_chunk_counter

# define noun-phrase chunk grammar here
chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"

# create RegexpParser object here
chunk_parser = RegexpParser(chunk_grammar)

# create a list to hold noun-phrase chunked sentences
np_chunked_oz = list()

# create a for loop through each pos-tagged sentence in pos_tagged_oz here
for sentece in pos_tagged_oz:
  # chunk each sentence and append to np_chunked_oz here
  np_chunked_oz.append(chunk_parser.parse(sentece))

  

# store and print the most common np-chunks here
most_common_np_chunks = np_chunk_counter(np_chunked_oz)
print(most_common_np_chunks)
