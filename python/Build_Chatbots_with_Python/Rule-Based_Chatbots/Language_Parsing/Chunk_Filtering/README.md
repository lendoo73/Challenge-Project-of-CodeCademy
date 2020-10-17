#### NATURAL LANGUAGE PARSING WITH REGULAR EXPRESSIONS
# [Chunk Filtering](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/rule-based-chatbots/modules/nlp-language-parsing/lessons/nlp-regex-parsing-intro/exercises/chunk-filtering)
Another option you have to find chunks in your text is chunk filtering.

***Chunk filtering*** lets you define what parts of speech you do not want in a chunk and remove them.

A popular method for performing chunk filtering is to chunk an entire sentence together and then indicate which parts of speech are to be filtered out. If the filtered parts of speech are in the middle of a chunk, it will split the chunk into two separate chunks! 

The chunk grammar:
```
chunk_grammar = """NP: {<.*>+}
                       }<VB.?|IN>+{"""
```
* `NP`: the user-defined name of the chunk you are searching for. In this case NP stands for noun phrase
* `{}`: indicate what parts of speech you are chunking. `<.*>+` matches every part of speech in the sentence
* `}{`: the inverted brackets indicate which parts of speech you want to filter from the chunk. `<VB.?|IN>+` will filter out any verbs or prepositions
