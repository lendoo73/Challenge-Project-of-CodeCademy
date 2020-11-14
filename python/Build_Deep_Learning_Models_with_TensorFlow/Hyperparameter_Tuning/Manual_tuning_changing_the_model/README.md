#### HYPERPARAMETER TUNING
## [Manual tuning: changing the model](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/hyperparameter-tuning-neural/exercises/tuning-changing-model)

If you have a big model and you train too long, you might overfit. Let us see the opposite - having a too simple model.

we compare a one-layer neural network and a model with a single hidden layer. The models look like this:
```
def one_layer_model(X, learning_rate):
   ...
   model.add(input) 
   model.add(layers.Dense(1))
   ...
```
```
def more_complex_model(X, learning_rate):
    ...
    model.add(input)
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
```

For the model with no hidden layers the validation curve is below the training curve.
This means that the training curve can get better at some point, but the model complexity doesn’t allow it. 
This phenomenon is called ***underfitting***.
You can also notice that no early stopping occurs here since the performance of this model is bad all the time.

For the model with a single hidden layer a well-behaving curve with the early stopping at epoch 38 and we have a much better result. 

How do we choose the number of hidden layers and the number of units per layer?

Start with one hidden layer and add as many units as we have features in the dataset. 
However, this might not always work. 
We need to try things out and observe our learning curve.

