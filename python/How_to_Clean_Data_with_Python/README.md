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

# [Dealing with Duplicates](https://www.codecademy.com/courses/practical-data-cleaning/lessons/pandas-data-cleaning/exercises/duplicates)
Often we see duplicated rows of data in the DataFrames we are working with. 
This could happen due to errors in data collection or in saving and loading the data.

To check for duplicates, we can use the pandas function `.duplicated()`, which will return a Series telling us which rows are duplicate rows.

We can use the pandas `.drop_duplicates()` function to remove all rows that are duplicates of another row.

If we wanted to remove every row with a duplicate value in the `item` column, we could specify a subset:
```
fruits = fruits.drop_duplicates(
  subset = ['item']
)
```
By default, this keeps the first occurrence of the duplicate.

Make sure that the columns you drop duplicates from are specifically the ones ***where duplicates don’t belong***. 
You wouldn’t want to drop duplicates with the `price` column as a subset, for example, because it’s okay if multiple items cost the same amount!

# [Splitting by Index](https://www.codecademy.com/courses/practical-data-cleaning/lessons/pandas-data-cleaning/exercises/splitting-index)
In trying to get clean data, we want to make sure each column represents one type of measurement. 
Often, multiple measurements are recorded in the same column, and we want to separate these out so that we can do individual analysis on each variable.

Let’s say we have a column `birthday` with data formatted in `MMDDYYYY` format. 
In other words, `11011993` represents a birthday of `November 1, 1993`. 
We want to split this data into `day`, `month`, and `year` so that we can use these columns as separate features.

In this case, we know the exact structure of these strings. 
The *first two characters* will always correspond to the `month`, the *second two* to the `day`, and the *rest of the string* will always correspond to `year`. 
We can easily break the data into three separate columns by splitting the strings using `.str`:
```
# Create the 'month' column
df['month'] = df.birthday.str[0:2]
 
# Create the 'day' column
df['day'] = df.birthday.str[2:4]
 
# Create the 'year' column
df['year'] = df.birthday.str[4:]
```
The first command takes the first two characters of each value in the `birthday` column and puts it into a `month` column. 
The second command takes the second two characters of each value in the `birthday` column and puts it into a `day` column. 
The third command takes the rest of each value in the `birthday` column and puts it into a `year` column.

# [Splitting by Character](https://www.codecademy.com/courses/practical-data-cleaning/lessons/pandas-data-cleaning/exercises/splitting-char)
Let’s say we have a column called `type` with data entries in the format `admin_US` or `user_Kenya`. 
Just like we saw before, this column actually contains two types of data. 
One seems to be the user type (with values like `admin` or `user`) and one seems to be the `country` this user is in (with values like `US` or `Kenya`).

We can no longer just split along the first 4 characters because `admin` and `user` are of different lengths. 
Instead, we know that we want to split along the `_`. 
Using that, we can split this column into two separate, cleaner columns:
```
# Create the 'str_split' column
df['str_split'] = df.type.str.split('_')
 
# Create the 'usertype' column
df['usertype'] = df.str_split.str.get(0)
 
# Create the 'country' column
df['country'] = df.str_split.str.get(1)
```

# [Looking at Types](https://www.codecademy.com/courses/practical-data-cleaning/lessons/pandas-data-cleaning/exercises/dtypes)
Each column of a DataFrame can hold items of the same *data type* or *dtype*. 
The **dtypes** that pandas uses are: `float`, `int`, `bool`, `datetime`, `timedelta`, `category` and `object`. 
Often, we want to convert between types so that we can do better analysis. 
If a numerical category like `num_users` is stored as a Series of objects instead of ints, 
for example, it makes it more difficult to do something like make a line graph of users over time.

To see the types of each column of a DataFrame, we can use:
```
print(df.dtypes)
```
The `dtype` of the `dtypes` attribute itself is an `object`! It is a `Series` object. Series objects compose all DataFrames.

# [String Parsing](https://www.codecademy.com/courses/practical-data-cleaning/lessons/pandas-data-cleaning/exercises/string-parsing-i)
Sometimes we need to modify strings in our DataFrames to help us transform them into more meaningful metrics. 
For example, in our fruits table from before:
| item |	price |	calories
| --- | :---: | :---:
| banana |	$1 |	105
| apple |	$0.75 |	95
| peach |	$3 |	55
| peach |	$4 |	55
| clementine |	$2.5 |	35

We can see that the `price` column is actually composed of strings representing dollar amounts. 
This column could be much better represented in floats, so that we could take the mean, calculate other aggregate statistics, or compare different fruits to one another in terms of price.

First, we can use what we know of regex to get rid of all of the dollar signs:
```
fruit.price = fruit['price'].replace(
    '[\$,]', 
    '', 
    regex = True
)
```
Then, we can use the pandas function `.to_numeric()` to convert strings containing numerical values to integers or floats:
```
fruit.price = pd.to_numeric(fruit.price)
```

# [More String Parsing](https://www.codecademy.com/courses/practical-data-cleaning/lessons/pandas-data-cleaning/exercises/string-parsing-ii)
Sometimes we want to do analysis on numbers that are hidden within string values. 
We can use regex to extract this numerical data from the strings they are trapped in. 
Suppose we had this DataFrame df representing a workout regimen:
| date |	exerciseDescription
| --- | ---
| 10/18/2018 |	lunges - 30 reps
| 10/18/2018 |	squats - 20 reps
| 10/18/2018 |	deadlifts - 25 reps
| 10/18/2018 |	jumping jacks - 30 reps
| 10/19/2018 |	lunges - 40 reps
| 10/19/2018 |	chest flyes - 15 reps













