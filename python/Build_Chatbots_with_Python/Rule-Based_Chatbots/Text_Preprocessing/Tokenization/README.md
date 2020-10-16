#### TEXT PREPROCESSING

# [Tokenization](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/rule-based-chatbots/modules/nlp-text-preprocessing/lessons/text-preprocessing/exercises/tokenization)
For many natural language processing tasks, we need access to each word in a string. To access each word, we first have to break the text into smaller components. The method for breaking text into smaller components is called ***tokenization*** and the individual components are called tokens.

A few common operations that require tokenization include:
* Finding how many words or sentences appear in text
* Determining how many times a specific word or phrase exists
* Accounting for which terms are likely to co-occur

To ***tokenize individual words***, we can use `nltk`‘s `word_tokenize()` function. The function accepts a string and returns a list of words:
```
from nltk.tokenize import word_tokenize

text = "Tokenize this text"
tokenized = word_tokenize(text)

print(tokenized)
# ["Tokenize", "this", "text"]
```
To ***tokenize at the sentence level***, we can use `sent_tokenize()` from the same module:
```
from nltk.tokenize import sent_tokenize

text = "Tokenize this sentence. Also, tokenize this sentence."
tokenized = sent_tokenize(text)

print(tokenized)
# ['Tokenize this sentence.', 'Also, tokenize this sentence.']
```
