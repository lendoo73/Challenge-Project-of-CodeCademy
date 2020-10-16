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
