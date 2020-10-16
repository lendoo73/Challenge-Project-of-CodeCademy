#### TEXT PREPROCESSING
# Noise Removal
Depending on the goal of your project and where you get your data from, you may want to remove unwanted information, such as:
* punctuation and accents
* special characters
* numeric digits
* leading, ending, and vertical whitespace
* HTML formatting

 You can use the `.sub()` method in Python’s regular expression (re) library for most of your noise removal needs.
 
The `.sub()` method has three required arguments:

1. `pattern` – a regular expression that is searched for in the input string. There must be an r preceding the string to indicate it is a raw string, which treats backslashes as literal characters.
2. `replacement_text` – text that replaces all matches in the input string
3. `input` – the input string that will be edited by the .sub() method

The method returns a string with all instances of the pattern replaced by the replacement_text.

Example how to remove HTML `<p>` tags from a string:
```
import re 

text = "<p>    This is a paragraph</p>" 

result = re.sub(r'<.?p>', '', text)

print(result) 
#    This is a paragraph
```
