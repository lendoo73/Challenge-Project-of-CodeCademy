#### NATURAL LANGUAGE PARSING WITH REGULAR EXPRESSIONS
## [Part-of-Speech Tagging](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/rule-based-chatbots/modules/nlp-language-parsing/lessons/nlp-regex-parsing-intro/exercises/pos-tagging)

| Part of speech | Function or "job" | Example words | Example sentences |
| --- | --- | --- | --- |
| **Noun** | the name of a person, place, thing, or idea | pen, dog, work, music, town, Chicago, teacher, John | This is my **cat**. He lives in my **house**. We live in **Chicago**. |
| **Pronoun** | a word used in place of a noun | I, you, he, she, some | Tara is a student. **She** is studying Computer Science. |
| **Determiner** | a word that introduces, limits, or "determines" a noun | a/an, the, 2, some, many | I have **two** alligators and **some** bunnies. |
| **Verb** | expresses action, state, or being | (to) be, have, do, like, work, sing, can, must | Codecademy **is** a web site. I **like** Codecademy. |
| **Adjective** | modifies or describes a noun or pronoun | good, big, red, colorful, well, interesting | My parrots are **big**. I like **colorful** parrots. |
| **Adverb** | modifies or describes a verb, an adjective, or another adverb | quickly, silently, well, badly, very, really | My lizard eats **quickly**. When he is **very** hungry, he eats **really** quickly. |
| **Preposition** | a word placed before a noun or pronoun to form a phrase modifying another word in the sentence | to, at, after, on, but | We went **to** work **on** Friday. |
| **Conjunction** | a word that joins words, phrases, clauses, or sentences | and, but, when | I like tigers **and** I like lions. I like lions **and** tigers. I like tigers **but** I don't like lions. |
| **Interjection** | a short exclamation, inserted into a sentence to express emotion | oh!, ouch!, hi!, well | **Ouch**! That hurts! **Hi**! How are you? **Well**, I don't know. |

Automate the part-of-speech tagging process with `nltk`‘s `pos_tag()` function:
* the function takes one argument, a list of words in the order they appear in a sentence,
* returns a list of tuples, where the first entry in the tuple is a word and the second is the part-of-speech tag.

```
from nltk import pos_tag

word_sentence = ['do', 'you', 'suppose', 'oz', 'could', 'give', 'me', 'a', 'heart', '?']

part_of_speech_tagged_sentence = pos_tag(word_sentence)
```
Abbreviations are given instead of the full part of speech name.
```
[
('do', 'VB'),                   # Verb, base form
('you', 'PRP'),                 # Personal pronoun 
('suppose', 'VB'), 
('oz', 'NNS'),                  # Noun, plural
('could', 'MD'),                # Modal
('give', 'VB'), 
('me', 'PRP'), 
('a', 'DT'),                    # Determiner
('heart', 'NN'),                # Noun, singular or mass 
('?', '.')
]
```
A complete list of part-of-speech tags and their abbreviations can be found [here](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html).
## Chunking
Given your part-of-speech tagged text, you can now use regular expressions to find patterns in sentence structure that give insight into the meaning of a text. This technique of grouping words by their part-of-speech tag is called ***chunking***.

With chunking in nltk, you can define a pattern of parts-of-speech tags using a modified notation of regular expressions. You can then find non-overlapping matches, or chunks of words, in the part-of-speech tagged sentences of a text.

##### chunk grammar
The regular expression you build to find chunks is called ***chunk grammar***.
```
chunk_grammar = "AN: {<JJ><NN>}"        # will match any adjective that is followed by a noun.
```
* `AN` is a user-defined name for the kind of chunk you are searching for. In this case AN stands for adjective-noun
* `{}` surround the actual chunk grammar
* `<JJ>` operates similarly to a regex character class, matching any adjective
* `<NN>` matches any noun, singular or plural

##### `nltk RegexpParser` object
To use the chunk grammar defined, you must create a nltk RegexpParser object and give it a piece of chunk grammar as an argument.
```
chunk_parser = RegexpParser(chunk_grammar)
```
You can then use the `RegexpParser` object’s `.parse()` method, which takes a list of part-of-speech tagged words as an argument, and identifies where such chunks occur in the sentence!
```
pos_tagged_sentence = [
  ('where', 'WRB'), 
  ('is', 'VBZ'), 
  ('the', 'DT'), 
  ('emerald', 'JJ'), 
  ('city', 'NN'), 
  ('?', '.')
]

chunked = chunk_parser.parse(pos_tagged_sentence)
```
