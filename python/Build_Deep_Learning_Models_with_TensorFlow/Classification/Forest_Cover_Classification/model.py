import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input   Layer
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping

df = pd.read_csv("drive/MyDrive/Forest Cover Classification/cover_data.csv")
feature = df.iloc[:, : -1]
labels = df.iloc[:, -1]
features_train, features_test, labels_train, labels_test = train_test_split(
    feature, 
    labels, 
    test_size = 0.2,
    random_state = 42,
    stratify = labels
)
scaler = StandardScaler()

features_train_scaled = scaler.fit_transform(features_train)
features_test_scaled = scaler.transform(features_test)

def design_model(learning_rate):

    model = Sequential()
    # Set the input layer:
    model.add(InputLayer(input_shape = (features_train_scaled.shape[1],)))
    
    # Set the hidden layers:
    model.add(Dense(256, activation = "relu"))
    model.add(Dense(128, activation = "relu"))
    #model.add(Dropout(0.1))
    model.add(Dense(64, activation = "relu"))
    model.add(Dense(32, activation = "relu"))
    model.add(Dense(16, activation = "relu"))
    model.add(Dense(8, activation = "relu"))
    # Set the output layer:
    model.add(Dense(8, activation = "softmax"))
    opt = Adam(learning_rate = learning_rate)
    model.compile(
        loss = "sparse_categorical_crossentropy",  
        metrics = ["accuracy"], 
        optimizer = opt
    )

    model.summary()
    return model

def fit_model(learning_rate, num_epochs, batch_size):
    model = design_model(learning_rate)
    stop = EarlyStopping(
        monitor = "val_accuracy", 
        mode = "auto",
        verbose = 1, 
        patience = 10 
    )
    history = model.fit(
        features_train,
        labels_train,
        epochs = num_epochs,
        batch_size = batch_size,
        verbose = 1,
        validation_split = 0.1,        #  10% of the data would be allocated for validation
        callbacks = [stop]
    )
    return history, features_test, labels_test
