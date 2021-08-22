#### MULTIPLE LINEAR REGRESSION

# [Quantitative Variables in Multiple Regression](https://www.codecademy.com/courses/linear-regression-mssp/lessons/stats-multiple-linear-regression/exercises/quantitative-variables-in-multiple-regression)

In the previous exercises, we looked at regression models with one quantitative predictor and one binary predictor, but we can also have models with multiple quantitative predictors. For example, consider the following model using the survey dataset (assignments is the number of homework assignments the student has completed):

import statsmodels.api as sm
model = sm.OLS.from_formula('score ~ hours_studied + assignments', data=survey).fit()
print(model.params)
 
# Output:
# Intercept        16.676498
# hours_studied     6.273886
# assignments       4.687796
From the coefficients above, our regression equation is:

\text{score} = 16.7 + 6.3*\text{hours\_studied} + 4.7*\text{assignments}score=16.7+6.3∗hours_studied+4.7∗assignments
We can still think of multiple regression as creating a new regression line for each value of a quantitative predictor. However, it is challenging to visualize this because we now have different regression lines for every possible value of assignments. To visualize the regression output, it is helpful to choose a few sample values: for example, 1, 5, and 10 assignments.

We can add these lines to our scatter plot of score vs. hours_studied as before:

import seaborn as sns
import matplotlib.pyplot as plt
 
# Create scatter plot of hours_studied and score
sns.lmplot(x='hours_studied', y='score', hue='assignments', palette='Blues', fit_reg=False, data=survey)
This time we will directly put the model coefficients into each regression equation by calling them individually from model.params. The code for 1, 5, and 10 assignments is given below.

# Add regression line for 1 assignment
plt.plot(survey.hours_studied, model.params[0] + model.params[1]*survey.hours_studied + model.params[2]*1, color='lightblue',linewidth=5)
 
# Add regression line for 5 assignments
plt.plot(survey.hours_studied, model.params[0] + model.params[1]*survey.hours_studied + model.params[2]*5, color='blue',linewidth=5)
 
# Add regression line for 10 assignments
plt.plot(survey.hours_studied, model.params[0] + model.params[1]*survey.hours_studied + model.params[2]*10, color='darkblue',linewidth=5)
 
# Show plot with legend
plt.legend(['assignments=1','assignments=5', 'assignments=10'])
plt.show()
Scatter plot showing hours studied on the x-axis and score on the y-axis. Three parallel lines each show a positive relationship between score and hours studied for 1, 5, and 10 assignments. The intercepts of the lines start higher as the number of assignments increases.

We can see in the plot that the slopes of all three lines are the same, but the intercepts differ. As the number of completed assignments increases, the intercept of the corresponding regression line also increases.
