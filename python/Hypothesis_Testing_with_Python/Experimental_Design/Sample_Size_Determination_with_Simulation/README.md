#### SAMPLE SIZE DETERMINATION WITH SIMULATION

# [Introduction](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/experimental-design/exercises/introduction)

In this lesson, we will use simulation to understand some of the considerations for setting up an A/B test: 
* sample size, 
* power, 
* and the false positive rate. 

But before we think about designing an A/B test, let’s first remind ourselves how to conduct the test itself, after planning and collecting data.

Suppose that a media company currently has a weekly newsletter email and wants to see 
if using the recipient’s first name in the email subject will cause more people to open the email (ie. “Bob! Checkout this week’s updates” vs “Checkout this week’s updates”). 
They randomly assign a group of 100 recipients to receive one of the two email subjects and record whether or not each recipient opened the email. 
The first few rows of their data might look something like this:

| Email |	Opened
| ---  | :---:
| name |	yes
| name |	no
| control |	yes
| control |	yes
| name |	no

In order to run a hypothesis test to decide whether there is a significant difference in the open rate for these emails, we would run a Chi-Square test. 
To accomplish this, we would first create a contingency table for the Email and Opened variables in the above table:
```python
X = pd.crosstab(data.Email, data.Opened)
print(X)
```
Output:

| Opened |	no |	yes
| Email		
| control |	23 |	27
| name |	16 |	34

We would then use this table to run a Chi-Square test and get a p-value:
```python
chi2, pval, dof, expected = chi2_contingency(X)
print(pval) #Output: 0.2186
```
Based on the p-value, we would make a decision about which email to use; 
a small p-value would provide evidence that the open rates are significantly different for the two groups, while a large p-value would suggest no significant difference.



















