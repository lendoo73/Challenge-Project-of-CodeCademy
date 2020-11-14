#### HYPERPARAMETER TUNING
## [Manual tuning: learning rate](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/hyperparameter-tuning-neural/exercises/manual-learning-rate)
Neural networks are trained with the gradient descent algorithm and one of the most important hyperparameters in the network training is the ***learning rate***. 
The learning rate determines how big of a change you apply to the network weights as a consequence of the error gradient calculated on a batch of training data.

A larger learning rate leads to a faster learning process at a cost to be stuck in a suboptimal solution (local minimum). 
A smaller learning rate might produce a good suboptimal or global solution, but it will take it much longer to converge.
In the extremes, a learning rate too large will lead to an unstable learning process oscillating over the epochs. 
A learning rate too small may not converge or get stuck in a local minimum.

It can be helpful to test different learning rates as we change our hyperparameters. 
A learning rate of 1.0 leads to oscillations, 0.01 may give us a good performance, while 1e-07 is too small and almost nothing is learned within the allotted time.
