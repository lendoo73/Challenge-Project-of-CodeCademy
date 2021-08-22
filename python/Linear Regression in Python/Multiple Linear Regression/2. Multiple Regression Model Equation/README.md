#### MULTIPLE LINEAR REGRESSION

# [Multiple Regression Model Equation](https://www.codecademy.com/courses/linear-regression-mssp/lessons/stats-multiple-linear-regression/exercises/multiple-regression-model-equation)

We often write the equation of a line in the form `y = mx + b`, where **`m`** is the **slope** of the line and **`b`** is the **y-intercept**. 
Since we will be adding at least two predictors to a multiple regression equation, it is helpful to modify our ordering and notation of this equation:

* First, we may rewrite this equation by putting the intercept term first and the slope term second.
<p align="center"><code>y = b + mx</code></p>

* Next, instead of using the names `b` and `m`, we use the names `b0` and `b1`, respectively.
<p align="center"><code>y = b<sub>0</sub> + b<sub>1</sub>x<sub>1</sub></code></p> 
 
Notice that we’ve also changed our variable name x to x1 because it is our FIRST predictor.
We are now able to add as many predictors as we need in the form
y = b_0 + b_1x_1 + b_2x_2 + ... + b_ix_iy=b 
0
​
 +b 
1
​
 x 
1
​
 +b 
2
​
 x 
2
​
 +...+b 
i
​
 x 
i
​
 
where y is the response variable, b0 is the intercept, and bi is the coefficient on the ith predictor variable.
The “slopes” (b1, b2, b3, etc.) on the variables in multiple regression are called partial regression coefficients.
While this is the proper mathematical way to write a multiple regression equation, it is often easier to write out the equation using actual variable names. For example, if we are modeling test scores (score) based on number of hours studied (hours_studied) and another variable that indicates whether a student ate breakfast (breakfast), our multiple regression equation might look like this:

\text{score} = b_0 + b_1 * \text{hours\_studied} + b_2 * \text{breakfast}score=b 
0
​
 +b 
1
​
 ∗hours_studied+b 
2
​
 ∗breakfast
Of course, after fitting our model, the intercept (b0) and coefficients (b1 and b2) could be filled in with actual numbers from the output of our regression. For instance, our final equation might have an intercept of 32.7, a coefficient of 8.5 on hours_studied, and a coefficient of 22.5 on breakfast:

\text{score} = 32.7 + 8.5*\text{hours\_studied} + 22.5*\text{breakfast}score=32.7+8.5∗hours_studied+22.5∗breakfast
Instructions

