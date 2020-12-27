#### ACCURACY, RECALL, PRECISION, AND F1 SCORE

# [Accuracy](https://www.codecademy.com/paths/machine-learning/tracks/introduction-to-supervised-learning-skill-path/modules/accuracy-recall-and-precision-skill-path/lessons/ml-accuracy/exercises/accuracy)

After creating a machine learning algorithm capable of making classifications, the next step in the process is to calculate its predictive power.
In order to calculate these statistics, we’ll need to split our data into a [training set and validation set](https://www.codecademy.com/content-items/ced99a64b810eda769bc48293550fd21).

Let’s say you’re using a machine learning algorithm to try to predict whether or not you will get above a B on a test. 
The features of your data could be something like:
* The number of hours you studied this week.
* The number of hours you watched Netflix this week.
* The time you went to bed the night before the test.
* Your average in the class before taking the test.

The simplest way of reporting the effectiveness of an algorithm is by calculating its accuracy.
Accuracy is calculated by finding the total number of correctly classified points and dividing by the total number of points.

![accuracy formula](images/accuracy_formula.jpg)

Let’s define those terms in the context of our grade example:
* True Positive: The algorithm predicted you would get above a B, and you did.
* True Negative: The algorithm predicted you would get below a B, and you did.
* False Positive: The algorithm predicted you would get above a B, and you didn’t.
* False Negative: The algorithm predicted you would get below a B, and you didn’t.

# [Recall](https://www.codecademy.com/paths/machine-learning/tracks/introduction-to-supervised-learning-skill-path/modules/accuracy-recall-and-precision-skill-path/lessons/ml-accuracy/exercises/recall)

Accuracy can be an extremely misleading statistic depending on your data. 
Consider the example of an algorithm that is trying to predict whether or not there will be over 3 feet of snow on the ground tomorrow. 
We can write a pretty accurate classifier right now: always predict False. 
This classifier will be incredibly accurate — there are hardly ever many days with that much snow. 
But this classifier never finds the information we’re actually interested in.

In this situation, the statistic that would be helpful is **recall**. Recall measures the percentage of relevant items that your classifier found. In this example, recall is the number of snow days the algorithm correctly predicted divided by the total number of snow days:

![recall formula](images/recall_formula.jpg)

