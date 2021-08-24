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

\text{happy} = 7.73 - 0.55*\text{stress} + 0.19*\textbf{freetime} + 0.04*\text{stress}*\textbf{freetime}happy=7.73−0.55∗stress+0.19∗freetime+0.04∗stress∗freetime
We can write a new equation for participants with differing amounts of daily free time.

For participants with 0 hours of free time, the equation is:

\begin{aligned} \text{happy} = 7.73 - 0.55*\text{stress} + 0.19*\bm{0} + 0.04*\text{stress}*\bm{0} \\ \text{happy} = 7.73 - 0.55*\text{stress} + 0 + 0 \\ \text{happy} = 7.73 - 0.55*\text{stress} \\ \end{aligned} 
happy=7.73−0.55∗stress+0.19∗0+0.04∗stress∗0
happy=7.73−0.55∗stress+0+0
happy=7.73−0.55∗stress
​
 
For participants with 1 hour of free time, the equation is:

\begin{aligned} \text{happy} = 7.73 - 0.55*\text{stress} + 0.19*\bm{1} + 0.04*\text{stress}*\bm{1} \\ \text{happy} = 7.73 - 0.55*\text{stress} + 0.19 + 0.4*\text{stress} \\ \text{happy} = (7.73+0.19) + (- 0.55 + 0.4)*\text{stress} \\ \end{aligned} 
happy=7.73−0.55∗stress+0.19∗1+0.04∗stress∗1
happy=7.73−0.55∗stress+0.19+0.4∗stress
happy=(7.73+0.19)+(−0.55+0.4)∗stress
​
 
When we simplify and combine terms, we see the intercept increases by 0.19 and the slope increases by 0.04 compared to the participants with 0 hours of free time. An additional 0.19 and 0.04 get added to the intercept and slope, respectively, when we increase freetime to 2 hours:

\begin{aligned} \text{happy} = 7.73 - 0.55*\text{stress} + 0.19*\bm{2} + 0.04*\text{stress}*\bm{2} \\ \text{happy} = 7.73 - 0.55*\text{stress} + 0.19*2 + 0.4*\text{stress}*2 \\ \text{happy} = (7.73+0.19*2) + (- 0.55 + 0.4*2)*\text{stress} \\ \end{aligned} 
happy=7.73−0.55∗stress+0.19∗2+0.04∗stress∗2
happy=7.73−0.55∗stress+0.19∗2+0.4∗stress∗2
happy=(7.73+0.19∗2)+(−0.55+0.4∗2)∗stress
​
 
The 0.19 that gets added to the intercept with each increase in freetime is the coefficient on freetime from our regression. The 0.04 that gets added to the slope of stress with each increase in freetime is the coefficient on stress:freetime from our regression.
