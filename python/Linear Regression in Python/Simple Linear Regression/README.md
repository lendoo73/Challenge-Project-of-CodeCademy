#### INTRODUCTION TO LINEAR REGRESSION

# [Introduction to Linear Regression](https://www.codecademy.com/courses/linear-regression-mssp/lessons/introduction-to-linear-regression/exercises/introduction-to-linear-regression)

Linear regression is a powerful modeling technique that can be used to understand the relationship between a quantitative variable and one or more other variables, 
sometimes with the goal of making predictions. 
For example, linear regression can help us answer questions like:
* What is the relationship between apartment size and rental price for NYC apartments?
* Is a mother’s height a good predictor of their child’s adult height?

The first step before fitting a linear regression model is exploratory data analysis and data visualization: is there a relationship that we can model? 
For example, suppose we collect heights (in cm) and weights (in kg) for 9 adults and inspect a plot of height vs. weight:
```py
plt.scatter(data.height, data.weight)
plt.xlabel('height (cm)')
plt.ylabel('weight (kg)')
plt.show()
```

![height vs. weight](images/height_weight_scatter.svg)

Scatter plot showing a positive linear relationship between height and weight (people who are taller tend to weigh more)

When we look at this plot, we see that there is some evidence of a relationship between height and weight: people who are taller tend to weigh more. 
In the following exercises, we’ll learn how to model this relationship with a line. 
If you were to draw a line through these points to describe the relationship between height and weight, what line would you draw?

# [Equation of a Line](https://www.codecademy.com/courses/linear-regression-mssp/lessons/introduction-to-linear-regression/exercises/equation-of-a-line)

Like the name implies, LINEar regression involves fitting a line to a set of data points. 
In order to fit a line, it’s helpful to understand the equation for a line, which is often written as y = mx + b. 
In this equation:
* x and y represent variables, such as height and weight or hours of studying and quiz scores.
* b represents the y-intercept of the line. This is where the line intersects with the y-axis (a vertical line located at x = 0).
* m represents the slope. This controls how steep the line is. If we choose any two points on a line, the slope is the ratio between the vertical and horizontal distance between those points; this is often written as rise/run.

The following plot shows a line with the equation y = 2x + 12:

![equation y = 2x + 12](images/equation_of_line.svg)

image showing a line with a point at the y-axis (a vertical line where the x-variable is equal to zero) labeled "y-intercept." 
The line also has two other points, which are connected by a horizontal and vertical dashed line, labeled "run" and "rise," respectively. 
The slope is calculated as rise/run which is equal to 2 in this example.

Note that we can also have a line with a negative slope. 
For example, the following plot shows the line with the equation y = -2x + 8:

![equation y = -2x + 8](images/equation_of_line_negslope.svg)

image showing a line with a point at the y-axis (a vertical line where the x-variable is equal to zero) labeled "y-intercept." 
The line also has two other points, which are connected by a horizontal and vertical dashed line, labeled "run" and "rise," respectively. 
The slope is calculated as rise/run which is equal to -2 in this example.

