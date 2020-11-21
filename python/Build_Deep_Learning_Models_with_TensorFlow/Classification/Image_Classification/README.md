# [Introduction to Image Classification](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-classification-track/modules/dlsp-image-classification/lessons/image-classification/exercises/introduction-to-image-classification)
Neural networks are perfectly suited for image classification.
The task of finding the complex patterns in pixels necessary to map an image to its label.
As a result, image classification is a common application of deep learning.

# [Preprocessing Image Data](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-classification-track/modules/dlsp-image-classification/lessons/image-classification/exercises/preprocessing-image-data)
Our goal is to pass these X-ray images into our network, and to classify them according to their respective labels.
At a high-level, this is very similar to our approach for classifying non-image data.

Now, our features are going to come from image pixels.
Each image will be 256 pixels tall and 256 pixels wide, and each pixel has a value between 0 (black) - 255 (white).

![X-ray image](xray_diagram_labeled.png)

We can use `ImageDataGenerator` to load images from a file path, and to preprocess them. 
```
my_image_data_generator = ImageDataGenerator()
```
The ImageDataGenerator can also preprocess our data.
We do this by passing additional arguments to the constructor.

The most important step is the *pixel normalization*.
Because neural networks struggle with large integer values, we want to rescale our raw pixel values between `0` and `1`.
Our pixels have values in `[0,255]`, so we can normalize pixels by dividing each pixel by `255.0`.

We can also use our ImageDataGenerator for `data augmentation`: generating more data without collecting any new images.
A common way to augment image data is to flip or randomly shift each image by small amounts.
Because our dataset is only a few hundred images, we’ll also use the `ImageDataGenerator` to randomly shift images during training.

For example, we can define another ImageDataGenerator and set its vertical_flip parameter to be True.
```
my_augmented_image_data_generator = ImageDataGenerator(vertical_flip = True)
```
If we use this ImageDataGenerator to load images, it will randomly flip some of those images upside down.

# [Loading Image Data](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-classification-track/modules/dlsp-image-classification/lessons/image-classification/exercises/loading-image-data)
Now, we can use the ImageDataGenerator object that we just created to load and batch our data:
```
training_iterator = training_data_generator.flow_from_directory(
  "my_data_directory",
  class_mode = "categorical",
  color_mode = "rgb,
  target_size = (128, 128),
  batch_size = 32
)
```
* `directory`: A string that defines the path to the folder containing our training data.
* `class_mode`: How we should represent the labels in our data. “For example, we can set this to `"categorical"` to return our labels as one-hot arrays, with a `1` in the correct class slot.
* `color_mode`: Specifies the type of image. For example, we set this to `"grayscale"` for black and white images, or to `"rgb"` (Red-Green-Blue) for color images.
* `target_size`: A tuple specifying the height and width of our image. Every image in the directory will be resized into this shape.
* `batch_size`: The batch size of our data.

The resulting `training_iterator` variable is a `DirectoryIterator` object. We can pass this object directly to `model.fit()` to train our model on our training data.

# [Modifying our Feed-Forward Classification Model](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-classification-track/modules/dlsp-image-classification/lessons/image-classification/exercises/modifying-our-feed-forward-classification-model)
One way to classify image data is to treat an image as a vector of pixels.

To do this, we need to:
1. Change the shape of our input layer model to accept our image data. Now, our input shape will be (`image height`, `image width`, `image channels`). 
For example, if our data were composed of 512x512 pixel RGB images, we add an input shape as follows:
```
model.add(tf.keras.Input(shape = (512, 512, 3)))
```
2. Add a `Flatten()` layer to “flatten” our input image into a single vector.
`Flatten()` layer allows us to preserve the batch size of data, but combine the other dimensions of the image (height, width, image channels) into a single, lengthy feature vector.
We can then pass this output to a `Dense()` layer.
```
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense( ... ))
```

# [A Better Alternative: Convolutional Neural Networks](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-classification-track/modules/dlsp-image-classification/lessons/image-classification/exercises/a-better-alternative-convolutional-neural-networks)
*Convolutional Neural Networks (CNNs)* use layers specifically designed for image data. 
These layers capture local relationships between nearby features in an image.

Previously, in our feed-forward model, we multiplied our normalized pixels by a large weight matrix (of shape (65536, 100)) to generate our next set of features.

However, when we use a convolutional layer, we learn a set of smaller weight tensors, called *filters* (also known as *kernels*).
We move each of these filters (i.e. convolve them) across the height and width of our input, to generate a new “image” of features.
Each new “pixel” results from applying the filter to that location in the original image.

## Why do convolution-based approaches work well for image data?
* Convolution can reduce the size of an input image using only a few parameters.
* Filters compute new features by only combining features that are near each other in the image. 
This operation encourages the model to look for local patterns (e.g., edges and objects).
* Convolutional layers will produce similar outputs even when the objects in an image are translated.
This is because the same filters are applied across the entire image.

## [Configuring a Convolutional Layer - Filters](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-classification-track/modules/dlsp-image-classification/lessons/image-classification/exercises/configuring-a-convolutional-layer-filters)
In Keras, we can define a `Conv2D` layer to handle the forward and backward passes of convolution.
```
#Defines a convolutional layer with 4 filters, each of size 5 by 5:ó
model.add(tf.keras.layers.Conv2D(
  4, 
  5, 
  activation = "relu"
))  
```
When defining a convolutional layer, we can specify the number and size of the filters that we convolve across each image.

### Number of Filters
When using convolutional layers, we don’t just convolve one filter.
We convolve each of these in turn to produce a new set of features. 
Then we stack these outputs (one for each filter) together in a new “image.”

Our output tensor is then (`batch_size`, `new height`, `new width`, `number of filters`).
We call this last dimension number of channels ( or feature maps ). 
These are the result of applying a single filter across the entire image.

### Filter Size
Each filter has three dimensions: `[Height, Width, Input Channels]`
* Height: the height of our filter (in pixels)
* Width: the width of our filter (also in pixels)
* Input Channels: The number of input channels. 
  * In a black and white image, there is 1 input channel (grayscale). 
  * In an RGB image, there are three input channels. 
We don’t have control over this dimension, Keras takes care of this last dimension for us.

Increasing height or width increases the number of pixels that a filter can pay attention to at each step in the convolution. 
However, doing so also increases the number of learnable parameters. 
People commonly use filters of size 5x5 and 3x3.  
In total, the number of parameters in a convolution layer is:   
  *Number of filters × (Input Channels × Height × Width + 1)*

