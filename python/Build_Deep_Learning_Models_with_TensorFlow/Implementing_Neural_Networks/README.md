# [Implementing Neural Networks](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/dl-neural-networks/exercises/introduction)
A neural network, just like any machine learning method, learns how to perform tasks by processing data and adjusting its model to best predict the desired outcome.
Most popular machine learning tasks are:
1. **Classification:**  given data and true labels or categories for each data point, train a model that predicts for each data example what its label should be. 
2. **Regression:** given data and true continuous value for each data point, train a model that can predict values for each data example.

Parametric models such as neural networks are described by parameters: configuration variables representing the model’s knowledge. 
We can tweak the parameters using the training data and we can evaluate the performance of the model using hold-out test data the model has not seen during training.

##  The main components of a neural network:
* ***Input data:*** this is used to train a neural network model you need to provide it with some training data.
* ***optimizer:*** this is an algorithm that based on the training data adjusts the parameters of the network in order to perform the task at hand.
* ***loss or cost function:*** this informs the optimizer whether it is doing a good job on the training data and how to adjust the parameters in the right direction.
* ***Evaluation metrics:*** these tell us how well the current model performs on validation data. 
For example, mean absolute error for regression tells us how far the predictions are on average from the true values.

## [Predicting medical costs: loading the data](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/dl-neural-networks/exercises/medical-costs-loading-the-data)
Every machine learning pipeline starts with data and a task. 
The [Medical Cost Personal Datasets dataset](https://www.kaggle.com/mirichoi0218/insurance) consists of seven columns.
| Column names | Description | Data type |
| --- | --- | --- |
| age | age of primary beneficiary | numerical / integer |
| sex | insurance contractor gender | integer (female 1, male 0) |
| bmi | body mass index | numerical / real value |
| children | number of children coverd by health insurance | numerical / integer |
| smoker | smoking or not | integer / (true 1, false 0) |
| region | the beneficiary’s residential area in the US |	categorical (northeast, northwest, southeast, southwest) |
| charges |	individual medical costs billed by health insurance |	numerical / real value |

We would like to predict the individual medical costs (charges) given the rest of the columns/features.
Since charges represent continuous values (in dollars), we’re performing a regression task. 

Our data is in the .csv format and we load it with pandas:
```
dataset = pd.read_csv('insurance.csv')
```
We split the data into features and the target variable:
```
#dataframe slicing using iloc; the first six columns:
features = dataset.iloc[:,0:6]  
# we select the last column with -1; the last (charges) column:
labels = dataset.iloc[:,-1] 
```
The pandas shape property tells us the shape of our data — a vector of two values: the number of samples and the number of features. 
```
print(“Number of features: “, features.shape[1])         # 6
print(“Number of samples: “, features.shape[0])          # 1338
```

## [Data preprocessing: one-hot encoding and standardization](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/dl-neural-networks/exercises/dl-one-hot-encoding-standardization)



