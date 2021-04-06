#### [AGGREGATES IN PANDAS](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-aggregates/exercises/intro-aggregates)

# [Introduction](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-aggregates/exercises/intro-aggregates)

An aggregate statistic is a way of creating a single number that describes a group of numbers. 
Common aggregate statistics include mean, median, or standard deviation.

You will also learn how to rearrange a DataFrame into a pivot table, which is a great way to compare data across two dimensions.

# [Calculating Column Statistics](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-aggregates/exercises/column-statistics)

In this exercise, you will learn how to combine all of the values from a column for a single calculation.

Some examples of this type of calculation include:
* The DataFrame `customers` contains the names and ages of all of your customers. 
You want to find the median age:
```
print(customers.age)
>> [23, 25, 31, 35, 35, 46, 62]
print(customers.age.median())
>> 35
```
* The DataFrame `shipments` contains address information for all shipments that you’ve sent out in the past year. 
You want to know how many different states you have shipped to (and how many shipments went to the same state).
```
print(shipments.state)
>> ['CA', 'CA', 'CA', 'CA', 'NY', 'NY', 'NJ', 'NJ', 'NJ', 'NJ', 'NJ', 'NJ', 'NJ']
print(shipments.state.nunique())
>> 3
```
* The DataFrame `inventory` contains a list of types of t-shirts that your company makes. 
You want a list of the colors that your shirts come in.
```
print(inventory.color)
>> ['blue', 'blue', 'blue', 'blue', 'blue', 'green', 'green', 'orange', 'orange', 'orange']
print(inventory.color.unique())
>> ['blue', 'green', 'orange']
```

The general syntax for these calculations is:
```
df.column_name.command()
```
The following table summarizes some common commands:

| Command |	Description
| --- | ---
| mean |	Average of all values in column
| std | Standard deviation
| median |	Median
| max |	Maximum value in column
| min |	Minimum value in column
| count |	Number of values in column
| nunique |	Number of unique values in column
| unique |	List of unique values in column

# [Calculating Aggregate Functions I](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-aggregates/exercises/groupby-i)

When we have a bunch of data, we often want to calculate aggregate statistics (mean, standard deviation, median, percentiles, etc.) over certain subsets of the data.

Suppose we have a grade book with columns `student`, `assignment_name`, and `grade`. 
The first few lines look like this:

| student |	assignment_name |	grade
| --- | --- | ---
| Amy |	Assignment 1 |	75
| Amy |	Assignment 2 |	35
| Bob |	Assignment 1 |	99
| Bob	Assignment 2 |	35
| …

We want to get an average grade for each student across all assignments. 
We could do some sort of loop, but Pandas gives us a much easier option: the method `.groupby`.

For this example, we’d use the following command:
```
grades = df.groupby('student').grade.mean()
```
The output might look something like this:

| student |	grade
| --- | ---
| Amy |	80
| Bob |	90
| Chris |	75
| …	

In general, we use the following syntax to calculate aggregates:
```
df.groupby('column1').column2.measurement()
```
where:

* **`column1`** is the column that we want to group by (`'student'` in our example)
* **`column2`** is the column that we want to perform a measurement on (`grade` in our example)
* **`measurement`** is the measurement function we want to apply (`mean` in our example)

# [Calculating Aggregate Functions II](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-aggregates/exercises/groupby-ii)
After using `groupby`, we often need to clean our resulting data.

As we saw in the previous exercise, the `groupby` function **creates a new Series**, not a DataFrame. 
For our ShoeFly.com example, the indices of the Series were different values of `shoe_type`, and the name property was `price`.

Usually, we’d prefer that those indices were actually a column. 
In order to get that, we can use `reset_index()`. 
This will **transform our Series into a DataFrame** and move the indices into their own column.

Generally, you’ll always see a `groupby` statement followed by `reset_index`:
```
df.groupby('column1').column2.measurement()
    .reset_index()
```
When we use groupby, we often want to rename the column we get as a result. 
For example, suppose we have a DataFrame `teas` containing data on types of tea:

