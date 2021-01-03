# [Implementing Neural Networks](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/dl-neural-networks/exercises/introduction)

A neural network, just like any machine learning method, learns how to perform tasks by processing data and adjusting its model to best predict the desired outcome.
Most popular machine learning tasks are:
1. **Classification:**  given data and true labels or categories for each data point, train a model that predicts for each data example what its label should be. 
2. **Regression:** given data and true continuous value for each data point, train a model that can predict values for each data example.

Parametric models such as neural networks are described by parameters: configuration variables representing the model’s knowledge. 
We can tweak the parameters using the training data and we can evaluate the performance of the model using hold-out test data the model has not seen during training.

##  The main components of a neural network:
* ***Input data:*** this is used to train a neural network model you need to provide it with some training data.
* ***optimizer:*** this is an algorithm that based on the training data adjusts the parameters of the network in order to perform the task at hand.
* ***loss or cost function:*** this informs the optimizer whether it is doing a good job on the training data and how to adjust the parameters in the right direction.
* ***Evaluation metrics:*** these tell us how well the current model performs on validation data. 
For example, mean absolute error for regression tells us how far the predictions are on average from the true values.

## [Predicting medical costs: loading the data](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/dl-neural-networks/exercises/medical-costs-loading-the-data)
Every machine learning pipeline starts with data and a task. 
The [Medical Cost Personal Datasets dataset](https://www.kaggle.com/mirichoi0218/insurance) consists of seven columns.
| Column names | Description | Data type |
| --- | --- | --- |
| age | age of primary beneficiary | numerical / integer |
| sex | insurance contractor gender | integer (female 1, male 0) |
| bmi | body mass index | numerical / real value |
| children | number of children coverd by health insurance | numerical / integer |
| smoker | smoking or not | integer / (true 1, false 0) |
| region | the beneficiary’s residential area in the US |	categorical (northeast, northwest, southeast, southwest) |
| charges |	individual medical costs billed by health insurance |	numerical / real value |

We would like to predict the individual medical costs (charges) given the rest of the columns/features.
Since charges represent continuous values (in dollars), we’re performing a regression task. 

Our data is in the .csv format and we load it with pandas:
```
dataset = pd.read_csv('insurance.csv')
```
We split the data into features and the target variable:
```
#dataframe slicing using iloc; the first six columns:
features = dataset.iloc[:,0:6]  
# we select the last column with -1; the last (charges) column:
labels = dataset.iloc[:,-1] 
```
The pandas shape property tells us the shape of our data — a vector of two values: the number of samples and the number of features. 
```
print(“Number of features: “, features.shape[1])         # 6
print(“Number of samples: “, features.shape[0])          # 1338
```

## [Data preprocessing:](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/dl-neural-networks/exercises/dl-one-hot-encoding-standardization)
### One-hot encoding of categorical features:
Neural networks cannot work with string data directly. 
We need to convert our categorical features (“region”) into numerical. 
*One-hot encoding* creates a binary column for each category.
Since the “region” variable has four categories, the one-hot encoding will result in four binary columns: “northeast”, “northwest”, “southeast”, “southwest”.
One-hot encoding can be accomplished by using the pandas get_dummies() function:
```
features  = pd.get_dummies(features)
```

### Split data into train and test sets:
In machine learning, we train a model on a training data, and we evaluate its performance on a held-out set of data, our test set, not seen during the learning:
```
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(
  features, 
  labels, 
  test_size = 0.33,         # we chose the test size to be 33% of the total data,
  random_state = 42
)
```
### Standardize/normalize numerical features:
The usual preprocessing step for numerical variables is ***standardization*** that rescales features to zero mean and unit variance. 
Our features have different scales or units: “age” has an interval of [18, 64] and the “children” column’s interval is much smaller, [0, 5].
By having features with differing scales, the optimizer might update some weights faster.

***Normalization*** is another way of preprocessing numerical data:
it scales the numerical features to a fixed range - usually between 0 and 1.

To normalize the numerical features we use `scikit-learn`, `ColumnTransformer`, in the following way:
```
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.compose import ColumnTransformer
 
ct = ColumnTransformer(
  [(
    "normalize", 
    Normalizer(), 
    ["age", "bmi", "children"]        # only numerical columns applies to the Normalizer()
  )], 
  remainder = "passthrough"           # ... the rest of the columns
)
features_train = ct.fit_transform(features_train)     
features_test = ct.transform(features_test)        
```
`ColumnTransformer()` returns NumPy arrays and we convert them back to a pandas DataFrame.
```
features_train_norm = pd.DataFrame(
  features_train_norm, 
  columns = features_train.columns
)
```

## [Neural network model: tf.keras.Sequential](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/dl-neural-networks/exercises/neural-network-sequential)
Now that we have our data preprocessed we can start building the neural network model.
A sequential model allows us to create models layer-by-layer in a step-by-step fashion.
This model can have only one input tensor and only one output tensor.

Import Sequential from keras.models:
```
from tensorflow.keras.models import Sequential
```
We will design the model in a separate Python function called `design_model()`.

Initializes a Sequential model instance `my_model`:
```
def design_model(features):
  model = Sequential(name = "my first model")               # name is an optional argument to any model in Keras
  .
  .
  .
  return model
```
We invoke our function in the main program with:
```
model = design_model(features_train)
```
The model’s layers are accessed via the layers attribute:
```
print(model.layers)       # (The list of layers is still empty, we will add layers to our model later.)
```

## [Neural network model: layers](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/dl-neural-networks/exercises/neural-network-layers)
Layers are the building blocks of neural networks and can contain 1 or more neurons.
Each layer is associated with parameters: weights, and bias, that are tuned during the learning.
A fully-connected layer in which all neurons connect to all neurons in the next layer is created the following way in TensorFlow:
```
from tensorflow.keras import layers

# we chose 3 neurons here
layer = layers.Dense(3) 
```
We chose to create a layer with three neurons, the number of outputs of this layer is 3.
The bias parameter would be a vector of (3, 1) dimensions. 
But what is the first dimension of the weights matrix?
```
print(layer.weights)                                 # we get an empty array since no input layer is specified.
```
```
# 13388 samples, 11 features as in our dataset
input = tf.ones((1338, 11))
# a fully-connected layer with 3 neurons
layer = layers.Dense(3) 
# calculate the outputs
output = layer(input) 
# print the weights
print(layer.weights)                                 # the weight matrix has shape = (11, 3)
```
TensorFlow will determine the shapes of the weight matrix and bias matrix automatically the moment it encounters the first input.

## [Neural network model: input layer](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/dl-neural-networks/exercises/neural-network-input-layer)
In Keras, an input for a neural network can be specified with a `tf.keras.layers.InputLayer` object.

The following code initializes an input layer for a DataFrame my_data that has 15 columns:
```
from tensorflow.keras.layers import InputLayer

my_input = InputLayer(input_shape = (15,))
```
The input_shape parameter has to have its first dimension equal to the number of features in the data. 
You don’t need to specify the second dimension: the number of samples or batch size.

The following code avoids hard-coding with using the .shape property of the my_data DataFrame:
```
#get the number of features/dimensions in the data
num_features = my_data.shape[1] 
my_input = InputLayer(input_shape = (num_features,)) 
```

Now add this input layer to a model instance:
```
model.add(my_input)
print(model.summary()) 
```
The summary shows that the total number of parameters is 0.
This shows you that the input layer has no trainable parameters and is just a placeholder for data.

## [Neural network model: output layer](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/dl-neural-networks/exercises/neural-network-output-layer)
The output layer shape depends on your task. In the case of regression, we need one output for each sample. 
If your data has 100 samples, you would expect your output to be a vector with 100 entries - a numerical prediction for each sample.

We are doing regression and wish to predict one number for each data point: the medical cost billed by health insurance indicated in the `charges` column in our data.

Add a layer with one neuron to a model:
```
from tensorflow.keras.layers import Dense

model.add(Dense(1))
```
You don’t need to specify the input shape of this layer since Tensorflow with Keras can automatically infer its shape from the previous layer.

## [Neural network model: hidden layers](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/dl-neural-networks/exercises/neural-network-hidden-layers)
We have added one input layer and one output layer to our model.
Our model. If you think about it, our model currently represents a linear regression.
To capture more complex or non-linear interactions among the inputs and outputs neural networks, we’ll need to incorporate hidden layers.

Add a hidden layer to a model instance my_model:
```
from tensorflow.keras.layers import Dense

my_model.add(
  Dense(
    64, 
    activation = "relu"       # Rectified Linear Unit activation function
  )
)
```
We chose 64 (2 ** 6) to be the number of neurons since it makes optimization more efficient due to the binary nature of computation.
With the activation parameter, we specify which activation function we want to have in the output of our hidden layer. 

Adding more layers to a neural network naturally increases the number of parameters to be tuned.
With every layer, there are associated weight and bias vectors.

The 1st layer’s weight matrix has shape (11, 64) because we feed 11 features to 64 hidden neurons. 
The output layer has the weight matrix of shape (64, 1) because we have 64 input units and 1 neuron in the final layer.

## [Optimizers](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/dl-neural-networks/exercises/dl-optimizers)
Our goal is for the network to effectively adjust its weights or parameters in order to reach the best performance.
Keras offers a variety of optimizers such as `SGD` (Stochastic Gradient Descent optimizer), `Adam`, `RMSprop`, and others.

Introducing the Adam optimizer:
```
from tensorflow.keras.optimizers import Adam

opt = Adam(learning_rate = 0.01)
```
The learning rate determines how big of jumps the optimizer makes in the parameter space (weights and bias) and it is considered a hyperparameter that can be also tuned. 
While model parameters are the ones that the model uses to make predictions, hyperparameters determine the learning process (learning rate, number of iterations, optimizer type).

If the learning rate is set too high, the optimizer will make large jumps and possibly miss the solution. 
If set too low, the learning process is too slow and might not converge to a desirable solution with the allotted time.
We’ll use a value of 0.01, which is often used.

A model instance my_model is compiled with the following code:
```
my_model.compile(
  loss = "mse",  
  metrics = ["mae"], 
  optimizer = opt
)
```
**`loss`** denotes the measure of learning success; the lower the loss the better the performance. The most often used loss function is the Mean Squared Error `mse` (the average squared difference between the estimated values and the actual value).

We want to observe the progress of the Mean Absolute Error (`mae`) while training the model because MAE can give us a better idea than `mse` on how far off we are from the true values in the units we are predicting.
We are predicting `charge` in dollars and MAE will tell us how many dollars we’re off, on average, from the actual values as the network is being trained.

## [Training and evaluating the model](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-getting-started-with-tensorflow/modules/dlsp-implementing-neural-networks/lessons/dl-neural-networks/exercises/training-evaluating-model)
Now that we built the model we are ready to train the model using the training data.

Trains a model instance `model` using training data features_train and training labels labels_train:
```
model.fit(
  features_train,         # the training data set
  labels_train,           # true labels for the training data points
  epochs = 40,            # refers to the number of cycles through the full training dataset; 
                          # Since training of neural networks is an iterative process, you need multiple passes through data. 
  batch_size = 1,         # the number of data points to work through before updating the model parameters; It is also a hyperparameter that can be tuned.
  verbose = 1             # will show you the progress bar of the training
)
```
When the training is finalized, we use the trained model to predict values for samples that the training procedure haven’t seen: the test set.

Evaluate the model on the test data:
```
val_mse, val_mae = model.evaluate(
  features_test, 
  labels_test, 
  verbose = 0
)

print("MAE: ", val_mae)
```
`model.evaluate()` returns the value for our chosen loss metrics (`mse`) and for an additional metrics (`mae`).
