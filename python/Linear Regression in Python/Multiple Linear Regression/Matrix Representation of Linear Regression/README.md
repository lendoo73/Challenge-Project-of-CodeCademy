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
| # |	rent |	bedrooms |	bathrooms |	size_sqft |	min_to_subway |	building_age_yrs |	has_washer_dryer 
| --- | --- | --- | --- | --- | --- | --- |
|0 |	3600 |	3.0 |	2 |	900 |	4 |	15 |	0 |
|1 |	3900 |	3.0 |	2 |	1000 |	4 |	8 |	0 |
|2 |	2700 |	2.0 |	1 |	900 |	4 |	96 |	0 |
|3 |	4900 |	1.0 |	1 |	1216 |	6 |	88 |	0 |
|4 |	3900 |	0.0 |	1 |	1100 |	3 |	85 |	0 |


































