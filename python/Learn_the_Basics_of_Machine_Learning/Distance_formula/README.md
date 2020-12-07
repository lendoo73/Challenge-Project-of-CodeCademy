# 
## [Representing Points](https://www.codecademy.com/courses/machine-learning/lessons/distance-formula/exercises/points)
In this lesson, you will learn three different ways to define the distance between two points:
1. Euclidean Distance
2. Manhattan Distance
3. Hamming Distance

In this exercise, we will use a list, where each item in the list represents a dimension of the point: `pt1 = [5, 8]`
Points aren’t limited to just two dimensions: a five-dimensional point could be represented as `[4, 8, 15, 16, 23]`.

Ultimately, we want to find the distance between two points.
We can only find the difference between two points if they have the same number of dimensions!

## [Euclidean Distance](https://www.codecademy.com/courses/machine-learning/lessons/distance-formula/exercises/euclidean-distance)
To find the Euclidean distance between two points, we first calculate the squared distance between each dimension.
If we add up all of these squared differences and take the square root, we’ve computed the Euclidean distance.

![Euclidean formula](eucledian_formula.jpg)

