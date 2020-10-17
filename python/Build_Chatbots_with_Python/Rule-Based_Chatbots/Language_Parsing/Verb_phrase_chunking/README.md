#### NATURAL LANGUAGE PARSING WITH REGULAR EXPRESSIONS
# [Chunking Verb Phrases](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/rule-based-chatbots/modules/nlp-language-parsing/lessons/nlp-regex-parsing-intro/exercises/chunking-verb-phrases)
Another popular type of chunking is VP-chunking, or ***verb phrase chunking***.

A verb phrase is a phrase that contains a verb and its complements, objects, or modifiers.

Verb phrases can take a variety of structures, and here you will consider two. 
1. The first structure begins with a verb VB of any tense, followed by a noun phrase, and ends with an optional adverb RB of any form.
```
(
  ('said', 'VBD'), 
  ('the', 'DT'), 
  ('cowardly', 'JJ'), 
  ('lion', 'NN')
)
```
The chunk grammar to find the first form of verb phrase:
```
chunk_grammar = "VP: {<VB.*><DT>?<JJ>*<NN><RB.?>?}"
```
* `VP`: the user-defined name of the chunk you are searching for. In this case VP stands for verb phrase
* `<VB.*>` matches any verb using the `.` as a wildcard and the `*` quantifier to match 0 or more occurrences of any character. 
`VB`	Verb, base form	
`VBD`	Verb, past tense	
`VBG`	Verb, gerund or present participle	
`VBN`	Verb, past participle	
`VBP`	Verb, non-3rd person singular present	
`VBZ`	Verb, 3rd person singular present
2. The second structure switches the order of the verb and the noun phrase, but also ends with an optional adverb.
```
(
  ('the', 'DT'), 
  ('cowardly', 'JJ'), 
  ('lion', 'NN'),
  ('said', 'VBD')
)
```
