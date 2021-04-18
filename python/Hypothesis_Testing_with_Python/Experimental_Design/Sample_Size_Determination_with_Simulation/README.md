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
| --- | --- | ---
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

# [Simulating Data for a Chi-Square test](https://www.codecademy.com/courses/hypothesis-testing-python/lessons/experimental-design/exercises/simulating-data-for-a-chi-square-test)

In the last exercise, we used some data from an A/B test to run a Chi-Square test. 
In the next few exercises, we’ll build up a simulation to understand the considerations that go into choosing a sample size for that test.

Again consider the A/B test example from the previous exercise, comparing email subjects with and without the recipient’s first name. 
Suppose we know that visitors have a 50% chance of opening the control email and a 65% chance of opening the name email (30% lift!).

Here we use lift to refer to the inherent difference in the distributions of our two groups of data. 
In the A/B Testing: 
Sample Size Calculators lesson, 
we learned that minimum detectable effect is the smallest size of the difference between the two groups that we want our test to be able to detect. 
If we set up our experiment with a minimum detectable effect of at least 20%, our statistical test should detect a difference with a “lift” or “effect” of 20% or greater. 
In this lesson we are going to simulate data that has a lift of 30% to demonstrate how the inherent lift impacts the power of our statistical test.

We can use the aforementioned probabilities to simulate a dataset of 100 email recipients as follows:
```python
sample_control = np.random.choice(
    ['yes', 'no'], 
    size = 50, 
    p = [.5, .5]
)
sample_name = np.random.choice(
    ['yes', 'no'], 
    size = 50, 
    p = [.65, .35]
)
```
This gives us two simulated samples, of 50 recipients each, who hypothetically saw the name or control email subject. 
Each one looks something like ['yes' 'no' 'no' 'no' 'yes' 'yes' ...], where 'yes' corresponds to an opened email.

Next, we can assemble these arrays into a data frame that looks a lot like the one we saw in exercise 1:
```python
group = ['control'] * 50 + ['name'] * 50
outcome = list(sample_control) + list(sample_name)
sim_data = {"Email": group, "Opened": outcome}
sim_data = pd.DataFrame(sim_data)
print(sim_data.head())
```
Output:

| Email |	Opened
| --- | :---:
| control |	no
| control |	yes
| control |	yes
| control |	no
| control |	no
Because of how we created this data frame, all of the “control” observations will be listed first, followed by all of the “name” observations.

















