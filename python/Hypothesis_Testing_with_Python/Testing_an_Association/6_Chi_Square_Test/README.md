#### HYPOTHESIS TESTING: ASSOCIATIONS

# [Chi-Square Test](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/hypothesis-testing-associations/exercises/chi-square-test)

If we want to understand whether the outcomes of two categorical variables are associated, we can use a Chi-Square test. 
It is useful in situations like:
* An A/B test where half of users were shown a green submit button and the other half were shown a purple submit button. 
Was one group more likely to click the submit button?
* People under and over age 40 were given a survey asking “Which of the following three products is your favorite?” 
Did these age groups have significantly different preferences?

In SciPy, we can use the function `chi2_contingency()` to perform a Chi-Square test. 
The input to `chi2_contingency` is a contingency table, which can be created using the pandas `crosstab()` function as follows:
```pythom
#create table:
import pandas as pd

table = pd.crosstab(variable_1, variable_2)
 
#run the test:
from scipy.stats import chi2_contingency

chi2, pval, dof, expected = chi2_contingency(table)
```
For example, suppose we want to know whether gender is associated with the probability of a website visitor making a purchase. 
The null hypothesis is that there’s no association between the variables 
(eg. males, females, and non-binary people are all equally likely to make a purchase on the website, so gender and purchase-status are not associated). 
If the p-value is below our chosen threshold (often 0.05), 
we reject the null hypothesis and can conclude there is a statistically significant association between the two variables 
(eg. men, women, and non-binary people appear to have different probabilities of making a purchase, so gender is associated with purchase-status).
