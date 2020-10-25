#### GENERATING TEXT WITH DEEP LEARNING
# [Training Setup (part 2)](https://www.codecademy.com/paths/build-chatbots-with-python/tracks/deep-learning-and-generative-chatbots/modules/deep-learning-for-nlp/lessons/generating-text-with-deep-learning/exercises/training-setup-part-2)
At this point we need to fill out the 1s in each vector. We can loop over each English-Spanish pair in our training sample using the features dictionaries to add a 1 for the token in question. For example, the dog sentence (["the", "dog", "licked", "me"]) would be split into the following matrix of vectors:
