#### MODIFYING DATAFRAMES
# [Modifying DataFrames](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-ii/exercises/intro-ii)
In the previous lesson, you learned what a DataFrame is and how to select subsets of data from one.

In this lesson, you’ll learn how to modify an existing DataFrame. 
Some of the skills you’ll learn include:
* Adding columns to a DataFrame
* Using lambda functions to calculate complex quantities
* Renaming columns

## [Adding a Column I](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-ii/exercises/add-column)
Sometimes, we want to add a column to an existing DataFrame. 
We might want to add new information or perform a calculation based on the data that we already have.

One way that we can add a new column is by giving a list of the same length as the existing DataFrame.

Suppose we own a hardware store called The Handy Woman and have a DataFrame containing inventory information:

| Product ID |	Product Description |	Cost to Manufacture |	Price
| --- | --- | --- | --- 
| 1 |	3 inch screw |	0.50 |	0.75
| 2 |	2 inch nail |	0.10 |	0.25
| 3 |	hammer |	3.00 |	5.50
| 4 |	screwdriver |	2.50 |	3.00

It looks like the actual quantity of each product in our warehouse is missing!

Let’s use the following code to add that information to our DataFrame.
```
df['Quantity'] = [100, 150, 50, 35]
```
Our new DataFrame looks like this:

| Product ID |	Product Description |	Cost to Manufacture |	Price |	Quantity
| --- | --- | --- | --- | ---
| 1 |	3 inch screw |	0.50 |	0.75 |	100
| 2 |	2 inch nail |	0.10 |	0.25 |	150
| 3 |	hammer |	3.00 |	5.50 |	50
| 4 |	screwdriver |	2.50 |	3.00 |	35

## [Adding a Column II](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-ii/exercises/add-column-ii)
We can also add a new column that is the same for all rows in the DataFrame. 
Let’s return to our inventory example:

| Product ID |	Product Description |	Cost to Manufacture |	Price
| --- | --- | --- | --- 
| 1 |	3 inch screw |	0.50 |	0.75
| 2 |	2 inch nail |	0.10 |	0.25
| 3 |	hammer |	3.00 |	5.50
| 4 |	screwdriver |	2.50 |	3.00

Suppose we know that all of our products are currently in-stock. 
We can add a column that says this:
```
df['In Stock?'] = True
```
Now all of the rows have a column called `In Stock?` with value `True`.

| Product ID |	Product Description |	Cost to Manufacture |	Price |	In Stock?
| --- | --- | --- | --- | --- 
| 1 |	3 inch screw |	0.50 |	0.75 |	True
| 2 |	2 inch nail |	0.10 |	0.25 |	True
| 3 |	hammer |	3.00 |	5.50 |	True
| 4 |	screwdriver | 2.50 |	3.00 |	True

## [Adding a Column III](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-ii/exercises/add-column-iii)
Finally, you can add a new column by performing a function on the existing columns.

Maybe we want to add a column to our inventory table with the amount of sales tax that we need to charge for each item. 
The following code multiplies each `Price` by `0.075`, the sales tax for our state:
```
df['Sales Tax'] = df.Price * 0.075
```
Now our table has a column called `Sales Tax`:

| Product ID |	Product Description |	Cost to Manufacture |	Price |	Sales Tax
| --- | --- | --- | --- | ---
| 1 |	3 inch screw |	0.50 |	0.75 |	0.06
| 2 |	2 inch nail |	0.10 |	0.25 |	0.02
| 3 |	hammer | 3.00 |	5.50 |	0.41
| 4 |	screwdriver |	2.50 |	3.00 |	0.22

## [Performing Column Operations](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-ii/exercises/columns-apply)
Often, the column that we want to add is related to existing columns, but requires a calculation more complex than multiplication or addition.

For example, imagine that we have the following table of customers.

| Name |	Email
| --- | ---
| JOHN SMITH |	john.smith@gmail.com
| Jane Doe |	jdoe@yahoo.com
| joe schmo |	joeschmo@hotmail.com

It’s a little annoying that the capitalization is different for each row. 
Perhaps we’d like to make it more consistent by making all of the letters uppercase.

We can use the `apply` function to apply a function to every value in a particular column. 
For example, this code overwrites the existing `'Name'` columns by applying the function `upper` to every row in `'Name'`.
```
from string import upper
 
df['Name'] = df.Name.apply(upper)
```
The result:

| Name |	Email
| --- | ---
| JOHN SMITH |	john.smith@gmail.com
| JANE DOE |	jdoe@yahoo.com
| JOE SCHMO |	joeschmo@hotmail.com

## [Reviewing Lambda Function](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-ii/exercises/lambda-functions)
A *lambda function* is a way of defining a function in a single line of code. 
Usually, we would assign them to a variable.

For example, the following lambda function multiplies a number by 2 and then adds 3:
```
mylambda = lambda x: (x * 2) + 3
print(mylambda(5)) # The output: 13
```
Lambda functions work with all types of variables, not just integers! 
Here is an example that takes in a string, assigns it to the temporary variable `x`, and then converts it into lowercase:
```
stringlambda = lambda x: x.lower()
print(stringlambda("Oh Hi Mark!")) # The output: "oh hi mark!"
```
Learn more about lambda functions in [this article](https://www.codecademy.com/articles/lambda-functions)!

## [Reviewing Lambda Function: If Statements](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-ii/exercises/lambda-functions-if)
We can make our lambdas more complex by using a modified form of an if statement.

Suppose we want to pay workers time-and-a-half for overtime (any work above 40 hours per week). 
The following function will convert the number of hours into time-and-a-half hours using an if statement:
```
def myfunction(x):
    if x > 40:
        return 40 + (x - 40) * 1.50
    else:
        return x
```
Below is a lambda function that does the same thing:
```
myfunction = lambda x: 40 + (x - 40) * 1.50 if x > 40 else x
```
In general, the syntax for an if function in a lambda function is:
```
lambda x: [OUTCOME IF TRUE] if [CONDITIONAL] else [OUTCOME IF FALSE]
```
```
mylambda = lambda age: "Welcome to BattleCity!" if age >= 13 else "You must be over 13"
```

## [Applying a Lambda to a Column](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-ii/exercises/lambda-apply-column)
In Pandas, we often use lambda functions to perform complex operations on columns. 
For example, suppose that we want to create a column containing the email provider for each email address in the following table:

| Name |	Email
| --- | ---
| JOHN SMITH |	john.smith@gmail.com
| Jane Doe |	jdoe@yahoo.com
| joe schmo |	joeschmo@hotmail.com

We could use the following code with a lambda function and the [string method](https://www.codecademy.com/courses/learn-python-3/lessons/string-methods/exercises/splitting-strings)
`.split()`:
```
df['Email Provider'] = df.Email.apply(
    lambda x: x.split('@')[-1]
)
```
The result would be:

| Name |	Email |	Email Provider
| --- | --- | ---
| JOHN SMITH |	john.smith@gmail.com |	gmail.com
| Jane Doe |	jdoe@yahoo.com |	yahoo.com
| joe schmo |	joeschmo@hotmail.com |	hotmail.com

































