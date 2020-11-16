# [Classification](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-classification-track/modules/dlsp-classification/lessons/classification-neural-networks/exercises/introduction-classification-neural)
Sorting the world into categories — classifying — is an important task you do every day.
Classifying is an important task within computer science as well.
Classification is a technique to predict to which class each instance or example belongs. 
Supervised classification learns the prediction model from the labeled data. 
In this lesson, we will talk about two types of classification:
1. **Binary classification** results in a decision that is yes or no.
2. **Multi-class classification** categorizes examples in one of several categories. 

Because neural networks are very effective for high-dimensionality problems and able to model complex relationships between variables, they are often used for classification tasks.

# 1. Loading and analyzing the data
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
