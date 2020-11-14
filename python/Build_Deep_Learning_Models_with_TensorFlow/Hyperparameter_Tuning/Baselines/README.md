#### HYPERPARAMETER TUNING
## [Baselines: how to know the performance is reasonable?](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/hyperparameter-tuning-neural/exercises/baselines-neural-network)
A baseline result is the simplest possible prediction.
For some problems, this may be a random result, and for others, it may be the most common class prediction.
Since we are focused on a regression task in this lesson, we can use averages or medians of the class distribution known as central tendency measures as the result for all predictions.
Scikit-learn provides `DummyRegressor`, which serves as a baseline regression algorithm.
```
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error

dummy_regr = DummyRegressor(strategy = "mean")                   # We choose mean (average) as our central tendency measure
dummy_regr.fit(features_train, labels_train)
y_pred = dummy_regr.predict(features_test)
MAE_baseline = mean_absolute_error(labels_test, y_pred)
print(MAE_baseline)
```
