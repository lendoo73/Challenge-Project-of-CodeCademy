#### [INTRODUCTION TO REGULAR EXPRESSIONS](https://www.codecademy.com/courses/practical-data-cleaning/lessons/nlp-regex-conceptual/exercises/introduction)

A regular expression is a special sequence of characters that describe a pattern of text that should be found, or matched, in a string or document. 
By matching text, we can identify how often and where certain pieces of text occur, as well as have the opportunity to replace or update these pieces of text if needed.

## [Literals](https://www.codecademy.com/courses/practical-data-cleaning/lessons/nlp-regex-conceptual/exercises/literals)
The simplest text we can match with regular expressions are ***literals***. 
This is where our regular expression contains the exact text that we want to match.  
The regex  
`bananas` will match the text `bananas`.

## [Alternation](https://www.codecademy.com/courses/practical-data-cleaning/lessons/nlp-regex-conceptual/exercises/alternation)
Alternation, performed in regular expressions with the pipe symbol, `|`, allows us to match either the characters preceding the `|` OR the characters after the `|`.  
The regex  
`baboons|gorillas` will match `baboons` in the text `I love baboons`, but will also match `gorillas` in the text `I love gorillas`.
