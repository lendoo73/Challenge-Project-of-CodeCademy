# Term frequency-inverse document frequency
Term frequency-inverse document frequency is a numerical statistic used to indicate how important a word is to each document in a collection of documents, or a corpus.

When applying tf-idf to a corpus, each word is given a tf-idf score for each document, representing the relevance of that word to the particular document.
A higher tf-idf score indicates a term is more important to the corresponding document.

Tf-idf has many similarities with the bag-of-words language model, which if you recall is concerned with word count — how many times each word appears in a document.

While tf-idf can be used in any situation bag-of-words can be used, there is a key difference in how it is calculated.

Tf-idf relies on two different metrics in order to come up with an overall score:
* ***term frequency***: how often a word appears in a document. This is the same as bag-of-words’ word count.
* ***inverse document frequency***: a measure of how often a word appears in the overall corpus.

tf-idf can give better insight into how important a word is to a particular document of a corpus.
