# [Random Forest](https://www.codecademy.com/courses/machine-learning/lessons/ml-random-forest/exercises/random-forest)

Decision trees can be powerful supervised machine learning models. 
However, decision trees are often prone to overfitting.

We’ve discussed some strategies to minimize this problem, like pruning, but sometimes that isn’t enough.
We need to find another way to generalize our trees. 

A *random forest* is an ensemble machine learning technique — a random forest contains many decision trees that all work together to classify new points.
When a random forest is asked to classify a new point, the random forest gives that point to each of the decision trees.
Each of those trees reports their classification and the random forest returns the most popular classification.
It’s like every tree gets a vote, and the most popular classification wins.

Some of the trees in the random forest may be overfit, but by making the prediction based on a large number of trees, overfitting will have less of an impact.

# [Bagging](https://www.codecademy.com/courses/machine-learning/lessons/ml-random-forest/exercises/bagging-i)

Our [algorithm for creating a decision tree](https://github.com/lendoo73/Challenge-Project-of-CodeCademy/tree/master/python/Learn_the_Basics_of_Machine_Learning/Decision_Trees) 
is deterministic — given a training set, the same tree will be made every time.

Random forests create different trees using a process known as ***bagging***.
