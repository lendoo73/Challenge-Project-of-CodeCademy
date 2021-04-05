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
