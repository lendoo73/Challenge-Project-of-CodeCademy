# [Classification](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-classification-track/modules/dlsp-classification/lessons/classification-neural-networks/exercises/introduction-classification-neural)
Sorting the world into categories — classifying — is an important task you do every day.
Classifying is an important task within computer science as well.
Classification is a technique to predict to which class each instance or example belongs. 
Supervised classification learns the prediction model from the labeled data. 
In this lesson, we will talk about two types of classification:
1. **Binary classification** results in a decision that is yes or no.
2. **Multi-class classification** categorizes examples in one of several categories. 

Because neural networks are very effective for high-dimensionality problems and able to model complex relationships between variables, they are often used for classification tasks.

## [1. Loading and analyzing the data](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-classification-track/modules/dlsp-classification/lessons/classification-neural-networks/exercises/loading-data-classification)
We have a dataset, stored in the train_glass.csv (training data) and test_glass.csv (test data) files, about various products made of glass. 
Using the train_glass.csv file, we want to learn a model that can predict which glass item can be constructed given the proportion of various elements such as Aluminium (Al), Magnesium (Mg), and Iron (Fe).

The following command lists all features with accompanying types about the columns:
```
import pandas as pd

data_train = pd.read_csv("train_glass.csv")
print(data_train.info())
```
```
#   Column    Non-Null Count   Dtype  
---  ------   --------------   -----  
 0   Al       300 non-null     float64
 1   Mg       300 non-null     float64 
 3   Fe       300 non-null     float64
 4   item     300 non-null     object
```
`Al`, `Mg`, and `Fe` are numeric columns, and `item` is an object column containing strings. We would like to predict the `item` column.

The following commands show us which categories we have in the item column and what their distribution is:
```
from collections import Counter

print("Classes and number of values in the dataset", Counter(data_train["item"]))
```
```
{"lamps": 75, "tableware": 125, "containers": 100}
```
Next, we need to split our data into features and labels:
```
train_x = data_train["item"]
train_y = data_train[["Al", "Mg", "Fe"]]
```

## [2. Preparing the data](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-classification-track/modules/dlsp-classification/lessons/classification-neural-networks/exercises/preparing-data-classification)
When using categorical cross-entropy needs to convert all the categorical features and labels into one-hot encoding vectors.
Previously, when we had features encoded as strings, we used the `pandas.get_dummies()` function.
This works well for features, but it’s not very usable for labels.
The problem is that `get_dummies()` creates a separate column for each category, and you cannot predict for multiple columns.

Convert the label vectors to integers ranging from 0 to the number of classes by using sklearn.preprocessing.LabelEncoder:
```
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
train_y = le.fit_transform(train_y.astype(str))
test_y = le.transform(test_y.astype(str))
```
We first fit the transformer to the training data using the `LabelEncoder.fit_transform()` method, and then fit the trained transformer to the test data using the `LabelEncoder.transform()` method.

We can print the resulting mappings with:
```
integer_mapping = {l: i for i, l in enumerate(le.classes_)}
print(integer_mapping)
```
We get the following output:
```
{"lamps": 0, "tableware": 1, "containers": 2}
```
Each category is mapped to an integer, from 0 to 2 (because we have three categories).

Now that we have labels as integers, we can use a Keras function called `to_categorical()` to convert them into one-hot-encodings — the format we need for our cross-entropy loss:
```
train_y = tensorflow.keras.utils.to_categorical(train_y, dtype = "int64")
test_y = tensorflow.keras.utils.to_categorical(test_y, dtype = "int64")
```

## [3. Designing a deep learning model for classification](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-classification-track/modules/dlsp-classification/lessons/classification-neural-networks/exercises/deep-model-classification)
Initialize a Keras Sequential model in TensorFlow:
```
from tensorflow.keras.models import Sequential

my_model = Sequential()
```

The process is the following:
* set the input layer
* set the hidden layers
* set the output layer

