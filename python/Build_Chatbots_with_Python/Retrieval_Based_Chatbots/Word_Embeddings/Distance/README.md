# [Distance](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/retrieval-based-chatbots/modules/nlp-word-embeddings/lessons/word-embeddings/exercises/distance)
The key at the heart of word embeddings is distance.

There are a variety of ways to find the distance between vectors.

## Manhattan distance (city block distance)
Defined as the sum of the differences across each individual dimension of the vectors.

![manhattan formula](manhattan_formula.jpg)

manhattan distance between x, y three-dimenzional vector:

vector x = [1, 2, 3]

vector y = [2, 4, 6]

manhattan distance = |1 - 2| + |2 - 4| + |3 - 6| = 1 + 2 + 3 = 6

## Euclidean distance (straight line distance)
With this distance metric, we take the square root of the sum of the squares of the differences in each dimension.

#### *One* dimension
*d(x, y) = |x - y|* 

#### *n* dimension
![eucledian formula](eucledian_formula.jpg)

