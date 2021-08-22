#### MULTIPLE LINEAR REGRESSION

# [Interpretation of Quantitative Variables](https://www.codecademy.com/courses/linear-regression-mssp/lessons/stats-multiple-linear-regression/exercises/interpretation-of-quantitative-variables)

In a multiple regression model, the coefficient on a quantitative predictor is the expected difference in the outcome variable for a one-unit increase of the predictor, 
holding all other predictors constant.

For the `survey` dataset, the multiple regression equation is:

\text{score} = 16.7 + 6.3*\text{hours\_studied} + 4.7*\text{assignments}score=16.7+6.3∗hours_studied+4.7∗assignments
The predictor assignments is a quantitative variable. Let’s substitute a few different values for assignments into the regression equation to see how it changes:

For students who completed 0 assignments:
\begin{aligned} \text{score} = 16.7 + 6.3*\text{hours\_studied} + 4.7*\bf{0}\\ \text{score} = 16.7 + 6.3*\text{hours\_studied}\\ \end{aligned} 
score=16.7+6.3∗hours_studied+4.7∗0
score=16.7+6.3∗hours_studied
​
 
For students who completed 1 assignment:
\begin{aligned} \text{score} = 16.7 + 6.3*\text{hours\_studied} + 4.7*\bf{1}\\ \text{score} = 21.4 + 6.3*\text{hours\_studied}\\ \end{aligned} 
score=16.7+6.3∗hours_studied+4.7∗1
score=21.4+6.3∗hours_studied
​
 
For students who completed 2 assignments:
\begin{aligned} \text{score} = 16.7 + 6.3*\text{hours\_studied} + 4.7*\bf{2}\\ \text{score} = 26.1 + 6.3*\text{hours\_studied}\\ \end{aligned} 
score=16.7+6.3∗hours_studied+4.7∗2
score=26.1+6.3∗hours_studied
​
 
The only difference between the equations is that we add 4.7 points to the intercept for each additional completed assignment. Thus, among students who studied the same number of hours (i.e., holding all other variables constant), students who completed one more assignment earned a 4.7 point higher test score on average.
