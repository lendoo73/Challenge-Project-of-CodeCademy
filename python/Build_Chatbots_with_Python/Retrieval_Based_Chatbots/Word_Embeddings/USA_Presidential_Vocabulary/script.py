import os
import gensim
import spacy
from president_helper import read_file, process_speeches, merge_speeches, get_president_sentences, get_presidents_sentences, most_frequent_words

# 2. get list of all speech files
files = sorted([file for file in os.listdir() if file[-4 : ] == ".txt"])
#print(len(files))

# 3. read each speech file
speeches = [read_file(file_name) for file_name in files]
#print(speeches[0])

# 4. preprocess each speech
processed_speeches = process_speeches(speeches)
# the first inaugural address:
#print(processed_speeches[0])
# the first sentence:
#print(processed_speeches[0][0])
# the first word:
#print(processed_speeches[0][0][0])

# 5. merge speeches
all_sentences = merge_speeches(processed_speeches)
#print(all_sentences)

# 6. view most frequently used words
most_freq_words = most_frequent_words(all_sentences)
#print(most_freq_words)

# 7. create gensim model of all speeches
def create_gensim_model(corpus, size = 96, window = 5, min_count = 1, workers = 2, sg = 1): 
  return gensim.models.Word2Vec(
    corpus, 
    size = size, 
    window = window, 
    min_count = min_count, 
    workers = workers, 
    sg = sg
  )

all_prez_embeddings = create_gensim_model(all_sentences)

# 8. view words similar to freedom
similar_to_freedom = all_prez_embeddings.most_similar(
  "freedom",
  topn = 20
)
#print(similar_to_freedom)

# 9.
similar_to_liberties = all_prez_embeddings.most_similar(
  "liberty",
  topn = 20
)
#print(similar_to_liberties)

# 10. get President Roosevelt sentences
roosevelt_sentences = get_president_sentences("franklin-d-roosevelt")
#print(roosevelt_sentences)

# 11. view most frequently used words of Roosevelt
roosevelt_most_freq_words = most_frequent_words(roosevelt_sentences)
#print(roosevelt_most_freq_words)

# 12. create gensim model for Roosevelt
roosevelt_embeddings = create_gensim_model(roosevelt_sentences)

# 13. view words similar to freedom for Roosevelt
roosevelt_similar_to_freedom = roosevelt_embeddings.most_similar(
  "freedom",
  topn = 20
)
#print(roosevelt_similar_to_freedom)

# 14. get sentences of multiple presidents
rushmore_prez_sentences = get_presidents_sentences(["washington","jefferson","lincoln","theodore-roosevelt"])

# 15. view most frequently used words of presidents
rushmore_most_freq_words = most_frequent_words(rushmore_prez_sentences)
#print(rushmore_most_freq_words)

# 16. create gensim model for the presidents
rushmore_embeddings = create_gensim_model(rushmore_prez_sentences)

# 17. view words similar to freedom for presidents
rushmore_similar_to_freedom = rushmore_embeddings.most_similar(
  "freedom",
  topn = 20
)
#print(rushmore_similar_to_freedom)

# 18.
rushmore_similar_to_peace = rushmore_embeddings.most_similar(
  "peace",
  topn = 20
)
#print(rushmore_similar_to_peace)

# 19.
word_war_prez_sentences = get_presidents_sentences(["wilson", "franklin-d-roosevelt", "truman"])
#print(word_war_prez_sentences)

word_war_most_freq_words = most_frequent_words(word_war_prez_sentences)
#print(word_war_most_freq_words)

word_war_embeddings = create_gensim_model(word_war_prez_sentences)

word_war_similar_to_peace = word_war_embeddings.most_similar(
  "peace",
  topn = 20
)
#print(word_war_similar_to_peace)

word_war_against_to_peace = word_war_embeddings.doesnt_match(["peace", "war", "life"])
print(word_war_against_to_peace)
