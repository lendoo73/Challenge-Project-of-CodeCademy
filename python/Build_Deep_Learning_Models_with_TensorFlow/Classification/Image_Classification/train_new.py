import numpy as np
import requests
import io
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf

def make_request(filename):
  response = requests.get('https://generalzach.s3-us-west-2.amazonaws.com/'+filename)
  response.raise_for_status()
  data = np.load(io.BytesIO(response.content)) 
  return data

def load_training_data():
  print("Making request...")
  training_data = make_request('training_data_256_balanced_sample_new_500.npz')
  print("Success!")
  return training_data['a'],training_data['b']

def load_validation_data():
  print("Making request...")
  validation_data = make_request('validation_data_256_balanced_sample_new_test.npz')
  print("Success!")
  return validation_data['a'],validation_data['b']

training_data,training_labels = load_training_data()
validation_data,validation_labels = load_validation_data()

print("\nLoading training data...")

training_data_generator = ImageDataGenerator(
        rescale=1./255,
        zoom_range=0.2,
        rotation_range=15,
        width_shift_range=0.05,
        height_shift_range=0.05)

BATCH_SIZE=32

training_iterator = training_data_generator.flow(training_data,training_labels,batch_size=BATCH_SIZE)

print("\nLoading validation data...")

#1) Create validation_data_generator, an ImageDataGenerator that just performs pixel normalization:

validation_data_generator = ImageDataGenerator(rescale=1./255)

#2) Use validation_data_generator.flow_from_directory(...) to load the validation data from the 'validation_data' folder:

validation_iterator = validation_data_generator.flow(validation_data,validation_labels,batch_size=BATCH_SIZE)


print("\nBuilding model...")

#Rebuilds our model from the previous exercise, with convolutional and max pooling layers:

model = tf.keras.Sequential()
model.add(tf.keras.Input(shape=(256, 256, 1)))
model.add(tf.keras.layers.Conv2D(2, 5, strides=3, activation="relu")) 
model.add(tf.keras.layers.MaxPooling2D(
    pool_size=(5, 5), strides=(5,5)))
model.add(tf.keras.layers.Conv2D(4, 3, strides=1, activation="relu")) 
model.add(tf.keras.layers.MaxPooling2D(
    pool_size=(2,2), strides=(2,2)))
model.add(tf.keras.layers.Flatten())

model.add(tf.keras.layers.Dense(2,activation="softmax"))

model.summary()

print("\nCompiling model...")

#3) Compile the model with an Adam optimizer, Categorical Cross Entropy Loss, and Accuracy and AUC metrics:

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=5e-3),
    loss=tf.keras.losses.CategoricalCrossentropy(),
    metrics=[tf.keras.metrics.CategoricalAccuracy(),tf.keras.metrics.AUC()],
)

#4) Use model.fit(...) to train and validate our model for 2 epochs:

print("\nTraining model...")

model.fit(
        training_iterator,
        steps_per_epoch=len(training_data)/BATCH_SIZE, #training_iterator.samples/BATCH_SIZE,
        epochs=4,
       validation_data=validation_iterator,
        validation_steps=len(validation_data)/BATCH_SIZE) 
