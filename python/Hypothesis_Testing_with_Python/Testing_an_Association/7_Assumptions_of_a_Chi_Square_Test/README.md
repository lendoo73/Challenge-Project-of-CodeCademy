####

# [Assumptions of a Chi-Square Test](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/hypothesis-testing-associations/exercises/assumptions-of-a-chi-square-test)

Before we use a Chi-Square test, we need to be sure that the following things are true:

## 1. The observations should be independently randomly sampled from the population
This is also true of **2-sample t-tests**, **ANOVA**, and **Tukey**. 
The purpose of this assumption is to ensure that the sample is representative of the population of interest.

## 2. The categories of both variables must be mutually exclusive
In other words, individual observations should only fall into one category per variable. 
This means that categorical variables like “college major”, where students can have multiple different college majors, would not be appropriate for a Chi-Square test.

## 3. The groups should be independent
Similar to **2-sample t-tests**, **ANOVA**, and **Tukey**, a **Chi-Square** test also shouldn’t be used if 
either of the categorical variables splits observations into groups that can influence one another. 
For example, a Chi-Square test would not be appropriate if one of the variables represents three different time points.
