# model.py
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras import Input
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.metrics import CategoricalAccuracy
from tensorflow.keras.metrics import AUC
from tensorflow.keras.callbacks import EarlyStopping

from preprocessing import create_iterator
import pprint

def design_model(training_iterator, learning_rate):
    model = Sequential()
    # set the input layer:
    model.add(Input(
        shape = training_iterator.image_shape
    ))

    # Configuring Convolutional Layer:
    model.add(Conv2D(
        5, 
        5, 
        strides = 5,
        padding = "same",
        activation = "relu"
    )) 
    model.add(Dropout(0.1))

    # Configuring Max pooling Layer:
    max_pool_2d = MaxPooling2D(
        pool_size = (2, 2),
        strides = (2, 2), 
        padding = "valid"
    )
    model.add(Dropout(0.2))
    
    model.add(Conv2D(
        3, 
        3, 
        strides = 2,
        padding = "same",
        activation = "relu"
    ))

    max_pool_2d = MaxPooling2D(
        pool_size = (2, 2),
        strides = (2, 2), 
        padding = "valid"
    )
    
    # Flatten Layer
    model.add(Flatten())
    """
    # set the hidden layer:
    model.add(Dense(
        2,                 #  hidden units
        activation = "relu" 
    ))
    model.add(Dropout(0.3))
    """
    # set the output layer:
    model.add(Dense(
        3, 
        activation = "softmax"
    ))

    model.compile(
        optimizer = Adam(learning_rate = learning_rate),
        loss = CategoricalCrossentropy(),
        metrics = [
            CategoricalAccuracy(), 
            AUC()                  # we want our AUC to be as close to 1.0 as possible
        ]
    )

    model.summary()
  
    return model

def fit_model(batch_size, learning_rate, num_epochs):
  
    print("\nLoading training data...")
    training_data_generator = ImageDataGenerator(
        rescale = 1 / 255,
        zoom_range = 0.1,
        rotation_range = 15,
        width_shift_range = 0.05,
        height_shift_range = 0.05
    )
    training_iterator = create_iterator(training_data_generator, "Covid19-dataset/train", batch_size)
    #print(training_iterator.image_shape)

    validation_data_generator = ImageDataGenerator(rescale = 1 / 255)
    print("\nLoading validation data...")
    validation_iterator = create_iterator(validation_data_generator, "Covid19-dataset/test", batch_size)

    print("\nDesign model...")
    model = design_model(training_iterator, learning_rate)

    stop = EarlyStopping(
        monitor = "val_loss", # we are monitoring the validation loss to decide when to stop the training
        mode = "min",         # we seek minimal loss
        verbose = 1, 
        patience = 40         # if the learning reaches a plateau, 
                              # it will continue for 40 more epochs in case the plateau leads to improved performance
        )

    print("\nTraining model...")
    history = model.fit(
        training_iterator,
        steps_per_epoch = training_iterator.samples / batch_size,
        epochs = num_epochs,
        verbose = 1, 
        callbacks = [stop],
        validation_data = validation_iterator,
        validation_steps = validation_iterator.samples / batch_size
    )
    
    return history, validation_iterator