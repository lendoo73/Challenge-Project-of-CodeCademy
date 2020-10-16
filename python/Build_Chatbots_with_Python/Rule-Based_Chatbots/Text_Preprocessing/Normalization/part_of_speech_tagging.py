from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from part_of_speech import get_part_of_speech

lemmatizer = WordNetLemmatizer()

populated_island = 'Indonesia was founded in 1945. It contains the most populated island in the world, Java, with over 140 million people.'

tokenized_string = word_tokenize(populated_island)

lemmatized_pos = [lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized_string]

try:
  print(f'The lemmatized words are: {lemmatized_pos}')
except:
  print('Expected a variable called `lemmatized_pos`')
