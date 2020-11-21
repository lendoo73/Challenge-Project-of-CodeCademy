import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from sklearn.model_selection import train_test_split
from utils import load_galaxy_data

import app

from visualize import visualize_activations

input_data, labels = load_galaxy_data()
# 1. print the dimensions of the input_data and labels:
print(input_data.shape)
#print(labels.shape)

# 2. divide the data into training and validation data:
# shuffle: bool, default=True
x_train, x_test, y_train, y_test = train_test_split(
    input_data, 
    labels, 
    test_size = 0.2,
    stratify = labels,
    random_state = 222
)

# Preprocess the input
# 3. Define an ImageDataGenerator, and configure it:
training_data_generator = ImageDataGenerator(
  rescale = 1 / 255,
)
# 4. create two NumpyArrayIterators:
training_iterator = training_data_generator.flow(
  x_train, 
  y_train,
  batch_size = 5
)
BATCH_SIZE = 5
validation_iterator = training_data_generator.flow(
  x_test, 
  y_test, 
  batch_size = BATCH_SIZE
)

# 5. build your model, starting with the input shape and output layer:
model = tf.keras.Sequential()

# set the input layer:
model.add(tf.keras.Input(
  shape = input_data.shape[1:]
))

# Configuring Convolutional Layer 
# 7. filters:
# 7.1
model.add(tf.keras.layers.Conv2D(
  8, 
  3, 
  strides = 2,
  activation = "relu"
)) 
# 7.2
model.add(tf.keras.layers.MaxPooling2D(
  pool_size = (2, 2),
  strides = (2, 2)
))
# 7.3
model.add(tf.keras.layers.Conv2D(
  8, 
  3, 
  strides = 2,
  activation = "relu"
)) 
# 7.4
model.add(tf.keras.layers.MaxPooling2D(
  pool_size = (2, 2),
  strides = (2, 2)
))
# 7.5 Flatten Layer
model.add(tf.keras.layers.Flatten())
# 7.6 set the hidden layer
Dense = tf.keras.layers.Dense
model.add(Dense(
  16, 
  activation = "relu" 
))
# 7.7 set the output layer:
model.add(Dense(
  4, 
  activation = "softmax"
))

# 8: At this point, your model should have 7,164 parameters. 
#model.summary()

# 6. compile your model:
model.compile(
  loss = tf.keras.losses.CategoricalCrossentropy(), 
  optimizer = tf.keras.optimizers.Adam(learning_rate = 0.001), 
  metrics = [tf.keras.metrics.CategoricalAccuracy(), tf.keras.metrics.AUC()]
)

# Train and evaluate the classification model
# 9. train your model:
model.fit(
  training_iterator, 
  steps_per_epoch = len(training_iterator.x) / BATCH_SIZE,
  epochs = 8,
  validation_data = validation_iterator,
  validation_steps = len(validation_iterator.x) / BATCH_SIZE
)

# 12. visualize how your convolutional neural network processes images
visualize_activations(model,validation_iterator)
