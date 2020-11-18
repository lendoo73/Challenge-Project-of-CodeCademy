import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report

from collections import Counter

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, InputLayer
from tensorflow.keras.utils import to_categorical

# Loading the data

# 1. load the data from heart_failure.csv:
data = pd.read_csv("heart_failure.csv")
# 2. print all the columns and their types:
#data.info()
#print(data.columns)

# 3. Print the distribution of the death_event column:
print("Classes and number of values in the dataset", Counter(data["death_event"]))

# 4. Extract the label column death_rate from the data DataFrame and assign the result to a variable called y.
y = data["death_event"]

# 5. Extract the features columns:
X = data[['age','anaemia','creatinine_phosphokinase','diabetes','ejection_fraction','high_blood_pressure','platelets','serum_creatinine','serum_sodium','sex','smoking','time']]

# Data preprocessing

# 6. Convert the categorical features to one-hot encoding vectors:
X = pd.get_dummies(X)
#X.info()

# 7. split the data into training features, test features, training labels, and test labels:
X_train, X_test, Y_train, Y_test = train_test_split(
    X, 
    y, 
    test_size = 0.33,         # we chose the test size to be 33% of the total data,
    random_state = 42
)

# 8. Initialize a ColumnTransformer object:
numerical_features = X.select_dtypes(
    include = ['float64', 'int64']
)
numerical_columns = numerical_features.columns
ct = ColumnTransformer(
    [(
        "numeric", 
        StandardScaler(), 
        numerical_columns 
    )]
)

# 9. train the scaler instance ct on the training data:
X_train = ct.fit_transform(X_train)

# 10. scale the test data
X_test = ct.transform(X_test)

# Prepare labels for classification

# 11. Initialize an instance of LabelEncoder
le = LabelEncoder()
# 12. Fit the encoder instance
Y_train = le.fit_transform(Y_train.astype(str))

# 13. Encode the test labels
Y_test = le.transform(Y_test.astype(str))

# 14. transform the encoded training labels Y_train into a binary vector
Y_train = to_categorical(Y_train)

# 15. transform the encoded test labels Y_test into a binary vector
Y_test = to_categorical(Y_test)

# Design the model
# 16. Initialize a mode
model = Sequential()

# 17. Create an input layer instance
model.add(
  InputLayer(
    input_shape = (X_train.shape[1], )
  )
)

# 18. Create a hidden layer
model.add(
  Dense(
    12,
    activation = "relu"
  )
)

# 19. Create an output layer
model.add(
  Dense(
    2,
    activation = "softmax"
  )
)

# 20. compile the model
model.compile(
  loss = "categorical_crossentropy",
  optimizer = "adam",
  metrics = ["accuracy"]
)

# Train and evaluate the model
# 21. fit the model
model.fit(
  X_train,
  Y_train,
  epochs = 100,
  batch_size = 16,
  verbose = 1
)

# 22. evaluate the trained model
loss, acc = model.evaluate(
  X_test,
  Y_test,
  verbose = 0
)
print("Loss: ", loss, "Accuracy: ", acc)

# 23-24. get the predictions
y_estimate = np.argmax(
  model.predict(X_test),
  axis = -1
)

# 25. select the indices of the true classes for each label
y_true = np.argmax(
  Y_test,
  axis = 1
)

# 26. Print additional metrics
print(classification_report(y_true, y_estimate))

