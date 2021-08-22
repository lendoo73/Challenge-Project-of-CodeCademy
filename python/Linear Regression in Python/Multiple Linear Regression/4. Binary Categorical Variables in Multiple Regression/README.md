#### MULTIPLE LINEAR REGRESSION

# [Binary Categorical Variables in Multiple Regression](https://www.codecademy.com/courses/linear-regression-mssp/lessons/stats-multiple-linear-regression/exercises/binary-categorical-variables-in-multiple-regression)

Binary categorical variables are variables with exactly two possible values. 
In a regression model, these two values are generally coded as 1 or 0. 
For example, a multiple regression equation from the `survey` dataset might look like this:


\text{score} = 32.7 + 8.5*\text{hours\_studied} + 22.5* \text{breakfast}score=32.7+8.5∗hours_studied+22.5∗breakfast
breakfast is a binary categorical predictor with two possible values: “ate breakfast,” which is coded as 1 in the model and “didn’t eat breakfast,” which is coded as 0. If we substitute these values for breakfast in the regression equation, we end up with two equations: one for each group.

For breakfast eaters, we substitute 1 for breakfast and simplify:

\begin{aligned} \text{score} = 32.7 + 8.5*\text{hours\_studied} + 22.5*\bm{1}& \\ \text{score} = 32.7 + 8.5*\text{hours\_studied} + 22.5& \\ \text{score} = (32.7 + 22.5) + 8.5*\text{hours\_studied}& \\ \text{score} = 55.2 + 8.5*\text{hours\_studied}& \\ \end{aligned} 
score=32.7+8.5∗hours_studied+22.5∗1
score=32.7+8.5∗hours_studied+22.5
score=(32.7+22.5)+8.5∗hours_studied
score=55.2+8.5∗hours_studied
​
  
​
 
For the group that didn’t eat breakfast, we substitute 0 for breakfast and simplify:

\begin{aligned} \text{score} = 32.7 + 8.5*\text{hours\_studied} + 22.5*\bm{0}& \\ \text{score} = 32.7 + 8.5*\text{hours\_studied} + 0& \\ \text{score} = 32.7 + 8.5*\text{hours\_studied}& \\ \end{aligned} 
score=32.7+8.5∗hours_studied+22.5∗0
score=32.7+8.5∗hours_studied+0
score=32.7+8.5∗hours_studied
​
  
​
 
If we inspect these two equations, we see that the only difference is the larger intercept for the group that ate breakfast (55.2) compared to the group that didn’t eat breakfast (32.7). The coefficient on hours_studied is the same for both groups.

We can visualize this regression equation by adding both lines to the scatter plot of score and hours_studied with plt.plot() as follows:

import seaborn as sns
import matplotlib.pyplot as plt
 
sns.lmplot(x='hours_studied', y='score', hue='breakfast', markers=['o', 'x'], fit_reg=False, data=survey)
plt.plot(survey.hours_studied, 42.2+8.7*survey.hours_studied, color='blue',linewidth=5)
plt.plot(survey.hours_studied, 49.7+8.7*survey.hours_studied, color='orange',linewidth=5)
plt.show()
Plot showing hours studied on the x-axis and score on the y-axis. Two parallel regression lines run in a positive direction over the scatter plot: the line for the group that didn't eat breakfast starts at a lower intercept than the line for the group that did eat breakfast.

From the plot, we can see the regression lines have the same slope. The orange line for the breakfast-eaters starts higher, but increases at the same rate as the blue line for the group that didn’t eat breakfast.
