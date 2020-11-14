import tensorflow as tf
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import Normalizer
import matplotlib.pyplot as plt

tf.random.set_seed(42) #for reproducibility of result we always use the same seed for random number generator
dataset = pd.read_csv("insurance.csv") #read the dataset
dataset.to_csv("test.csv", index = False)

def design_model(X, learning_rate):  #our function to design the model
    model = Sequential(name="my_first_model")
    input = tf.keras.Input(shape=(X.shape[1],))
    model.add(input)
    model.add(layers.Dense(64, activation='relu')) #addinf one hidden layer
    model.add(layers.Dense(1))
    opt = tf.keras.optimizers.Adam(learning_rate = learning_rate) #setting the learning rate of Adam to the one specified in the function parameter
    model.compile(loss='mse', metrics=['mae'], optimizer=opt)
    return model

features = dataset.iloc[:,0:6] #choose first 7 columns as features
labels = dataset.iloc[:,-1] #choose the final column for prediction
features = pd.get_dummies(features) #one hot encoding for categorical variables
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.33, random_state=42)

#standardize
ct = ColumnTransformer([('standardize', StandardScaler(), ['age', 'bmi', 'children'])], remainder='passthrough')
features_train = ct.fit_transform(features_train) #gives numpy arrays
features_test = ct.transform(features_test) #gives numpy arrays
