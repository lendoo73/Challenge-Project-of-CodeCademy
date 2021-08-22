#### MULTIPLE LINEAR REGRESSION

# [Interpretation of Quantitative Variables](https://www.codecademy.com/courses/linear-regression-mssp/lessons/stats-multiple-linear-regression/exercises/interpretation-of-quantitative-variables)

In a multiple regression model, the coefficient on a quantitative predictor is the expected difference in the outcome variable for a one-unit increase of the predictor, 
holding all other predictors constant.

For the `survey` dataset, the multiple regression equation is:
<h4>
    <p><em><code>score = 16.7 + 6.3 * hours_studied + 4.7 * assignments</code></em></p>
</h4>
The predictor `assignments` is a quantitative variable. 
Let’s substitute a few different values for `assignments` into the regression equation to see how it changes:
<ul>
    <li>
        For students who completed 0 assignments:
        <h4>
            <p>
                <em>
                    <code>score = 16.7 + 6.3 * hours_studied + 4.7 * 0</code>
                </em>
            </p>
            <p>
                <em>
                    <code>score = 16.7 + 6.3 * hours_studied</code>
                </em>
            </p>
        </h4>
    </li>
    <li>
        For students who completed 1 assignment:
        <h4>
            <p>
                <em>
                    <code>score = 16.7 + 6.3 * hours_studied + 4.7 * 1</code>
                </em>
            </p>
            <p>
                <em>
                    <code>score = 21.4 + 6.3 * hours_studied</code>
                </em>
            </p>
        </h4>
    </li>
    <li>
        For students who completed 2 assignment:
        <h4>
            <p>
                <em>
                    <code>score = 16.7 + 6.3 * hours_studied + 4.7 * 2</code>
                </em>
            </p>
            <p>
                <em>
                    <code>score = 26.1 + 6.3 * hours_studied</code>
                </em>
            </p>
        </h4>
    </li>
</ul>

The only difference between the equations is that we add 4.7 points to the intercept for each additional completed assignment. 
Thus, among students who studied the same number of hours (i.e., holding all other variables constant), 
students who completed one more assignment earned a 4.7 point higher test score on average.
