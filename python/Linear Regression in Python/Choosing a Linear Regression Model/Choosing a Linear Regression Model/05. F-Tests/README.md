#### CHOOSING A LINEAR REGRESSION MODEL

# [F-Tests](https://www.codecademy.com/courses/linear-regression-mssp/lessons/choosing-a-linear-regression-model/exercises/f-tests)

In the previous exercises, we compared nested models based on adjusted R-squared.

Another way to compare nested models is by using a hypothesis test called an **F-test**. 
Suppose we want to compare the following two models:
```py
model1 = sm.OLS.from_formula(
    'rent ~ bedrooms + size_sqft', 
    data = rentals
).fit()
 
model2 = sm.OLS.from_formula(
    'rent ~ bedrooms + size_sqft + building_age_yrs + has_elevator', 
    data = rentals
).fit()
```
Note that the second model has two more predictors than the first (`building_age_yrs` and `has_elevator`). 
For an F-test comparing these two models:
* The null hypothesis is that the coefficients on `building_age_yrs` and `has_elevator` are equal to zero (they are not useful in explaining the observed variation in rent).
* The alternative hypothesis is that least one of the coefficients is non-zero.

We can run the test in Python as follows:
```py
from statsmodels.stats.anova import anova_lm

anova_results = anova_lm(model1, model2)

print(anova_results)
```
Output:

|  | df_resid |	ssr |	df_diff |	ss_diff | F |	Pr(>F) |
| --- | --- | --- | --- | --- | --- | --- |
| 0 |	4997.0 |	1.4e+10 |	0.0 |	NaN |	NaN |	NaN |
| 1 |	4995.0 |	1.4e+10 |	2.0 |	9.2e+08 |	170.9 |	1.6e-72 |

The p-value (`1.6e-72`, which is equal to .00000..[72 total zeros]..16) is located in the bottom right corner of this table. 
The column name `Pr(>F)` means “the probability of observing an F statistic greater than observed (170.9) if the null hypothesis is true”.

Using a significance threshold of 0.05, the p-value is below the threshold. 
Therefore, we would conclude that either (or both) of the coefficients on `building_age_yrs` and `has_elevator` is non-zero. 
Thus, including at least one of these two predictors significantly improves the model.

This would lead us to choose `model2` over `model1`. 
After running this test, we might also want to separately compare a model with `building_age_yrs` and a model with `has_elevator` to see whether both are necessary. 
We could do this with separate F-tests or adjusted R-squared.
