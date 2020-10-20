import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from preprocessing import preprocess_text
from poems import poems

# preprocess text
processed_poems = [preprocess_text(poem) for poem in poems]

# initialize and fit CountVectorizer
vectorizer = CountVectorizer()
term_frequencies = vectorizer.fit_transform(processed_poems)

# get vocabulary of terms
feature_names = vectorizer.get_feature_names()

# get corpus index
corpus_index = [f"Poem {i+1}" for i in range(len(poems))]

# create pandas DataFrame with term frequencies
df_term_frequencies = pd.DataFrame(term_frequencies.T.todense(), index=feature_names, columns=corpus_index)
