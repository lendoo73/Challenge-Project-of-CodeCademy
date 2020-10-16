#### TEXT PREPROCESSING
# [Normalization](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/rule-based-chatbots/modules/nlp-text-preprocessing/lessons/text-preprocessing/exercises/normalization)
Some data may require further processing through text normalization. Text ***normalization*** is a catch-all term for various text pre-processing tasks.
Example:
* Upper or lowercasing: `my_string.upper()`, `my_string.lower()`
* Stopword removal
* Stemming – bluntly removing prefixes and suffixes from a word
* Lemmatization – replacing a single-word token with its root

## [Stopword Removal](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/rule-based-chatbots/modules/nlp-text-preprocessing/lessons/text-preprocessing/exercises/stopword-removal)
Stopwords are words that we remove during preprocessing when we don’t care about sentence structure. They are usually the most common words in a language and don’t provide any information about the tone of a statement.

They include words such as “a”, “an”, and “the”.

NLTK provides a built-in library with these words:
```
from nltk.corpus import stopwords 

stop_words = set(stopwords.words('english')) 
```
Now that we have the words saved to stop_words, we can use tokenization and a list comprehension to remove them from a sentence:
```
nbc_statement = "NBC was founded in 1926 making it the oldest major broadcast network in the USA"

word_tokens = word_tokenize(nbc_statement) 
# tokenize nbc_statement

statement_no_stop = [word for word in word_tokens if word not in stop_words]

print(statement_no_stop)
# ['NBC', 'founded', '1926', 'making', 'oldest', 'major', 'broadcast', 'network', 'USA']
```
We first tokenized our string, nbc_statement, then used a list comprehension to return a list with all of the stopwords removed.

## [Stemming](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/rule-based-chatbots/modules/nlp-text-preprocessing/lessons/text-preprocessing/exercises/stemming)
Stemming is the text preprocessing normalization task concerned with bluntly removing word affixes (prefixes and suffixes).
For example, stemming would cast the word “going” to “go”. This is a common method used by search engines to improve matching between user input and website hits.

NLTK has a built-in stemmer called PorterStemmer. You can use it with a list comprehension to stem each word in a tokenized list of words.
```
# import stemmer:
from nltk.stem import PorterStemmer

# initialize the stemmer:
stemmer = PorterStemmer()

tokenized = ['NBC', 'was', 'founded', 'in', '1926', '.', 'This', 'makes', 'NBC', 'the', 'oldest', 'major', 'broadcast', 'network', '.']

stemmed = [stemmer.stem(token) for token in tokenized]

print(stemmed)
# ['nbc', 'wa', 'found', 'in', '1926', '.', 'thi', 'make', 'nbc', 'the', 'oldest', 'major', 'broadcast', 'network', '.']
```
The words like ‘was’ and ‘founded’ became ‘wa’ and ‘found’.
Words can often be converted to something unrecognizable.
## [Lemmatization](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/rule-based-chatbots/modules/nlp-text-preprocessing/lessons/text-preprocessing/exercises/lemmatization)
*Lemmatization* is a method for casting words to their root forms.

This is a more involved process than stemming, because it requires the method to know the part-of-speech for each word. Since lemmatization requires the part of speech, it is a less efficient approach than stemming.

We can use NLTK’s WordNetLemmatizer to lemmatize text:
```
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
```
Once we have the lemmatizer initialized, we can use a list comprehension to apply the lemmatize operation to each word in a list:
```
tokenized = ["NBC", "was", "founded", "in", "1926"]

lemmatized = [lemmatizer.lemmatize(token) for token in tokenized]

print(lemmatized)
# ["NBC", "wa", "founded", "in", "1926"]
```
The result, saved to lemmatized contains 'wa', because lemmatize() treats every word as a noun. To take advantage of the power of lemmatization, we need to tag each word in our text with the most likely part of speech. 

## [Part-of-Speech Tagging](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/rule-based-chatbots/modules/nlp-text-preprocessing/lessons/text-preprocessing/exercises/part-of-speech-tagging)
To improve the performance of lemmatization, we need to find the part of speech for each word in our string.

`get_part_of_speech()`: The function accepts a word, then returns the most common part of speech for that word.

### 1. Import wordnet and Counter:
```
from nltk.corpus import wordnet
from collections import Counter
```
* `wordnet` is a database that we use for contextualizing words
* `Counter` is a container that stores elements as dictionary keys

### 2. Get synonyms:
`wordnet.synsets()` returns a set of synonyms for the word:
```
probable_part_of_speech = wordnet.synsets(word)
```
The returned synonyms come with their part of speech.
### 3. Use synonyms to determine the most likely part of speech:
Next, we create a Counter() object and set each value to the count of the number of synonyms that fall into each part of speech:
```
pos_counts["n"] = len(  [ item for item in probable_part_of_speech if item.pos()=="n"]  )
... 
```
This line counts the number of nouns in the synonym set.
### 4. Return the most common part of speech:
Now that we have a count for each part of speech, we can use the .most_common() counter method to find and return the most likely part of speech:
```
most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
```
<hr />

Now that we can find the most probable part of speech for a given word, we can pass this into our lemmatizer when we find the root for each word.
```
tokenized = ["How", "old", "is", "the", "country", "Indonesia"]

lemmatized = [lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized]

print(lemmatized)
# ['How', 'old', 'be', 'the', 'country', 'Indonesia']
# Previously: ['How', 'old', 'is', 'the', 'country', 'Indonesia']
```
