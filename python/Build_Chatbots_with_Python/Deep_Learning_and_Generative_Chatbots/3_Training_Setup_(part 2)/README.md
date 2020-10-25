#### GENERATING TEXT WITH DEEP LEARNING
# [Training Setup (part 2)](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/deep-learning-and-generative-chatbots/modules/deep-learning-for-nlp/lessons/generating-text-with-deep-learning/exercises/training-setup-part-2)
At this point we need to fill out the `1`s in each vector. We can loop over each English-Spanish pair in our training sample using the features dictionaries to add a 1 for the token in question. For example, the dog sentence (`["the", "dog", "licked", "me"]`) would be split into the following matrix of vectors:
```
[
  [1, 0, 0, 0], # timestep 0 => "the"
  [0, 1, 0, 0], # timestep 1 => "dog"
  [0, 0, 1, 0], # timestep 2 => "licked"
  [0, 0, 0, 1], # timestep 3 => "me"
]
```
We use these timesteps to track where in a given document (sentence) we are.

To build out a three-dimensional NumPy matrix of one-hot vectors, we can assign a value of 1 for a given word at a given timestep in a given line:
```
matrix_name[line, timestep, features_dict[token]] = 1.
```
