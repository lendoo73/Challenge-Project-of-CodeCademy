# [Perceptron](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-foundations-deep-learning-and-perceptrons/modules/perceptron/lessons/perceptron/exercises/what-is-perceptron)

Perceptrons are the building blocks of Neural Networks.

The perceptron is an artificial neuron that simulates the task of a biological neuron to solve problems through its own “sense” of the world.

The perceptron comes with its own artificial design and set of parameters, at its core, a single perceptron is trying to make a simple decision.

The perceptron can correct itself based on the result of its decision to make better decisions in the future!

If you combine a bunch of such perceptrons, you will get a neural network that can even make better decisions.

## [Representing a Perceptron](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-foundations-deep-learning-and-perceptrons/modules/perceptron/lessons/perceptron/exercises/represent-perceptron)

So the perceptron is an artificial neuron that can make a simple decision.

The perceptron has three main components:
* **inputs:** Each input corresponds to a feature. (age, height, weight, college degree...
* **weights:** Each input also has a weight which assigns a certain amount of importance to the input. If an input’s weight is large, it means this input plays a bigger role in determining the output. 
* **output:** The perceptron uses the inputs and weights to produce an output. The type of the output varies depending on the nature of the problem. 

### 1. [Weighted Sum](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-foundations-deep-learning-and-perceptrons/modules/perceptron/lessons/perceptron/exercises/weighted-sum)
How are the inputs and weights turned into an output? This is a two-step process, and the first step is finding the weighted sum of the inputs.

 The weighted sum is a number that gives a reasonable representation of the inputs:
 
 ![weighted sum formula](weighted_sum_formula.jpg)

The `x`‘s are the inputs and the `w`‘s are the weights.

`weighted_sum()`

### 2. [Activation Function](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-foundations-deep-learning-and-perceptrons/modules/perceptron/lessons/perceptron/exercises/activation-functions)
After finding the weighted sum, the second step is to constrain the weighted sum to produce a desired output.

The **activation functions** come are special functions that transform the weighted sum into a desired and constrained output.
 
If you want to train a perceptron to detect whether a point is above or below a line, you might want the output to be a `+1` or `-1` label. For this task, you can use the “sign activation function” to help the perceptron make the decision:
* If weighted sum is positive, return `+1`
* If weighted sum is negative, return `-1`

`activation()`

## [Training the Perceptron](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-foundations-deep-learning-and-perceptrons/modules/perceptron/lessons/perceptron/exercises/training-perceptron)
Right now we expect the perceptron to be very bad because it has random weights.
We can train the perceptron to produce better and better results! 
In order to do this, we provide the perceptron a training set — a collection of random inputs with correctly predicted outputs.

In the code, the training set has been represented as a dictionary with coordinates as keys and labels as values:
```
training_set = {
  (18, 49): -1, 
  (2, 17): 1, 
  (24, 35): -1, 
  (14, 26): 1, 
  (17, 34): -1
}
```

We can measure the perceptron’s actual performance against this training set.
By doing so, we get a sense of “how bad” the perceptron is.
The goal is to gradually nudge the perceptron — by slightly changing its weights — towards a better version of itself that correctly matches all the input-output pairs in the training set.
We will use these points to train the perceptron to correctly separate the positive labels from the negative labels by visualizing the perceptron as a line. 

`generate_training_set()` 

## [Training Error](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-foundations-deep-learning-and-perceptrons/modules/perceptron/lessons/perceptron/exercises/training-error)
Now that we have our training set, we can start feeding inputs into the perceptron and comparing the actual outputs against the expected labels!

Every time the output mismatches the expected label, we say that the perceptron has made a **training error** — a quantity that measures “how bad” the perceptron is performing.

The goal is to nudge the perceptron towards zero training error. The training error is calculated by subtracting the predicted label value from the actual label value:

***training error = actual label − predicted label***

For each point in the training set, the perceptron either produces a `+1` or a `-1` (as we are using the *Sign Activation Function*).
Since the labels are also a +1 or a -1, there are four different possibilities for the error the perceptron makes:
| **Actual** | **Predicted** | **Trainig Error** |
| --- | --- | --- |
| +1 | +1 | 0 |
| +1 | -1 | 2 |
| -1 | -1 | 0 |
| -1 | +1 | -2 |

These training error values will be crucial in improving the perceptron’s performance.

`training()`

## [Tweaking the Weights](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-foundations-deep-learning-and-perceptrons/modules/perceptron/lessons/perceptron/exercises/tweaking-weights)
We slowly nudge the perceptron towards a better version of itself that eventually has zero error.

The only way to do that is to change the parameters that define the perceptron. We can’t change the inputs so the only thing that can be tweaked are the weights. As we change the weights, the outputs change as well.

The goal is to find the optimal combination of weights that will produce the correct output for as many points as possible in the dataset.

### [The Perceptron Algorithm](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-foundations-deep-learning-and-perceptrons/modules/perceptron/lessons/perceptron/exercises/perceptron-algorithm)
There needs to be a way to guarantee that the perceptron improves its performance over time.
The **Perceptron Algorithm** optimally tweak the weights and nudge the perceptron towards zero error.

The most important part of the algorithm is the update rule where the weights get updated:

***weight = weight + (error ∗ input)***

We keep on tweaking the weights until all possible labels are correctly predicted by the perceptron. This means that multiple passes might need to be made through the `training_set` before the Perceptron Algorithm comes to a halt.

The `training()` method:
* `foundLine = False`: a boolean that indicates whether the perceptron has found a line to separate the positive and negative labels
* `while not foundLine`: a while loop that continues to train the perceptron until the line is found
* `total_error = 0`: to count the total error the perceptron makes in each round
* `total_error += abs(error)`: to update the total error the perceptron makes in each round

## [The Bias Weight](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-foundations-deep-learning-and-perceptrons/modules/perceptron/lessons/perceptron/exercises/bias-weight)
You have understood that the perceptron can be trained to produce correct outputs by tweaking the regular weights.

There are times when a minor adjustment is needed for the perceptron to be more accurate. This supporting role is played by the bias weight. It takes a default input value of 1 and some random weight value.

So now the weighted sum equation should look like:

![bias weight formula](bias_weight.jpg)
In the `Perceptron` constructor parameters:
* now there are 3 inputs instead of 2 (`num_inputs = 3`)
* now there are 3 weights instead of 2 (`weights = [1, 1, 1]`)

## [Representing a Line](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-foundations-deep-learning-and-perceptrons/modules/perceptron/lessons/perceptron/exercises/represent-line)
We could visualize the perceptron’s training process to gain a better understanding of what’s going on.

The weights change throughout the training process so if only we could meaningfully visualize those weights…

The weights can actually be used to represent a line! 

A line can be represented using the slope-intercept form.

 A perceptron’s weights can be used to find the slope and intercept of the line that the perceptron represents:
 * `slope = -self.weights[0] / self.weights[1]`
 * `intercept = -self.weights[2] / self.weights[1]`

## [Finding a Linear Classifier](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-foundations-deep-learning-and-perceptrons/modules/perceptron/lessons/perceptron/exercises/linear-classifier)
**The perceptron has**
* **inputs**, 
* **weights**, 
* and an **output**. 

The weights are parameters that define the perceptron and they can be used to represent a line. In other words, the perceptron can be visualized as a line.

What does it mean for the perceptron to correctly classify every point in the training set?

Theoretically, it means that the perceptron predicted every label correctly.

Visually, it means that the perceptron found a linear classifier, or a decision boundary, that separates the two distinct set of points in the training set.

# [Neural Networks](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-foundations-deep-learning-and-perceptrons/modules/perceptron/lessons/perceptron/exercises/non-linear-classifier)
There are any limits to a single perceptron?

The data points in the training set were linearly separable i.e. a single line could easily separate the two dissimilar sets of points.
What would happen if the data points were scattered in such a way that a line could no longer classify the points?

A single perceptron with only two inputs wouldn’t work for such a scenario because it cannot represent a non-linear decision boundary.

That’s when more perceptrons and features come into play!

By increasing the number of features and perceptrons, we can give rise to the **Multilayer Perceptrons**, also known as **Neural Networks**, which can solve much more complicated problems.
