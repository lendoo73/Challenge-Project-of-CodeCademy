## [Using a validation set for hyperparameter tuning](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/hyperparameter-tuning-neural/exercises/validation-hyperparam-tuning)
In TensorFlow Keras, validation split can be specified as a parameter in the .fit() function:
```
my_model.fit(
  data, 
  labels, 
  epochs = 20, 
  batch_size = 1, 
  verbose = 1,  
  validation_split = 0.2       # a float between 0 and 1, denoting a fraction of the training data to be used as validation data.
)
```
In the example above, 20% of the data would be allocated for validation.
