import codecademylib3_seaborn
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from preprocessing import preprocess_text

poem = '''
Success is counted sweetest
By those who ne'er succeed.
To comprehend a nectar
Requires sorest need.

Not one of all the purple host
Who took the flag to-day
Can tell the definition,
So clear, of victory,

As he, defeated, dying,
On whose forbidden ear
The distant strains of triumph
Break, agonized and clear!'''

# define clear_count:
clear_count = 2

# preprocess text
processed_poem = preprocess_text(poem)

# initialize and fit CountVectorizer
vectorizer = CountVectorizer()
term_frequencies = vectorizer.fit_transform([processed_poem])

# get vocabulary of terms
feature_names = vectorizer.get_feature_names()

# create pandas DataFrame with term frequencies
try:
  df_term_frequencies = pd.DataFrame(term_frequencies.T.todense(), index=feature_names, columns=['Term Frequency'])
  print(df_term_frequencies)
except:
  pass
