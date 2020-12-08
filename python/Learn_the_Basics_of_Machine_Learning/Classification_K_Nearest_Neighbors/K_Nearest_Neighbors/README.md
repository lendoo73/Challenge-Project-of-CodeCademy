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
To do this, we’re going to use the [Distance Formula](https://github.com/lendoo73/Challenge-Project-of-CodeCademy/tree/master/python/Learn_the_Basics_of_Machine_Learning/Classification_K_Nearest_Neighbors/Distance_formula).

For this example, the data has two dimensions:
* The length of the movie
* The movie’s release date

Consider Star Wars and Raiders of the Lost Ark. 
Star Wars is 125 minutes long and was released in 1977. 
Raiders of the Lost Ark is 115 minutes long and was released in 1981.

The distance between the movies is computed below:
![formula](ST_RotLA.jpg)

# [Distance Between Points - 3D](https://www.codecademy.com/courses/machine-learning/lessons/knn/exercises/distance-three-d)
Making a movie rating predictor based on just the length and release date of movies is pretty limited. 
There are so many more interesting pieces of data about movies that we could use! So let’s add another dimension.

Let’s say this third dimension is the movie’s budget.
We now have to find the distance between these two points in three dimensions.

What if we’re not happy with just three dimensions?

The generalized distance formula between points `x` and `y` is as follows:

![eucledian formula](../Distance_formula/eucledian_formula.jpg)

Using this formula, we can find the K-Nearest Neighbors of a point in N-dimensional space!
We now can use as much information about our movies as we want.
```
[(movie1[i] - movie2[i]) ** 2 for i in range(len(movie1))]) ** 0.5
```
