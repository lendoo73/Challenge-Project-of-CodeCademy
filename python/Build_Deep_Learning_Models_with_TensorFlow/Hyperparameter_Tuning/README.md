# [Hyperparameter Tuning](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/hyperparameter-tuning-neural/exercises/introduction-hyperparameter-tuning)
Previously, we chose certain values for the following:
* the learning rate
* number of batches
* number of epochs
* number of units per hidden layer
* activation functions.

These are all **hyperparameters**. Sometimes you start with a “hunch,” by looking at what other machine learning engineers often use in their solutions.

1. First, we split data into the following sets:
* A **training set** to fit the model by updating the parameters (weights) of a neural network model. 
* A **validation set** for checking the model’s fit. It is a biased evaluation since the model is modified based on its performance on this set. We haven’t set aside a validation set until now.
* A **test set** is used for an unbiased evaluation of the model. The test set should never be used for hyperparameter selection and tweaking! Rather, it is used to compare different models.

2. Second, we set hyperparameters to some initial values.
We fit the model to the training data and check how it performs on the validation data by looking at accuracy for classification or mean absolute error for regression. 

3. Finally, if the performance is not satisfactory, we change the hyperparameters and repeat the steps. 

Otherwise, we evaluate the final model on the test set and report the results.

Usually, machine learning engineers choose 70% of data for training, 20% for validating, and 10% for testing. But other splits are possible.

## [Manual tuning: learning rate](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/hyperparameter-tuning-neural/exercises/manual-learning-rate)
Neural networks are trained with the gradient descent algorithm and one of the most important hyperparameters in the network training is the ***learning rate***. 
The learning rate determines how big of a change you apply to the network weights as a consequence of the error gradient calculated on a batch of training data.

A larger learning rate leads to a faster learning process at a cost to be stuck in a suboptimal solution (local minimum). 
A smaller learning rate might produce a good suboptimal or global solution, but it will take it much longer to converge.
In the extremes, a learning rate too large will lead to an unstable learning process oscillating over the epochs. 
A learning rate too small may not converge or get stuck in a local minimum.

It can be helpful to test different learning rates as we change our hyperparameters. 
A learning rate of 1.0 leads to oscillations, 0.01 may give us a good performance, while 1e-07 is too small and almost nothing is learned within the allotted time.
