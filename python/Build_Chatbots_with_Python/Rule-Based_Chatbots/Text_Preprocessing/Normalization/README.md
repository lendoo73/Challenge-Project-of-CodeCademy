#### TEXT PREPROCESSING
# Normalization
Some data may require further processing through text normalization. Text ***normalization*** is a catch-all term for various text pre-processing tasks.
Example:
* Upper or lowercasing: `my_string.upper()`, `my_string.lower()`
* Stopword removal
* Stemming – bluntly removing prefixes and suffixes from a word
* Lemmatization – replacing a single-word token with its root

## Stopword Removal
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

## Stemming
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
