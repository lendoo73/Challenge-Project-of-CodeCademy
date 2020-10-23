import os
from nltk.tokenize import PunktSentenceTokenizer
from collections import Counter

def read_file(file_name):
  with open(file_name, 'r+', encoding='utf-8') as file:
    file_text = file.read()
  return file_text

def process_speeches(speeches):
  word_tokenized_speeches = list()
  for speech in speeches:
    sentence_tokenizer = PunktSentenceTokenizer()
    sentence_tokenized_speech = sentence_tokenizer.tokenize(speech)
    word_tokenized_sentences = list()
    for sentence in sentence_tokenized_speech:
      word_tokenized_sentence = [word.lower().strip('.').strip('?').strip('!') for word in sentence.replace(",","").replace("-"," ").replace(":","").split()]
      word_tokenized_sentences.append(word_tokenized_sentence)
    word_tokenized_speeches.append(word_tokenized_sentences)
  return word_tokenized_speeches

def merge_speeches(speeches):
  all_sentences = list()
  for speech in speeches:
    for sentence in speech:
      all_sentences.append(sentence)
  return all_sentences

def get_president_sentences(president):
  files = sorted([file for file in os.listdir() if president.lower() in file.lower()])
  speeches = [read_file(file) for file in files]
  processed_speeches = process_speeches(speeches)
  all_sentences = merge_speeches(processed_speeches)
  return all_sentences

def get_presidents_sentences(presidents):
  all_sentences = list()
  for president in presidents:
    files = sorted([file for file in os.listdir() if president.lower() in file.lower()])
    speeches = [read_file(file) for file in files]
    processed_speeches = process_speeches(speeches)
    all_prez_sentences = merge_speeches(processed_speeches)
    all_sentences.extend(all_prez_sentences)
  return all_sentences

def most_frequent_words(list_of_sentences):
  all_words = [word for sentence in list_of_sentences for word in sentence]
  return Counter(all_words).most_common()
