#### INTERACTIONS AND POLYNOMIAL TERMS

# [Interactions in Python: Binary and Quantitative](https://www.codecademy.com/courses/linear-regression-mssp/lessons/stats-interactions-and-polynomial-terms-in-multiple-regression/exercises/interactions-in-python-binary-and-quantitative)

In the last exercise, we ran a regression predicting happiness scores from stress scores and exercise participation without an interaction term. 
We got the following model coefficients:
```py
# Output:
# Intercept    10.256296
# stress       -0.707925
# exercise     -0.894058
```
Using these coefficients, our regression equation is:

<h4>
    <em>
        happy = 10.3 − 0.7 ∗ stress − 0.9 ∗ exercise
    </em>
</h4>

In the Python library `statsmodels.api`, we can easily add an interaction term to the model formula by 
adding a third predictor that combines `stress` and `exercise` with a colon (`stress:exercise`). 
The code to run the updated model and print the coefficients is shown below.
```py
import statsmodels.api as sm

model = sm.OLS.from_formula(
    'happy ~ stress + exercise + stress:exercise', 
    data = happiness
).fit()

print(model.params)
 
# Output:
# Intercept          12.053583
# stress             -0.971225
# exercise           -3.135705
# stress:exercise     0.357365
```
In addition to the expected coefficients, when we add the interaction term, the coefficient table shows a new term with a coefficient: `stress:exercise`. 
The coefficient on `stress:exercise` is really a coefficient on a whole new variable formed by multiplying `stress` by `exercise`. 
Thus, our regression equation for this model looks like this:

<h4>
    <em>
        happy = 12.1 − 1.0 ∗ stress − 3.1 ∗ exercise + 0.4 ∗ stress ∗ exercise
    </em>
</h4>

Note that our other coefficients changed slightly with the additional predictor. 
This is because we have explicitly pulled out more of the relationship between stress and exercise, causing the other coefficients to adjust to take this into account.
