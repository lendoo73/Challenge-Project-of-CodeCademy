####  Supervised Learning

# [K-Nearest Neighbors Classifier](https://github.com/lendoo73/Challenge-Project-of-CodeCademy/tree/master/python/Learn_the_Basics_of_Machine_Learning/Classification_K_Nearest_Neighbors/K_Nearest_Neighbors)

# [K-Nearest Neighbor Regressor](https://www.codecademy.com/paths/machine-learning/tracks/introduction-to-supervised-learning-skill-path/modules/k-nearest-neighbors-skill-path/lessons/ml-knn-regression/exercises/regression)

## [Regression](https://www.codecademy.com/paths/machine-learning/tracks/introduction-to-supervised-learning-skill-path/modules/k-nearest-neighbors-skill-path/lessons/ml-knn-regression/exercises/regression)

The K-Nearest Neighbors algorithm is a powerful supervised machine learning algorithm typically used for classification. 
However, it can also perform regression.

Instead of classifying a new movie as either good or bad, we are now going to predict its IMDb rating as a real number.

This process is almost identical to classification, except for the final step. 
We are going to find the `k` nearest neighbors of the new movie by using the distance formula. 
However, instead of counting the number of good and bad neighbors, the regressor averages their IMDb ratings.

For example, if the three nearest neighbors to an unrated movie have ratings of `5.0`, `9.2`, and `6.8`, then we could predict that this new movie will have a rating of `7.0`.
#### `(5 + 9.2 + 6.8) / 3 = 7`
```
  sum_rating = 0
  for neighbor in neighbors:
    title = neighbor[1]
    sum_rating += movie_ratings[title]
    avg_rating = sum_rating / k
```

## [Weighted Regression](https://www.codecademy.com/paths/machine-learning/tracks/introduction-to-supervised-learning-skill-path/modules/k-nearest-neighbors-skill-path/lessons/ml-knn-regression/exercises/weighted-regression)

We can be even more clever in the way that we compute the average.
We can compute a weighted average based on how close each neighbor is.

Let’s say we’re trying to predict the rating of movie X and we’ve found its three nearest neighbors:
| Movie | Rating | Distance to movie X |
| :----:  |:------:| :-------------------:|
| A     | 5.0    | 3.2                 |
| B     | 6.8    | 11.5                |
| C     | 9.0    | 1.1                 |


