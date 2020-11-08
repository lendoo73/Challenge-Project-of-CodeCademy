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

### [Weighted Sum](https://www.codecademy.com/paths/build-deep-learning-models-with-tensorflow/tracks/dlsp-foundations-deep-learning-and-perceptrons/modules/perceptron/lessons/perceptron/exercises/weighted-sum)
How are the inputs and weights turned into an output? This is a two-step process, and the first step is finding the weighted sum of the inputs.

 The weighted sum is a number that gives a reasonable representation of the inputs:
