#### HYPERPARAMETER TUNING
## [Manual tuning: batch size](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/hyperparameter-tuning-neural/exercises/tuning-batch-size)
The batch size is a hyperparameter that determines how many training samples are seen before updating the network’s parameters (weight and bias matrices).

When the batch contains all the training examples, the process is called *batch gradient descent*.

If the batch has one sample, it is called the *stochastic gradient descent*.

When 1 < batch size < number of training points, is called *mini-batch gradient descent*.

An advantage of using batches is for GPU computation that can parallelize neural network computations.

A larger batch size will provide our model with better gradient estimates and a solution close to the optimum, but this comes at a cost of computational efficiency and good generalization performance.

A smaller batch size is a poor estimate of the gradient, but the learning is performed faster. 

For this experiment, we fix the learning rate to 0.01 and try the following batch sizes: 1, 2, 10, and 16.
Want to improve the performance with a larger batch size? A good trick is to increase the learning rate!
