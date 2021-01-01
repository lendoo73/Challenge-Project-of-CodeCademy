from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# ------ Exploring the Data ------

#emails = fetch_20newsgroups()

#print(type(emails))  # <class 'sklearn.utils.Bunch'>
#print(emails.keys())  # 'data', 'filenames', 'target_names', 'target', 'DESCR'
#print(emails.target_names) # different  categories

#emails = fetch_20newsgroups(categories = [
#  'rec.sport.baseball', 
#  'rec.sport.hockey'
#])

#print(type(emails.data))  # list
#print(emails.data[5])

# the labels:
#print(type(emails.target))  # numpy.ndarray
#print(emails.target[5])  # 1
#print(type(emails.target_names))  # list
#print(emails.target_names)  # ['rec.sport.baseball', 'rec.sport.hockey']
#print(emails.target_names[emails.target[5]])

def model(categories):
  # ------ Making the Training and Test Sets ------
  train_emails = fetch_20newsgroups(
    categories = categories,
    subset = "train",
    shuffle = True,
    random_state = 108
  )

  test_emails = fetch_20newsgroups(
    categories = categories,
    subset = "test",
    shuffle = True,
    random_state = 108
  )

  # ------ Counting Words ------
  counter = CountVectorizer()

  counter.fit(train_emails.data + test_emails.data)
  #print(counter.vocabulary_)

  train_counts = counter.transform(train_emails.data)
  test_counts = counter.transform(test_emails.data)

  # ------ Making a Naive Bayes Classifier ------
  classifier = MultinomialNB()

  classifier.fit(
    train_counts,        # trainig set
    train_emails.target  # trainig labels
  )

  print(classifier.score(
    test_counts,        # test set
    test_emails.target  # test labels
  ))

# ------ Testing Other Datasets ------
model([
  'rec.sport.baseball', 
  'rec.sport.hockey'
])
model([
  'comp.sys.ibm.pc.hardware', 
  'rec.sport.hockey'
])
model([
  'comp.sys.ibm.pc.hardware', 
  'rec.sport.hockey',
  "talk.religion.misc"
])
