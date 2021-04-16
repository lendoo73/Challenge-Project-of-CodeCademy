#### HYPOTHESIS TESTING: ASSOCIATIONS

# [Two-Sample T-Test](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/hypothesis-testing-associations/exercises/two-sample-t-test)

Suppose that a company is considering a new color-scheme for their website. 
They think that visitors will spend more time on the site if it is brightly colored. 
To test this theory, the company shows the old and new versions of the website to 50 site visitors, each — and finds that, on average, 
visitors spent 2 minutes longer on the new version compared to the old. 
Will this be true of future visitors as well? 
Or could this have happened by random chance among the 100 people in this sample?

One way of testing this is with a 2-sample t-test. 
The ***null hypothesis*** for this test is that *average length of a visit does not differ based on the color of the website*. 
In other words, if we could observe all site visitors in two alternate universes (one where they see each version of the site), 
the average visiting times in these universes would be equal.

We can use SciPy’s `ttest_ind()` function to perform a 2-sample t-test. 
It takes the values for each group as inputs and returns the *t-statistic* (not covered in this course) and a *p-value*:
```
from scipy.stats import ttest_ind

tstat, pval = ttest_ind(times_version1, times_version2)
```
By default, `ttest_ind()` runs a two-sided test.

