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


