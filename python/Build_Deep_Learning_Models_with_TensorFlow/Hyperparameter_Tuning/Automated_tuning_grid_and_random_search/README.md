#### HYPERPARAMETER TUNING
## [Towards automated tuning: grid and random search](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/hyperparameter-tuning-neural/exercises/automated-tuning-grid-random-search)
There are some strategies for automated hyperparameter tuning.

***Grid search, or exhaustive search***, tries every combination of desired hyperparameter values.
If we want to try learning rates of 0.01 and 0.001 and batch sizes of 10, 30, and 50, grid search will try six combinations of parameters (0.01 and 10, 0.01 and 30, 0.01 and 50, 0.001 and 10, and so on). 
This obviously gets very computationally demanding when we increase the number of values per hyperparameter or the number of hyperparameters we want to tune.

***Random Search*** goes through random combinations of hyperparameters and doesn’t try them all.

### Grid search in Keras
To use `GridSearchCV` from scikit-learn for regression we need to first wrap our neural network model into a `KerasRegressor`:
```
model = KerasRegressor(build_fn = design_model)
```
Then we need to setup the desired hyperparameters grid :
```
batch_size = [10, 40]
epochs = [10, 50]
param_grid = dict(batch_size = batch_size, epochs = epochs)
```
Finally, we initialize a GridSearchCV object and fit our model to the data:
```
grid = GridSearchCV(
  estimator = model, 
  param_grid = param_grid, 
  scoring = make_scorer(                   # we initialized the scoring parameter with scikit-learn’s .make_scorer() method
    mean_squared_error, 
    greater_is_better = False
  )
)
grid_result = grid.fit(features_train, labels_train, verbose = 0)
```
We’re evaluating our hyperparameter combinations with a mean squared error making sure that `greater_is_better` is set to `False` since we are searching for a set of hyperparameters that yield us the smallest error.


