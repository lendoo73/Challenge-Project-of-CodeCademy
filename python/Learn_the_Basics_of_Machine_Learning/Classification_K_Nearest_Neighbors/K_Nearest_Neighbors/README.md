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

We’ll implement the three steps of the K-Nearest Neighbor Algorithm:
* Normalize the data
* Find the k nearest neighbors
* Classify the new point based on those neighbors

# [1. Data with Different Scales: Normalization](https://www.codecademy.com/courses/machine-learning/lessons/knn/exercises/normalize)
When we added the dimension of budget, you might have realized there are some problems with the way our data currently looks.

The maximum difference between two movies’ release dates is about 125 years (The Lumière Brothers were making movies in the 1890s).
However, the difference between two movies’ budget can be millions of dollars.

The problem is that the distance formula treats all dimensions equally, regardless of their scale. The difference in one year is exactly equal to the difference in one dollar of budget.

The solution to this problem is to [normalize the data](https://github.com/lendoo73/Challenge-Project-of-CodeCademy/tree/master/python/Learn_the_Basics_of_Machine_Learning/Classification_K_Nearest_Neighbors/Normalization) so every value is between 0 and 1.
We’re going to be using *min-max normalization*.
```
def min_max_normalize(lst):
  minimum = min(lst)
  maximum = max(lst)
  normalized = []

  return [(val - minimum) / (maximum - minimum) for val in lst]
```
# [2. Finding the Nearest Neighbors](https://www.codecademy.com/courses/machine-learning/lessons/knn/exercises/find-neighbors)
Now that our data has been normalized and we know how to find the distance between two points, we can begin classifying unknown data!

We want to find the k nearest neighbors of the unclassified point.

In order to find the 5 nearest neighbors, we need to compare this new unclassified movie to every other movie in the dataset.
This means we’re going to be using the distance formula again and again.
We ultimately want to end up with a sorted list of distances and the movies associated with those distances.

# [3. Count Neighbors](https://www.codecademy.com/courses/machine-learning/lessons/knn/exercises/count-neighbors)
We’ve now found the k nearest neighbors, and have stored them in a list.

Our goal now is to count the number of good movies and bad movies in the list of neighbors. 
If more of the neighbors were good, then the algorithm will classify the unknown movie as good. Otherwise, it will classify it as bad.

In order to find the class of each of the labels, we’ll need to look at our `movie_labels` dataset. For example, `movie_labels['Akira']` would give us `1` because Akira is classified as a good movie.
```
def classify(unknown, dataset, labels, k):
  distances = []

  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]
  
  num_good = 0
  num_bad = 0

  for movie in neighbors:
    title = movie[1]
    if labels[title] == 0:
      num_bad += 1
    else:
      num_good +=1
  return 1 if num_good > num_bad else 0
```

# [Training and Validation Sets](https://www.codecademy.com/courses/machine-learning/lessons/knn/exercises/training-and-validation)
We now need to report how effective our algorithm is.

As with most machine learning algorithms, we have split our data into a training set and validation set.

Once these sets are created, we will want to use every point in the validation set as input to the K Nearest Neighbor algorithm.
We will take a movie from the validation set, compare it to all the movies in the training set, find the K Nearest Neighbors, and make a prediction.
After making that prediction, we can then peek at the real answer (found in the validation labels) to see if our classifier got the answer correct.

If we do this for every movie in the validation set, we can count the number of times the classifier got the answer right and the number of times it got it wrong.
Using those two numbers, we can compute the validation accuracy.

Validation accuracy will change depending on what K we use.

# [Choosing K](https://www.codecademy.com/courses/machine-learning/lessons/knn/exercises/choosing-k)
The validation accuracy changes as k changes.
The first situation that will be useful to consider is when k is very small.
Let’s say `k = 1`. We would expect the validation accuracy to be fairly low due to *overfitting*. 
Overfitting occurs when you rely too heavily on your training data; you assume that data in the real world will always behave exactly like your training data.
In the case of K-Nearest Neighbors, overfitting happens when you don’t consider enough neighbors.
A single outlier could drastically determine the label of an unknown point.
Our classifier has relied too heavily on the small quirks in the training data.

If k is very large, our classifier will suffer from *underfitting*.
Underfitting occurs when your classifier doesn’t pay enough attention to the small quirks in the training set.
```
def find_validation_accuracy(training_set, training_labels, validation_set, validation_labels, k):

  num_correct = 0

  for title in validation_set:
    guess = classify(validation_set[title], training_set, training_labels, k)
    num_correct += 1 if guess == validation_labels[title] else 0

  validation_error = num_correct / len(validation_set)

  return validation_error 
```

# [Using sklearn](https://www.codecademy.com/courses/machine-learning/lessons/knn/exercises/sklearn)
`sklearn` is a Python library specifically used for Machine Learning.

First, you need to create a KNeighborsClassifier object.
The code below will create a classifier where k = 3:
```
from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors = 3)
```
Next, we’ll need to train our classifier.
The `.fit()` method takes two parameters: 
* The first is a list of points, 
* and the second is the labels associated with those points.

Finally, after training the model, we can classify new points. 
The `.predict()` method takes a list of points that you want to classify. 
It returns a list of its guesses for those points.
