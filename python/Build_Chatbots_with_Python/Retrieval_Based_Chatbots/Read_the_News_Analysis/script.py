import codecademylib3_seaborn
import pandas as pd
import numpy as np
from articles import articles
from preprocessing import preprocess_text

# 1. import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer

# 2. view article
#print(articles[0])

# 3. preprocess articles
processed_articles = [preprocess_text(article) for article in articles]
#print(processed_articles[0])

# 4-5. initialize and fit CountVectorizer
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(processed_articles)

# 6-7. convert counts to tf-idf
transformer = TfidfTransformer(norm = None)
tfidf_scores_transformed = transformer.fit_transform(counts)

# 8-9. initialize and fit TfidfVectorizer
vectorizer = TfidfVectorizer(norm = None)
tfidf_scores = vectorizer.fit_transform(processed_articles)

# 10. check if tf-idf scores are equal
if np.allclose(tfidf_scores_transformed.todense(), tfidf_scores.todense()):
  print(pd.DataFrame({'Are the tf-idf scores the same?':['YES']}))
else:
  print(pd.DataFrame({'Are the tf-idf scores the same?':['No, something is wrong :(']}))

# get vocabulary of terms
try:
  feature_names = vectorizer.get_feature_names()
except:
  pass

# get article index
try:
  article_index = [f"Article {i+1}" for i in range(len(articles))]
except:
  pass

# create pandas DataFrame with word counts
try:
  df_word_counts = pd.DataFrame(counts.T.todense(), index=feature_names, columns=article_index)
  print(df_word_counts)
except:
  pass

# create pandas DataFrame(s) with tf-idf scores
try:
  df_tf_idf = pd.DataFrame(tfidf_scores_transformed.T.todense(), index=feature_names, columns=article_index)
  print(df_tf_idf)
except:
  pass

try:
  df_tf_idf = pd.DataFrame(tfidf_scores.T.todense(), index=feature_names, columns=article_index)
  print(df_tf_idf)
except:
  pass

# 11. get highest scoring tf-idf term for each article
for i in range(1, 11):
  # 12. get the index of the highest value in a DataFrame column:
  print(df_tf_idf[[f'Article {i}']].idxmax())
