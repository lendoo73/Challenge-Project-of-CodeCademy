#### GENERATING TEXT WITH DEEP LEARNING
# [Build and Train seq2seq](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/deep-learning-and-generative-chatbots/modules/deep-learning-for-nlp/lessons/generating-text-with-deep-learning/exercises/build-and-train-seq-2-seq)
We define the seq2seq model using the Model() function we imported from Keras.

To make it a seq2seq model, we feed it the encoder and decoder inputs, as well as the decoder output:
```
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
```
Our model is ready to train. First, we compile everything. Keras models demand two arguments to compile:
* An optimizer (we’re using RMSprop, which is a fancy version of the widely-used gradient descent) to help minimize our error rate (how bad the model is at guessing the true next word given the previous words in a sentence).
* A loss function (we’re using the logarithm-based cross-entropy function) to determine the error rate.

Because we care about accuracy, we’re adding that into the metrics to pay attention to while training.
```
model.compile(
  optimizer='rmsprop', 
  loss='categorical_crossentropy',
  metrics=['accuracy']
)
```
Next we need to fit the compiled model. To do this, we give the `.fit()` method the encoder and decoder input data (what we pass into the model), the decoder target data (what we expect the model to return given the data we passed in), and some numbers we can adjust as needed:
* **batch size** (smaller batch sizes mean more time, and for some problems, smaller batch sizes will be better, while for other problems, larger batch sizes are better)
* the number of **epochs** or cycles of training (more epochs mean a model that is more trained on the dataset, and that the process will take more time)
* validation split (what percentage of the data should be set aside for validating — and determining when to stop training your model — rather than training)

Keras will take it from here to get you a nicely trained seq2seq model:
```
model.fit(
  [encoder_input_data, decoder_input_data], 
  decoder_target_data,
  batch_size=10,
  epochs=100,
  validation_split=0.2
)
```
