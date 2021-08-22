#### MULTIPLE LINEAR REGRESSION

# [Multiple Regression Model Equation](https://www.codecademy.com/courses/linear-regression-mssp/lessons/stats-multiple-linear-regression/exercises/multiple-regression-model-equation)

We often write the equation of a line in the form `y = mx + b`, where **`m`** is the **slope** of the line and **`b`** is the **y-intercept**. 
Since we will be adding at least two predictors to a multiple regression equation, it is helpful to modify our ordering and notation of this equation:
<ul>
    <li>
        First, we may rewrite this equation by putting the intercept term first and the slope term second.
        <p><code>y = b + mx</code></p>
    </li>
    <li>
        Next, instead of using the names `b` and `m`, we use the names `b0` and `b1`, respectively.
        <p><code>y = b<sub>0</sub> + b<sub>1</sub>x<sub>1</sub></code></p>
        Notice that we’ve also changed our variable name `x` to `x1` because it is our FIRST predictor.
    </li>
    <li>
        We are now able to add as many predictors as we need in the form
        <p><code>y = b<sub>0</sub> + b<sub>1</sub>x<sub>1</sub> + b<sub>2</sub>x<sub>2</sub> ... + b<sub>i</sub>x<sub>i</sub></code></p>
        where `y` is the response variable, `b0` is the intercept, and `bi` is the coefficient on the `i`th predictor variable.
    </li>
    <li>
        The “slopes” (**`b1`, `b2`, `b3`**, etc.) on the variables in multiple regression are called **partial regression coefficients**.
    </li>
</ul>

While this is the proper mathematical way to write a multiple regression equation, it is often easier to write out the equation using actual variable names. 
For example, if we are modeling test scores (`score`) based on number of hours studied (`hours_studied`) 
and another variable that indicates whether a student ate breakfast (`breakfast`), our multiple regression equation might look like this:
<h4>
    <p>score = b<sub>0</sub> + b<sub>1</sub> * hours_studied + b<sub>2</sub> * breakfast</p>
</h4>

Of course, after fitting our model, the intercept (b0) and coefficients (b1 and b2) could be filled in with actual numbers from the output of our regression. For instance, our final equation might have an intercept of 32.7, a coefficient of 8.5 on hours_studied, and a coefficient of 22.5 on breakfast:

\text{score} = 32.7 + 8.5*\text{hours\_studied} + 22.5*\text{breakfast}score=32.7+8.5∗hours_studied+22.5∗breakfast
Instructions

