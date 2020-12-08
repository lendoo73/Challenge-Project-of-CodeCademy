### K-NEAREST NEIGHBORS
# [K-Nearest Neighbors Classifier](https://www.codecademy.com/courses/machine-learning/lessons/knn/exercises/knn)
**K-Nearest Neighbors (KNN)** is a classification algorithm. 
The central idea is that data points with similar attributes tend to fall into similar categories.

If you have a dataset of points where the class of each point is known, you can take a new point with an unknown class, find it’s nearest neighbors, and classify it.

# [Introduction](https://www.codecademy.com/courses/machine-learning/lessons/knn/exercises/movies)
Consider a dataset of movies. 
Let’s brainstorm some features of a movie data point. 
A feature is a piece of information associated with a data point.

Let’s think about how we might want to classify a movie.
We’re going to be classifying movies as either good or bad.
In our dataset, we’ve classified a movie as good if it had an IMDb rating of 7.0 or greater.
Every “good” movie will have a class of `1`, while every bad movie will have a class of `0`.

# [Distance Between Points - 2D](https://www.codecademy.com/courses/machine-learning/lessons/knn/exercises/distance-two-d)
We need to define what it means for two points to be close together or far apart. 
To do this, we’re going to use the [Distance Formula]().
