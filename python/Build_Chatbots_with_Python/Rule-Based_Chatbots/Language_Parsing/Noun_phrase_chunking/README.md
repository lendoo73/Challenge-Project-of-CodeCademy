#### NATURAL LANGUAGE PARSING WITH REGULAR EXPRESSIONS
# [Chunking Noun Phrases](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/rule-based-chatbots/modules/nlp-language-parsing/lessons/nlp-regex-parsing-intro/exercises/chunking-noun-phrases)
One such type of chunking is NP-chunking, or ***noun phrase chunking***.

A noun phrase is a phrase that contains a noun and operates, as a unit, as a noun.

A popular form of noun phrase
* begins with a determiner `DT`, which specifies the noun being referenced,
* followed by any number of adjectives `JJ`, which describe the noun,
* and ends with a noun `NN`.

The chunk grammar for a noun phrase:
```
chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"
```
* `NP: `the user-defined name of the chunk you are searching for. In this case NP stands for noun phrase
* `<DT>`: matches any determiner
* `?`: optional quantifier, matching either 0 or 1 determiners
* `<JJ>`: matches any adjective
* `*`: the Kleene star quantifier, matching 0 or more occurrences of an adjective
* `<NN>`: matches any noun, singular or plural
