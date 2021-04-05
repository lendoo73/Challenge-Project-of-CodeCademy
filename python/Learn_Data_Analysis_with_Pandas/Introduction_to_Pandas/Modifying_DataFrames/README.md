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








































