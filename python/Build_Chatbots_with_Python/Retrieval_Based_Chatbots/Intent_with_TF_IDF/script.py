from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocessing import preprocess_text 

response_a = "Every dress style is cut from a polyester blend for a strechy fit."
response_b = "The 'Elosie' dress runs large. I suggest you take your regular size or smaller."
response_c = "The 'Elosie' dress comes in green, lavender, and orange."
user_message = "Hello! What is the fit of the 'Elosie' dress? My shoulders are broad, so I often size up for a comfortable fit. Do dress sizes run large or small?"

documents = [response_a, response_b, response_c, user_message]

# preprocess responses and user_message:
processed_docs = [preprocess_text(response) for response in documents]

# create tfidf vectorizer:
vectorizer = TfidfVectorizer()

# fit and transform vectorizer on processed docs:
tfidf_vectors = vectorizer.fit_transform(processed_docs)

# compute cosine similarity betweeen the user message tf-idf vector and the different response tf-idf vectors:
cosine_similarities = cosine_similarity(tfidf_vectors[-1], tfidf_vectors)

# get the index of the most similar response to the user message:
similar_response_index = cosine_similarities.argsort()[0][-2]

best_response = documents[similar_response_index]
print(best_response)
