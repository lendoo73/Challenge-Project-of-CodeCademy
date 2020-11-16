# [Cross-entropy](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-classification-track/modules/dlsp-classification/lessons/classification-neural-networks/exercises/cross-entropy)
Cross-entropy is an important concept for evaluating classification model training. 
Cross-entropy is a score that summarizes the average difference between the actual and predicted probability distributions for all classes. 
The goal is to minimize the score, with a **perfect cross-entropy value is 0**.

To calculate cross-entropy between two distributions we are using the log_loss() function in scikit-learn:
```
from sklearn.metrics import log_loss

ex_1_true = [1, 0, 0] 
ex_2_true = [0, 1, 0] 
ex_3_true = [0, 0, 1] 

ex_1_predicted = [0.7, 0.2, 0.1] 
ex_2_predicted = [0.1, 0.8, 0.1] 
ex_3_predicted = [0.2, 0.2, 0.6]

true_labels = [ex_1_true, ex_2_true, ex_3_true]
predicted_labels = [ex_1_predicted, ex_2_predicted, ex_3_predicted]

ll = log_loss(true_labels, predicted_labels)
print('Average Log Loss: %.3f' % ll)
```
