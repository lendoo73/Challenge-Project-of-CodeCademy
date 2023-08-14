#### CREATING, LOADING, AND SELECTING DATA WITH PANDAS
# [Importing the Pandas Module](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-i/exercises/intro-pandas)
Pandas is a Python module for working with tabular data (i.e., data in a table with rows and columns). 
Tabular data has a lot of the same functionality as SQL or Excel, but Pandas adds the power of Python.

In order to get access to the Pandas module, we’ll need to install the module and then import it into a Python file. 

The `pandas` module is usually imported at the top of a Python file under the alias pd.
```
import pandas as pd
```
If we need to access the pandas module, we can do so by operating on `pd`.

# [Create a DataFrame I](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-i/exercises/create-dataframe-i)
A DataFrame is an object that stores data as rows and columns. 
You can think of a DataFrame as a spreadsheet or as a SQL table. 
You can manually create a DataFrame or fill it with data from a CSV, an Excel spreadsheet, or a SQL query.

DataFrames have rows and columns. 
Each column has a name, which is a string. 
Each row has an index, which is an integer. 
DataFrames can contain many different data types: strings, ints, floats, tuples, etc.

You can pass in a dictionary to `pd.DataFrame()`. 
Each key is a column name and each value is a list of column values. 
The columns must all be the same length or you will get an error. Here’s an example:
```
df1 = pd.DataFrame({
    'name': ['John Smith', 'Jane Doe', 'Joe Schmo'],
    'address': ['123 Main St.', '456 Maple Ave.', '789 Broadway'],
    'age': [34, 28, 51]
})
```
This command creates a DataFrame called `df1` that looks like this:

| address |	age |	name
| --- | --- | ---
| 123 Main St. |	34 |	John Smith
| 456 Maple Ave. |	28 |	Jane Doe
| 789 Broadway |	51 |	Joe Schmo

Note that the columns will appear in alphabetical order because dictionaries don’t have any inherent order for columns.

# [Create a DataFrame II](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-i/exercises/create-dataframe-ii)
You can also add data using lists.

For example, you can pass in a list of lists, where each one represents a row of data. 
Use the keyword argument `columns` to pass a list of column names.
```
df2 = pd.DataFrame([
    ['John Smith', '123 Main St.', 34],
    ['Jane Doe', '456 Maple Ave.', 28],
    ['Joe Schmo', '789 Broadway', 51]
    ],
    columns=['name', 'address', 'age'])
``` 
This command produces a DataFrame `df2` that looks like this:

| name | address | age
| --- | --- | ---
| John Smith | 123 Main St. | 34
| Jane Doe |	456 Maple Ave. |	28
| Joe Schmo |	789 Broadway |	51

In this example, we were able to control the ordering of the columns because we used lists.

# [Comma Separated Variables (CSV)](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-i/exercises/what-is-csv)
We now know how to create our own DataFrame. 
However, most of the time, we’ll be working with datasets that already exist. 
One of the most common formats for big datasets is the *CSV*.

