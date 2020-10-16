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