### Set the input layer:
```
from tensorflow.keras.layers import  InputLayer

my_model.add(
  InputLayer(
    input_shape = (data_train.shape[1],)
  )
)
```
### Set the hidden layers:
```
from tensorflow.keras.layers import Dense

my_model.add(
  Dense(
    8,                           # eight hidden units
    activation = "relu"          # uses a rectified linear unit (relu) as the activation function
  )
)
```
### Set the output layer:
For regression, we don’t use any activation function in the final layer because we needed to predict a number without any transformations. 
However, for classification, the desired output is a vector of categorical probabilities.
To have this vector as an output, we need to use the `softmax` activation function that outputs a vector with elements having values between 0 and 1 and that sum to 1 
(just as all the probabilities of all outcomes for a random variable must sum up to 1).
In the case of a binary classification problem, a `sigmoid` activation function can also be used in the output layer but paired with the `binary_crossentropy` loss.
Since we have 3 classes to predict in our glass production data, the final `softmax` layer must have 3 units:
```
my_model.add(Dense(
  3,                            # the output layer is a softmax with 3 units
  activation = "softmax")
)
```

## [4. Setting the optimizer](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-classification-track/modules/dlsp-classification/lessons/classification-neural-networks/exercises/setting-optimizer-multiclass)
1. To specify the use of cross-entropy when optimizing the model, we need to set the `loss` parameter to `categorical_crossentropy` of the `Model.compile()` method.
2. We also need to decide which metrics to use to evaluate our model. 
For classification, we usually use accuracy. 
Accuracy calculates how often predictions equal labels and is expressed in percentages.
3.  We will use Adam as our optimizer.
```
my_model.compile(
  loss = "categorical_crossentropy", 
  optimizer = "adam", 
  metrics = ["accuracy"]
)
```
We are now ready to train our model.

## [5. Train and evaluate the classification model](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-classification-track/modules/dlsp-classification/lessons/classification-neural-networks/exercises/train-evaluate-classification-model)
Train a model instance:
```
my_model.fit(
  my_data, 
  my_labels, 
  epochs = 10, 
  batch_size = 1, 
  verbose = 1        # To see the progress of the training we set verbose to true (1).
)
```
After the model is trained, we can evaluate it using the unseen test data my_test and test labels test_labels:
```
loss, acc = my_model.evaluate(
  my_test, 
  test_labels, 
  verbose = 0
)
```
We take two outputs out of the `evaluate()` function:
* the value of the loss (`categorical_crossentropy`)
* accuracy (as set in the `metrics` parameter of `compile()`).

## [6. Additional evaluation statistics](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-classification-track/modules/dlsp-classification/lessons/classification-neural-networks/exercises/evaluation-statistics)
Sometimes having only accuracy reported is not enough or adequate.
Accuracy is often used when data is balanced, meaning it contains an equal or almost equal number of samples from all the classes.
However, oftentimes data comes imbalanced.
Reporting another metric such as **F1-score** is more adequate.
To observe the F1-score of a trained model instance `my_model`, amongst other metrics, we use `sklearn.metrics.classification_report`:
```
import numpy as np
from sklearn.metrics import classification_report

yhat_classes = np.argmax(            
  my_model.predict(my_test),         # predict classes for all test cases my_test
  axis = -1
)
y_true = np.argmax(                 # convert the one-hot-encoded labels my_test_labels into the index of the class the sample belongs to. 
  my_test_labels,                   # The index corresponds to our class encoded as an integer
  axis = 1
)
print(classification_report(y_true, yhat_classes))           # use the .classification_report() method to calculate all the metrics
```

## [7. Tweak the model](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-classification-track/modules/dlsp-classification/lessons/classification-neural-networks/exercises/tweak-model)
Now that we have run our code several times, we might be wondering if the model can be further improved.
1. We can try to increase the number of epochs.
Having 20 epochs, as we previously had, is usually not enough.
Increasing the number of epochs naturally makes the learning longer, but as you probably observed, the results are often much better.
2. Other hyperparameters you might consider changing are: the batch size 


