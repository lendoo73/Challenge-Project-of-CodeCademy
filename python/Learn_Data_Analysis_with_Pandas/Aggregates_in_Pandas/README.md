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
