| id |	tea |	category |	caffeine |	price
| --- | --- | --- | --- | --- 
| 0 |	earl grey |	black |	38 |	3
| 1 |	english breakfast |	black |	41 |	3
| 2 |	irish breakfast |	black |	37 |	2.5
| 3 |	jasmine |	green |	23 |	4.5
| 4 |	matcha |	green |	48 |	5
| 5 |	camomile |	herbal |	0 |	3
| …				

We want to find the number of each `category` of tea we sell. 
We can use:
```
teas_counts = teas.groupby('category').id.count().reset_index()
```
This yields a DataFrame that looks like:

|   | category |	id
| --- | --- | ---
| 0 |	black |	3
| 1 |	green |	4
| 2 |	herbal |	8
| 3 |	white |	2
| …		

The new column contains the counts of each category of tea sold. 
We have 3 black teas, 4 green teas, and so on. 
However, this column is called `id` because we used the `id` column of `teas` to calculate the counts. 
We actually want to call this column `counts`. 
Remember that we can rename columns:
```
teas_counts = teas_counts.rename(
    columns = {
        "id": "counts"
    }
)
```
Our DataFrame now looks like:

|    | category |	counts
| --- | --- | ---
| 0 |	black |	3
| 1 |	green |	4
| 2 |	herbal |	8
| 3 |	white |	2
| …		

# [Calculating Aggregate Functions III](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-aggregates/exercises/groupby-iii)

Sometimes, the operation that you want to perform is more complicated than `mean` or `count`. 
In those cases, you can use the `apply` method and lambda functions, just like we did for individual column operations. 
Note that the input to our lambda function will always be a list of values.

A great example of this is calculating percentiles. 
Suppose we have a DataFrame of employee information called `df` that has the following columns:
* `id`: the employee’s id number
* `name`: the employee’s name
* `wage`: the employee’s hourly wage
* `category`: the type of work that the employee does

Our data might look something like this:

| id |	name |	wage |	category
| --- | --- | --- | ---
| 10131 |	Sarah Carney |	39 |	product
| 14189 |	Heather Carey |	17 |	design
| 15004 |	Gary Mercado |	33 |	marketing
| 11204 |	Cora Copaz |	27 |	design
| …			

If we want to calculate the 75th percentile (i.e., the point at which 75% of employees have a lower wage and 25% have a higher wage) for each `category`, we can use the following combination of `apply` and a lambda function:
```
# np.percentile can calculate any percentile over an array of values
high_earners = df.groupby('category').wage
    .apply(lambda x: np.percentile(x, 75))
    .reset_index()
```
The output, `high_earners` might look like this:

|    | category |	wage
| --- | --- | ---
|0 |	design |	23
| 1 |	marketing |	35
| 2 |	product |	48
| …		

# [Calculating Aggregate Functions IV](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-aggregates/exercises/groupby-iv)

Sometimes, we want to group by more than one column. 
We can easily do this by passing a list of column names into the `groupby` method.

Imagine that we run a chain of stores and have data about the number of sales at different locations on different days:

| Location |	Date |	Day of Week |	Total Sales
| --- | --- | ---- | ----
| West Village |	February 1 |	W |	400
| West Village |	February 2 |	Th |	450
| Chelsea |	February 1 |	W |	375
| Chelsea |	February 2 |	Th |	390

We suspect that sales are different at different locations on different days of the week. 
In order to test this hypothesis, we could calculate the average sales for each store on each day of the week across multiple months. 
The code would look like this:
```
df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()
```
The results might look something like this:

| Location |	Day of Week |	Total Sales
| --- | --- | ---
| Chelsea |	M |	402.50
| Chelsea |	Tu |	422.75
| Chelsea |	W |	452.00
| …		
| West Village |	M |	390
| West Village |	Tu |	400
| …		



















