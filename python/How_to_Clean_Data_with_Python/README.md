#### HOW TO CLEAN DATA WITH PYTHON

# [Diagnose the Data](https://www.codecademy.com/courses/practical-data-cleaning/lessons/pandas-data-cleaning/exercises/diagnose-data)
We often describe data that is easy to analyze and visualize as “tidy data”. 
What does it mean to have tidy data?

For data to be tidy, it must have:
* Each variable as a separate column
* Each row as a separate observation

The first step of diagnosing whether or not a dataset is tidy is using `pandas` functions to explore and probe the dataset.

You’ve seen most of the functions we often use to diagnose a dataset for cleaning. 
Some of the most useful ones are:
* **`.head()`** — display the first 5 rows of the table
* **`.info()`** — display a summary of the table
* **`.describe()`** — display the summary statistics of the table
* **`.columns`** — display the column names of the table
* **`.value_counts()`** — display the distinct values for a column

# [Dealing with Multiple Files](https://www.codecademy.com/courses/practical-data-cleaning/lessons/pandas-data-cleaning/exercises/multiple-files)
Often, you have the same data separated out into multiple files.

Let’s say that we have a ton of files following the filename structure: `'file1.csv'`, `'file2.csv'`, `'file3.csv'`, and so on. 
The power of pandas is mainly in being able to manipulate large amounts of structured data, 
so we want to be able to get all of the relevant information into one table so that we can analyze the aggregate data.

We can combine the use of `glob`, a Python library for working with files, with pandas to organize this data better. 
`glob` can open multiple files by using regex matching to get the filenames:
```
import glob
 
files = glob.glob("file*.csv")
 
df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)
 
df = pd.concat(df_list)
 
print(files)
```
This code goes through any file that starts with `'file'` and has an extension of `.csv`. 
It opens each file, reads the data into a DataFrame, and then concatenates all of those DataFrames together.

# [Reshaping your Data](https://www.codecademy.com/courses/practical-data-cleaning/lessons/pandas-data-cleaning/exercises/reshape)
Since we want

Each variable as a separate column
Each row as a separate observation
We would want to reshape a table like:

We can use `pd.melt()` to reshape a table. 
`.melt()` takes in a DataFrame, and the columns to unpack:
```
pd.melt(
  frame = df, 
  id_vars = "name", 
  value_vars = ["Checking","Savings"], 
  value_name = "Amount", 
  var_name = "Account Type"
)
```
The parameters you provide are:
* `frame`: the DataFrame you want to melt
* `id_vars`: the column(s) of the old DataFrame to preserve
* `value_vars`: the column(s) of the old DataFrame that you want to turn into variables
* `value_name`: what to call the column of the new DataFrame that stores the values
* `var_name`: what to call the column of the new DataFrame that stores the variables

The default names may work in certain situations, but it’s best to always have data that is self-explanatory. 
Thus, we often use `.columns()` to rename the columns after melting:
```
df.columns(["Account", "Account Type", "Amount"])
```


