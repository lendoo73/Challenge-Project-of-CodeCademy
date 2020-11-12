import pandas as pd
import tensorflow
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

tensorflow.random.set_seed(35) #for the reproducibility of results

def design_model(features):
  model = Sequential(name = "my_first_model")
  #without hard-coding
  input = InputLayer(input_shape=(features.shape[1],)) 
  #add the input layer
  model.add(input) 
  #add a hidden layer with 64 neurons
  model.add(Dense(128, activation='relu')) 
  #add an output layer to our model
  model.add(Dense(1)) 
  opt = Adam(learning_rate=0.1)
  model.compile(
    loss = 'mse',  
    metrics = ['mae'], 
    optimizer = opt
  )

  return model

dataset = pd.read_csv('insurance.csv') #load the dataset
features = dataset.iloc[:,0:6] #choose first 7 columns as features
labels = dataset.iloc[:,-1] #choose the final column for prediction

features = pd.get_dummies(features) #one-hot encoding for categorical variables
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.33, random_state=42) #split the data into training and test data
 
#standardize
ct = ColumnTransformer([('standardize', StandardScaler(), ['age', 'bmi', 'children'])], remainder='passthrough')
features_train = ct.fit_transform(features_train)
features_test = ct.transform(features_test)

#invoke the function for our model design
model = design_model(features_train)
print(model.summary())

#fit the model using 40 epochs and batch size 1
model.fit(
  features_train, 
  labels_train, 
  epochs = 40, 
  batch_size = 1, 
  verbose = 1
)

#evaluate the model on the test data
val_mse, val_mae = model.evaluate(features_test, labels_test, verbose = 0)
 
print("MAE: ", val_mae)
