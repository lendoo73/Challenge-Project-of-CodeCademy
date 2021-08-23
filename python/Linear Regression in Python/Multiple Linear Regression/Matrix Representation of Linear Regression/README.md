# [Matrix Representation of Linear Regression](https://www.codecademy.com/courses/linear-regression-mssp/articles/matrix-representation-of-linear-regression)

Learn about the matrix representation of the regression problem.

## Introduction

In this article we will walk through the matrix representation of the regression problem. 
While understanding the underlying math is not necessary in order to fit a regression model, 
it is useful in diagnosing problems, improving models, and working with new libraries and technologies.

## Data to Matrix transformation: Simple Linear Regression

A numerical matrix is simply a rectangular array of numbers. 
It is not difficult to see how a DataFrame already looks a lot like that. 
As an example, let’s look at a dataset from the [StreetEasy dataset](https://github.com/Codecademy/datasets/tree/master/streeteasy), 
which contains data about housing rentals in Brooklyn.
```py
import pandas as pd

df = pd.read_csv('brooklyn.csv')

#columns we're interested in
bk = df[[
    ‘rent’, 
    ‘bedrooms’,  
    ‘bathrooms’, 
    ‘size_sqft’, 
    ‘min_to_subway’, 
    ’building_age_yrs’, 
    ‘has_washer_dryer’
]]

print(bk.head(5))
```
|  |	rent |	bedrooms |	bathrooms |	size_sqft |	min_to_subway |	building_age_yrs |	has_washer_dryer |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 |	3600 |	3.0 |	2 |	900  |	4 |	15 |	0 |
| 1 |	3900 |	3.0 |	2 |	1000 |	4 |	8  |	0 |
| 2 |	2700 |	2.0 |	1 |	900  |	4 |	96 |	0 |
| 3 |	4900 |	1.0 |	1 |	1216 |	6 |	88 |	0 |
| 4 |	3900 |	0.0 |	1 |	1100 |	3 |	85 |	0 |

A quick glance at the dataset tells us that there is more than one variable that might be predictive of rental price. 
For starters, let’s focus on the apartment size. 
Suppose we fit the date with the following simple linear regression model with **slope `m`** and **intercept `b`**:
<h3 align="center">
    <em>
        rent = m ∗ size_sqft + b + error
    </em>
</h3>
This equation is actually short-hand for a large number of equations — one for each apartment in our dataset. 
The first five equations (corresponding to the first five rows of the dataset) are:
<h3 align="center">
    <em>3600 = m ∗ 900 + b + error<sub>1</sub></em><br />
    <em>3900 = m ∗ 1000 + b + error<sub>2</sub></em><br />
    <em>2700 = m ∗ 900 + b + error<sub>3</sub></em><br />
    <em>4900 = m ∗ 1216 + b + error<sub>4</sub></em><br />
    <em>3900 = m ∗ 1100 + b + error<sub>5</sub></em><br />
</h3>
When we fit this linear regression model, we are trying to find the values of *m* and *b* such that the sum of the squared error terms above 
*(eg., error_1^2 + error_2^2 + error_3^2 + error_4^2 + error_5^2 + ….)* is minimized.  

<p></p>

We create 
* a column matrix of rents (the outcome variable), 
* a column matrix of apartment sizes (the predictor variable) 
* and a column matrix of the errors

and rewrite the five equations above as one matrix equation:
<div align="center">
    <img src="formula/one_matrix_equation.jpg" />
</div>
We can do so because when we add two matrices of the same size, 
an element in one matrix gets added to the corresponding element in the other matrix that occupies the same position (row, column). 
Also, when we multiply a matrix by a constant, each element gets multiplied by it. So:
<div align="center">
    <img src="formula/m_matrix_equation.jpg" />
</div>
<div align="center">
    and similarity:<br />
    <img src="formula/b_matrix_equation.jpg" />
</div>
We can simplify this even further by combining the column of 1’s with the column of the apartment sizes (the predictor variable) into a two-column matrix. 
This works because of the following matrix algebra (this is how matrix multiplication works!):
<div align="center">
    <br />
    <img src="formula/two_column_matrix_equation.jpg" />
</div>
Therefore, the most simple version of our matrix equation look like this:
<div align="center">
    <br />
    <img src="formula/simple_two_column_matrix_equation.jpg" />
</div>
In total we have 4 matrices in this equation:
* A one-column matrix on the left hand side of the equation containing the **outcome variable** values (rent here) that we will call **y**
* A two-column matrix on the right hand side that contains a **column of 1’s** and a **column of the predictor** variable values (size_sqft here) that we will call **X**. This is also known as the **design matrix** or **X matrix**.
* A one-column matrix containing the **intercept b** and the **slope m**, i.e, the **solution matrix** that we will denote by the Greek letter **beta**. The goal of the regression problem is to evaluate this matrix.
* A one-column matrix of the residuals or errors, the error matrix. The regression problem can be solved by minimizing the sum of the squares of the elements of this matrix. The error matrix will be denoted by the Greek letter epsilon.

Using these shorthands, the matrix representation of the regression equation is thus:
<div align="center">
    <br />
    <img src="formula/matrix_representation_of_the_regression_equation.jpg" />
</div>

## Multiple Linear Regression

Now there are more factors than the size of an apartment that likely influence its rental price. 
If we want to regress on more than one of these variables, our regression equation will look as follows:
<h3 align="center">
    <em>
        rent = b<sub>0</sub> + b<sub>1</sub> * size_sqft + b<sub>2</sub> * min_to_subway + b<sub>3</sub> * has_washer_dryer + ... + error
    </em>
</h3>
We are now in the territory of Multiple Linear Regression models. 
If we denote the different predictor variables by *{x1, x2, x3, …, xm}*, their corresponding slopes by *{b1,b2,b3,.., bm}* and the intercept by *b0*, 
we can write a more general form of the above equation:
<h3 align="center">
    <em>
        y = b<sub>0</sub> + b<sub>1</sub> * x<sub>1</sub> + b<sub>2</sub> * x<sub>2</sub> + ... + b<sub>m</sub> * x<sub>m</sub> + error
    </em>
</h3>
If our dataset has n data points, we will have n such equations:
<h3 align="center">
    <em>
        y<sub>1</sub> = b<sub>0</sub> + b<sub>1</sub> * x<sub>11</sub> + b<sub>2</sub> * x<sub>21</sub> + ... + b<sub>m</sub> * x<sub>m1</sub> + error<sub>1</sub>
    </em>
    <br />
    <em>
        y<sub>2</sub> = b<sub>0</sub> + b<sub>1</sub> * x<sub>12</sub> + b<sub>2</sub> * x<sub>22</sub> + ... + b<sub>m</sub> * x<sub>m2</sub> + error<sub>2</sub>
    </em>
    <br />
    <em>
        y<sub>3</sub> = b<sub>0</sub> + b<sub>1</sub> * x<sub>13</sub> + b<sub>2</sub> * x<sub>23</sub> + ... + b<sub>m</sub> * x<sub>m3</sub> + error<sub>3</sub>
    </em>
    <br />
        ...
    <br />
    <em>
        y<sub>n/sub> = b<sub>0</sub> + b<sub>1</sub> * x<sub>1n/sub> + b<sub>2</sub> * x<sub>2n/sub> + ... + b<sub>m</sub> * x<sub>mn</sub> + error<sub>n</sub>
    </em>
</h3>
The matrix formulation for multiple linear regression thus looks as follows:


























