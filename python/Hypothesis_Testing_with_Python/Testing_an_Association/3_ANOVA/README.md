#### HYPOTHESIS TESTING: ASSOCIATIONS

# [ANOVA](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/hypothesis-testing-associations/exercises/anova)

In the last exercise, we ran three separate 2-sample t-tests to investigate an association between 
a quantitative variable (amount spent per sale) 
and a non-binary categorical variable (location of VeryAnts visited, with options A, B, and C). 
The problem with this approach is that **it inflates our probability of a type I error**; 
the more tests we run, the worse the problem becomes!

In this situation, one approach is to instead use **ANOVA (Analysis of Variance)**. 
ANOVA tests the null hypothesis that all groups have the same population mean (eg., the true average price of a sale is the same at every location of VeryAnts).

In Python, we can use the SciPy function `f_oneway()` to perform an ANOVA. 
`f_oneway()` has two outputs: 
* the F-statistic (not covered in this course) 
* and the p-value. 

If we were comparing scores on a video-game for math majors, writing majors, and psychology majors, we could run an ANOVA test with this line:
```python
from scipy.stats import f_oneway

fstat, pval = f_oneway(scores_mathematicians, scores_writers, scores_psychologists)
```
If the p-value is below our significance threshold, we can conclude that at least one pair of our groups earned significantly different scores on average; 
however, we won’t know which pair until we investigate further!
