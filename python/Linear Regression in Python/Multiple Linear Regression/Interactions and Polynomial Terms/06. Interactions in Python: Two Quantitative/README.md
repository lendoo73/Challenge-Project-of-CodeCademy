#### INTERACTIONS AND POLYNOMIAL TERMS

# [Interactions in Python: Two Quantitative](https://www.codecademy.com/courses/linear-regression-mssp/lessons/stats-interactions-and-polynomial-terms-in-multiple-regression/exercises/interactions-in-python-two-quantitative)

Building on the last exercise, let’s run a model predicting `happy` from `stress` and `freetime` with an interaction term for the predictors.
```py
import statsmodels.api as sm

modelQ = sm.OLS.from_formula(
    'happy ~ stress + freetime + stress:freetime', 
    data = happiness
).fit()

print(modelQ.params)
 
# Output:
# Intercept          7.731785
# stress            -0.551098
# freetime           0.187882
# stress:freetime    0.040401
```
We form the regression equation from the coefficients just as we did for an interaction term with a binary variable.

<h4>
    <em>
        happy = 7.73 − 0.55 ∗ stress + 0.19 ∗ freetime + 0.04 ∗ stress ∗ freetime
    </em>
</h4>

We can write a new equation for participants with differing amounts of daily free time.

For participants with **`0`** hours of free time, the equation is:

<h4>
    <em>
        happy = 7.73 − 0.55 ∗ stress + 0.19 ∗ 0 + 0.04 ∗ stress ∗ 0
    </em>
    <br />
    <em>
        happy = 7.73 − 0.55 ∗ stress + 0 + 0
    </em>
    <br />
    <em>
        happy = 7.73 − 0.55 ∗ stress
    </em>
</h4>
 
For participants with **`1`** hour of free time, the equation is:

<h4>
    <em>
        happy = 7.73 − 0.55 ∗ stress + 0.19 ∗ 1 + 0.04 ∗ stress ∗ 1
    </em>
    <br />
    <em>
        happy = 7.73 − 0.55 ∗ stress + 0.19 + 0.04 ∗ stress
    </em>
    <br />
    <em>
        happy = (7.73 + 0.19) + (−0.55 + 0.04) ∗ stress
    </em>
</h4>
 
When we simplify and combine terms, we see the intercept increases by 0.19 and the slope increases by 0.04 compared to the participants with 0 hours of free time. 
An additional 0.19 and 0.04 get added to the intercept and slope, respectively, when we increase `freetime` to **2** hours:

<h4>
    <em>
        happy = 7.73 − 0.55 ∗ stress + 0.19 ∗ 2 + 0.04 ∗ stress ∗ 2
    </em>
    <br />
    <em>
        happy = 7.73 − 0.55 ∗ stress + 0.19 ∗ 2 + 0.4 ∗ stress ∗ 2
    </em>
    <br />
    <em>
        happy = (7.73 + 0.19 ∗ 2) + (−0.55 + 0.4 ∗ 2) ∗ stress
    </em>
</h4>
 
The 0.19 that gets added to the intercept with each increase in `freetime` is the coefficient on `freetime` from our regression. 
The 0.04 that gets added to the slope of `stress` with each increase in `freetime` is the coefficient on `stress:freetime` from our regression.
