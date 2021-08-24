#### INTERACTIONS AND POLYNOMIAL TERMS

# [Interpreting Interactions: Binary and Quantitative](https://www.codecademy.com/courses/linear-regression-mssp/lessons/stats-interactions-and-polynomial-terms-in-multiple-regression/exercises/interpreting-interactions-binary-and-quantitative)

By adding an interaction term for our binary predictor, we have made our model more complex and have therefore also added complexity to its interpretation.

Returning to our multiple regression equation with an interaction term from the last exercise, we have:

<h4>
    <em>
        happy = 12.1 − 1.0 ∗ stress − 3.1 ∗ exercise + 0.4 ∗ stress ∗ exercise
    </em>
</h4>

We can rewrite this equation for the group that doesn’t exercise regularly (`exercise = 0`) and for the one that does (`exercise = 1`).

When `exercise = 0`, the last two terms become zero and go away:

<h4>
    <em>
        happy = 12.1 − 1.0 ∗ stress − 3.1 ∗ 0 + 0.4 ∗ stress ∗ 0
    </em>
    <br />
    <em>
        happy = 12.1 − 1.0 ∗ stress − 0 + 0
    </em>
    <br />
    <em>
        happy = 12.1 − 1.0 ∗ stress
    </em>
</h4>

When `exercise = 1`, the intercept goes down by 3.1 and the coefficient on `stress` increases by 0.4:

<h4>
    <em>
        happy = 12.1 − 1.0 ∗ stress − 3.1 ∗ 1 + 0.4 ∗ stress ∗ 1
    </em>
    <br />
    <em>
        happy = 12.1 − 1.0 ∗ stress − 3.1 + 0.4 ∗ stress
    </em>
    <br />
    <em>
        happy = (12.1 − 3.1) + (−1.0 + 0.4) ∗ stress
    </em>
    <br />
    <em>
        happy = 9.0 − 0.6 ∗ stress
    </em>
</h4>
 
We can see the coefficient on `exercise` tells us the difference in INTERCEPTS between the two exercise groups. 
In this case, the intercept of the regression line for the group that exercises (9.0) is 3.1 units lower than that of the group that doesn’t exercise (12.1).

On the other hand, the coefficient on the interaction term tells us the difference in SLOPES between the two regression lines. 
The slope on `stress` for the group that exercises (-0.6) is 0.4 units greater than that of the group that doesn’t exercise (-1.0). 
This would lead us to conclude that the happiness level of the group who exercises is less negatively impacted by stress.
