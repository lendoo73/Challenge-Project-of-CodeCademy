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
