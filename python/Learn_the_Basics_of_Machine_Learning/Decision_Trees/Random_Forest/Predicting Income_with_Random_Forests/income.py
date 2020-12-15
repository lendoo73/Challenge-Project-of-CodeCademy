def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

# Investigate The Data
income_data = pd.read_csv(
  "income.csv",
  header = 0,
  delimiter = ", "
)
#print(income_data.iloc[0])
print(income_data.info())
#print(set(income_data["marital-status"]))
#print(income_data["marital-status"].value_counts())

def factorize(column):
  return pd.factorize(column)[0] + 1

def string_to_01(data, column, string):
  return data[column].apply(lambda row: 0 if row == string else 1)

income_data["sex-int"] = string_to_01(income_data, "sex", "Male")

income_data["country-int"] = string_to_01(income_data, "native-country", "United-States")

income_data["workclass-int"] = string_to_01(income_data, "workclass", "Private")

income_data["education-int"] = factorize(income_data["education"])

income_data["marital-status-int"] = factorize(income_data["marital-status"])

# Format The Data For Scikit-learn
labels = income_data.income
data = income_data[[
  #"fnlwgt",
  #"age", 
  "education-int",
  "capital-gain", 
  "capital-loss", 
  "hours-per-week",
  "sex-int",
  "marital-status-int",
  #"country-int",
  "workclass-int"
]]
#print(data.info())
#print(set(income_data["sex-int"]))

train_data, test_data, train_labels, test_labels = train_test_split(
  data, 
  labels,
  random_state = 1
)

# Create The Random Forest
forest = RandomForestClassifier(
  random_state = 1
)
forest.fit(train_data, train_labels)

print(forest.feature_importances_)
print(forest.score(test_data, test_labels))
