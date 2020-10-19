from mystery_test import postcard_test, email_test
from goldman_emma_raw import goldman_docs, goldman_test
from henson_matthew_raw import henson_docs, henson_test
from wu_tingfang_raw import wu_docs, wu_test
# 1. import sklearn modules here:
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Setting up the combined list of friends' writing samples
friends_docs = goldman_docs + henson_docs + wu_docs
# Setting up labels for your three friends
friends_labels = [1] * 154 + [2] * 141 + [3] * 166

# 5. Print out a document from each friend:
#print(goldman_docs[0])
#print(henson_docs[0])
#print(henson_docs[0])

# Postcard test:
#mystery_postcard = postcard_test

# Emma Goldman test
#mystery_postcard = goldman_test

# Matthew Henson test
#mystery_postcard = henson_test

# TingFang Wu test
#mystery_postcard = wu_test

# an email test:
mystery_postcard = email_test

# 2. Create bow_vectorizer:
bow_vectorizer = CountVectorizer()

# 3. Define friends_vectors (training vector):
friends_vectors = bow_vectorizer.fit_transform(friends_docs)


# 4. Define mystery_vector: 
mystery_vector = bow_vectorizer.transform([mystery_postcard])

# 6. Define friends_classifier:
friends_classifier = MultinomialNB()

# 7. Train the classifier:
friends_classifier.fit(friends_vectors, friends_labels)

# 8. Change predictions:
predictions = friends_classifier.predict(mystery_vector)

mystery_friend = predictions[0] if predictions[0] else "someone else"

# Uncomment the print statement:
names = ["Emma Goldman", "Matthew Henson", "TingFang Wu"]
print("The postcard was from {}!".format(names[mystery_friend - 1]))
