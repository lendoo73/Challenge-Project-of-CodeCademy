#### HYPERPARAMETER TUNING
## [Regularization: dropout](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/hyperparameter-tuning-neural/exercises/regularization-dropout)
Regularization is a set of techniques that prevent the learning process to completely fit the model to the training data which can lead to overfitting.
It makes the model simpler, smooths out the learning curve, and hence makes it more ‘regular’. 
There are many techniques for regularization such as simplifying the model, adding weight regularization, weight decay, and so on. 
The most common regularization method is dropout.

**Dropout** is a technique that randomly ignores, or “drops out” a number of outputs of a layer by setting them to zeros. 
The dropout rate is the percentage of layer outputs set to zero (usually between 20% to 50%).
In Keras, we can add a dropout layer by introducing the Dropout layer.

Let’s recreate our overfitting network having too many layers and too many neurons per layer in the `design_model_no_dropout()` method.
The validation error gets worse, which indicates the trend of overfitting.

Next, we introduce dropout layers in the `design_model_dropout()` method:
```
model.add(input)
model.add(layers.Dense(128, activation = 'relu'))
model.add(layers.Dropout(0.1))
model.add(layers.Dense(64, activation = 'relu'))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(24, activation = 'relu'))
model.add(layers.Dropout(0.3))
model.add(layers.Dense(1))
```