*CSV (comma separated values)* is a text-only spreadsheet format. 
You can find CSVs in lots of places:
* Online datasets (here’s an example from [data.gov](https://catalog.data.gov/dataset?res_format=CSV))
* Export from Excel or Google Sheets
* Export from SQL

The first row of a CSV contains column headings. 
All subsequent rows contain values. 
Each column heading and each variable is separated by a comma:
```
column1,column2,column3
value1,value2,value3
```
That example CSV represents the following table:

| column1 |	column2 | column3
| --- | --- | ---
| value1 |	value2 | value3

# [Loading and Saving CSVs](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-i/exercises/load-save-csv)
When you have data in a CSV, you can load it into a DataFrame in Pandas using `.read_csv()`:
```
pd.read_csv('my-csv-file.csv')
```
In the example above, the `.read_csv()` method is called. 
The CSV file called `my-csv-file` is passed in as an argument.

We can also save data to a CSV, using `.to_csv()`.
```
df.to_csv('new-csv-file.csv')
```
In the example above, the `.to_csv()` method is called on `df` (which represents a DataFrame object). 
The name of the CSV file is passed in as an argument (`new-csv-file.csv`). 
By default, this method will save the CSV file in your current directory.

# [Inspect a DataFrame](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-i/exercises/inspect-dataframe)
When we load a new DataFrame from a CSV, we want to know what it looks like.

If it’s a small DataFrame, you can display it by typing `print(df)`.

If it’s a larger DataFrame, it’s helpful to be able to inspect a few items without having to look at the entire DataFrame.

The method `.head()` gives the first 5 rows of a DataFrame. 
If you want to see more rows, you can pass in the positional argument `n`. 
For example, `df.head(10)` would show the first 10 rows.

The method `df.info()` gives some statistics for each column.

# [Select Columns](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-i/exercises/select-columns)
Now we know how to create and load data. 
Let’s select parts of those datasets that are interesting or important to our analyses.

Suppose you have the DataFrame called `customers`, which contains the ages of your customers:

| name |	age
| --- | ---
| Rebecca Erikson |	35
| Thomas Roberson |	28
| Diane Ochoa |	42
| … |	…

Perhaps you want to take the average or plot a histogram of the ages. 
In order to do either of these tasks, you’d need to select the column.

There are two possible syntaxes for selecting all values from a column:
1. Select the column as if you were selecting a value from a dictionary using a key. 
In our example, we would type `customers['age']` to select the ages.
2. If the name of a column follows all of the rules for a variable name (doesn’t start with a number, doesn’t contain spaces or special characters, etc.),  
then you can select it using the following notation: `df.MySecondColumn`. 
In our example, we would type `customers.age`.

When we select a single column, the result is called a *Series*.

# [Selecting Multiple Columns](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-i/exercises/select-multiple-columns)
When you have a larger DataFrame, you might want to select just a few columns.

For instance, let’s return to a DataFrame of `orders` from ShoeFly.com:

| id |	first_name |	last_name |	email |	shoe_type |	shoe_material |	shoe_color
| --- | --- | --- | --- | --- | --- | --- 
| 54791 |	Rebecca |	Lindsay |	RebeccaLindsay57@hotmail.com |	clogs |	faux-leather |	black
| 53450 |	Emily |	Joyce |	EmilyJoyce25@gmail.com |	ballet flats |	faux-leather |	navy
| 91987 |	Joyce |	Waller |	Joyce.Waller@gmail.com |	sandals |	fabric |	black
| 14437 |	Justin |	Erickson |	Justin.Erickson@outlook.com |	clogs |	faux-leather |	red

We might just be interested in the customer’s `last_name` and `email`. 
We want a DataFrame like this:

| last_name |	email
| --- | --- 
| Lindsay |	RebeccaLindsay57@hotmail.com
| Joyce |	EmilyJoyce25@gmail.com
| Waller |	Joyce.Waller@gmail.com
| Erickson |	Justin.Erickson@outlook.com

To select two or more columns from a DataFrame, we use a list of the column names. 
To create the DataFrame shown above, we would use:
```
new_df = orders[['last_name', 'email']]
```
*Note: *Make sure that you have a double set of brackets (`[[]]`), or this command won’t work!

# [Select Rows](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-i/exercises/select-rows)
Let’s revisit our `orders` from ShoeFly.com:

| id |	first_name |	last_name |	email |	shoe_type |	shoe_material |	shoe_color
| --- | --- | --- | --- | --- | --- | --- 
| 54791 |	Rebecca |	Lindsay |	RebeccaLindsay57@hotmail.com |	clogs |	faux-leather |	black
| 53450 |	Emily |	James |	EmilyJames25@gmail.com |	ballet flats |	faux-leather |	navy
| 91987 |	Joyce |	Waller |	Joyce.Waller@gmail.com |	sandals	fabric |	black
| 14437 |	Justin |	Erickson |	Justin.Erickson@outlook.com |	clogs |	faux-leather |	red
| …						

Maybe our Customer Service department has just received a message from Joyce Waller, so we want to know exactly what she ordered. 
We want to select this single row of data.

DataFrames are zero-indexed, meaning that we start with the 0th row and count up from there. 
Joyce Waller’s order is the 2nd row.

We select it using the following command:
```
orders.iloc[2]
```
When we select a single row, the result is a Series (just like when we select a single column).

# [Selecting Multiple Rows](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-i/exercises/select-multiple-rows)
You can also select multiple rows from a DataFrame.

Here are a few more rows from ShoeFly.com’s `orders` DataFrame:

| id |	first_name |	last_name |	email |	shoe_type |	shoe_material |	shoe_color
| --- | --- | --- | --- | --- | --- | --- 
| 54791 |	Rebecca |	Lindsay |	RebeccaLindsay57@hotmail.com |	clogs |	faux-leather |	black
| 53450 |	Emily |	Joyce |	EmilyJoyce25@gmail.com |	ballet flats |	faux-leather |	navy
| 91987 |	Joyce |	Waller |	Joyce.Waller@gmail.com |	sandals |	fabric |	black
| 14437 |	Justin |	Erickson |	Justin.Erickson@outlook.com |	clogs |	faux-leather| 	red
| 79357 |	Andrew |	Banks |	AB4318@gmail.com |	boots |	leather	brown
| 52386 |	Julie |	Marsh |	JulieMarsh59@gmail.com |	sandals |	fabric |	black
| 20487 |	Thomas |	Jensen |	TJ5470@gmail.com |	clogs |	fabric |	navy
| 76971 |	Janice |	Hicks |	Janice.Hicks@gmail.com |	clogs |	faux-leather |	navy
| 21586 |	Gabriel |	Porter |	GabrielPorter24@gmail.com |	clogs |	leather	brown

Here are some different ways of selecting multiple rows:
* `orders.iloc[3:7]` would select all rows starting at the 3rd row and up to but not including the 7th row (i.e., the 3rd row, 4th row, 5th row, and 6th row)

| id |	first_name |	last_name |	email |	shoe_type |	shoe_material |	shoe_color
| --- | --- | --- | --- | --- | --- | --- 
| 14437 |	Justin |	Erickson |	Justin.Erickson@outlook.com |	clogs |	faux-leather |	red
| 79357 |	Andrew |	Banks |	AB4318@gmail.com |	boots |	leather	brown
| 52386 |	Julie |	Marsh |	JulieMarsh59@gmail.com |	sandals |	fabric |	black
| 20487 |	Thomas |	Jensen |	TJ5470@gmail.com |	clogs |	fabric |	navy

* `orders.iloc[:4]` would select all rows up to, but not including the 4th row (i.e., the 0th, 1st, 2nd, and 3rd rows)

| id |	first_name |	last_name |	email |	shoe_type |	shoe_material |	shoe_color
| --- | --- | --- | --- | --- | --- | --- 
| 54791 |	Rebecca |	Lindsay |	RebeccaLindsay57@hotmail.com |	clogs |	faux-leather |	black
| 53450 |	Emily |	Joyce |	EmilyJoyce25@gmail.com |	ballet flats |	faux-leather |	navy
| 91987 |	Joyce |	Waller |	Joyce.Waller@gmail.com |	sandals |	fabric |	black
| 14437 |	Justin |	Erickson |	Justin.Erickson@outlook.com |	clogs |	faux-leather| 	red

* `orders.iloc[-3:]` would select the rows starting at the 3rd to last row and up to and including the final row

| id |	first_name |	last_name |	email |	shoe_type |	shoe_material |	shoe_color
| --- | --- | --- | --- | --- | --- | --- 
| 20487 |	Thomas |	Jensen |	TJ5470@gmail.com |	clogs |	fabric |	navy
| 76971 |	Janice |	Hicks |	Janice.Hicks@gmail.com |	clogs |	faux-leather |	navy
| 21586 |	Gabriel |	Porter |	GabrielPorter24@gmail.com |	clogs |	leather	brown

# [Select Rows with Logic I](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-i/exercises/select-rows-logic)
You can select a subset of a DataFrame by using logical statements:
```
df[df.MyColumnName == desired_column_value]
```
We have a large DataFrame with information about our customers. 
A few of the many rows look like this:

| name |	address |	phone |	age
| --- | --- | --- | --- 
| Martha Jones |	123 Main St. |	234-567-8910 |	28
| Rose Tyler |	456 Maple Ave. |	212-867-5309 |	22
| Donna Noble |	789 Broadway |	949-123-4567 |	35
| Amy Pond |	98 West End Ave. |	646-555-1234 |	29
| Clara Oswald |	54 Columbus Ave. |	714-225-1957 |	31
| … |	… |	… |	…

Suppose we want to select all rows where the customer’s `age` is `30`. 
We would use:
```
df[df.age == 30]
```
In Python, `==` is how we test if a value is exactly equal to another value.

We can use other logical statements, such as:
* Greater Than, `>` — Here, we select all rows where the customer’s age is greater than 30:
```
df[df.age > 30]
```
* Less Than, `<` — Here, we select all rows where the customer’s age is less than 30:
```
df[df.age < 30]
```
* Not Equal, `!=` — This snippet selects all rows where the customer’s name is not Clara Oswald:
```
df[df.name != 'Clara Oswald']
```

# [Select Rows with Logic II](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-i/exercises/select-rows-logic-ii)
You can also combine multiple logical statements, as long as each statement is in parentheses.

For instance, suppose we wanted to select all rows where the customer’s age was under 30 or the customer’s name was “Martha Jones”:

| name |	address	phone |	age
| --- | --- | ---
| Martha Jones |	123 Main St. |	234-567-8910 |	28
| Rose Tyler |	456 Maple Ave. |	212-867-5309 |	22
| Donna Noble |	789 Broadway |	949-123-4567 |	35
| Amy Pond |	98 West End Ave. |	646-555-1234 |	29
| Clara Oswald |	54 Columbus Ave. |	714-225-1957 |	31
| …			

We could use the following code:
```
df[(df.age < 30) |
   (df.name == 'Martha Jones')]
```
In Python, `|` means “or” and `&` means “and”.

# [Select Rows with Logic III](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-i/exercises/select-rows-isin)
Suppose we want to select the rows where the customer’s name is either “Martha Jones”, “Rose Tyler” or “Amy Pond”.

| name |	address	phone |	age
| --- | --- | ---
| Martha Jones |	123 Main St. |	234-567-8910 |	28
| Rose Tyler |	456 Maple Ave. |	212-867-5309 |	22
| Donna Noble |	789 Broadway |	949-123-4567 |	35
| Amy Pond |	98 West End Ave. |	646-555-1234 |	29
| Clara Oswald |	54 Columbus Ave. |	714-225-1957 |	31
| … |	… |	… |	…

We could use the `isin` command to check that `df.name` is one of a list of values:
```
df[df.name.isin([
    'Martha Jones',
    'Rose Tyler',
    'Amy Pond'
])]
```

# [Setting indices](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-i/exercises/reset-index)
When we select a subset of a DataFrame using logic, we end up with non-consecutive indices. 
This is inelegant and makes it hard to use `.iloc()`.

We can fix this using the method `.reset_index()`. 
For example, here is a DataFrame called `df` with non-consecutive indices:

| First | Name |	Last Name
| --- | --- | ---
| 0 | 	John |	Smith
| 4 |	Jane |	Doe
| 7 |	Joe |	Schmo

If we use the command `df.reset_index()`, we get a new DataFrame with a new set of indices:

| index | First | Name |	Last Name
| --- | --- | --- | ---
| 0 |	0 |	John |	Smith
| 1 |	4 |	Jane |	Doe
| 2 |	7 |	Joe |	Schmo

Note that the old indices have been moved into a new column called `'index'`. 
Unless you need those values for something special, it’s probably better to use the keyword `drop = True` so that you don’t end up with that extra column. 
If we run the command `df.reset_index(drop = True)`, we get a new DataFrame that looks like this:

| First | Name |	Last Name
| --- | --- | ---
| 0 |	John |	Smith
| 1 |	Jane |	Doe
| 2 |	Joe |	Schmo

Using `.reset_index()` will return a new DataFrame, but we usually just want to modify our existing DataFrame. 
If we use the keyword `inplace = True` we can just modify our existing DataFrame.
