import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.compose import ColumnTransformer

df = pd.read_csv("admissions_data.csv")
#print(df.head())

df = df.drop(columns = ["Serial No."])
#print(df.describe())

labels = df.iloc[:, -1]
#print(labels)

feature = df.iloc[:, : -1]
#print(feature)

# there are no categorical variables in this dataset, so do not have to perform one-hot encoding.

features_train, features_test, labels_train, labels_test = train_test_split(
    feature, 
    labels, 
    test_size = 0.33,
    random_state = 42
)

numerical_features = feature.select_dtypes(
    include = ['float64', 'int64']
)
numerical_columns = numerical_features.columns

ct = ColumnTransformer(
    [(
        "only numeric", 
        StandardScaler(), 
        numerical_columns 
    )], 
    remainder = "passthrough"
)

features_train_scaled = ct.fit_transform(features_train)
features_test_scaled = ct.transform(features_test)

features_train_norm = pd.DataFrame(
  features_train_scaled, 
  columns = features_train.columns
)
#print(features_train_norm)

def design_model(X, learning_rate):
    layers = tf.keras.layers
    Dense = tf.keras.layers.Dense

    model = tf.keras.models.Sequential()
    input = layers.InputLayer(input_shape = (X.shape[1], ))
    model.add(input)
    
    model.add(
        Dense(
            7, 
            activation = "relu" 
        )
    )

    model.add(Dense(1))
    #print(model.summary())

    opt = tf.keras.optimizers.Adam(learning_rate = learning_rate)
    model.compile(
        loss = "mse",  
        metrics = ["mae"], 
        optimizer = opt
    )

    return model

def fit_model(num_epochs):
    model = design_model(features_train_scaled, learning_rate)
    stop = tf.keras.callbacks.EarlyStopping(
        monitor = "val_loss", 
        mode = "min",
        verbose = 1, 
        patience = 40 
    )
    history = model.fit(
        features_train_scaled,
        labels_train,
        epochs = num_epochs,
        batch_size = 16,
        verbose = 0,
        validation_split = 0.2,        #  20% of the data would be allocated for validation
        callbacks = [stop]
    )
    
    return history
