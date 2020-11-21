from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf

BATCH_SIZE = 16

print("\nLoading training data...")

training_data_generator = ImageDataGenerator(
        rescale = 1 / 255,
        zoom_range = 0.2,
        rotation_range = 15,
        width_shift_range = 0.05,
        height_shift_range = 0.05
)

training_iterator = training_data_generator.flow_from_directory('data/train',class_mode='categorical',color_mode='grayscale',batch_size=BATCH_SIZE)


print("\nLoading validation data...")

#1) Create validation_data_generator, an ImageDataGenerator that just performs pixel normalization:
validation_data_generator = ImageDataGenerator(
  rescale = 1 / 255
)

#2) Use validation_data_generator.flow_from_directory(...) to load the validation data from the 'data/test' folder:
validation_iterator = validation_data_generator.flow_from_directory(
  "data/test",
  class_mode = "categorical",
  color_mode = "grayscale",
  batch_size = BATCH_SIZE
)


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
  optimizer = tf.keras.optimizers.Adam(learning_rate = 0.005),
  loss = tf.keras.losses.CategoricalCrossentropy(),
  metrics = [
    tf.keras.metrics.CategoricalAccuracy(), 
    tf.keras.metrics.AUC()
  ]
)

print("\nTraining model...")

#4) Use model.fit(...) to train and validate our model for 5 epochs:

model.fit(
  training_iterator,
  steps_per_epoch = training_iterator.samples / BATCH_SIZE,
  epochs = 5,
  validation_data = validation_iterator,
  validation_steps = validation_iterator.samples / BATCH_SIZE
)
