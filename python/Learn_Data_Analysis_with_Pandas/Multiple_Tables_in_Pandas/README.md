#### WORKING WITH MULTIPLE DATAFRAMES

# [Introduction: Multiple DataFrames](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-multiple-tables/exercises/intro)

In order to efficiently store data, we often spread related information across multiple tables.

For instance, imagine that we own an e-commerce business and we want to track the products that have been ordered from our website.

We could have one table with all of the following information:

* `order_id`
* `customer_id`
* `customer_name`
* `customer_address`
* `customer_phone_number`
* `product_id`
* `product_description`
* `product_price`
* `quantity`
* `timestamp`

However, a lot of this information would be repeated. 
If the same customer makes multiple orders, that customer’s name, address, and phone number will be reported multiple times. 
If the same product is ordered by multiple customers, then the product price and description will be repeated. 
This will make our orders table big and unmanageable.

So instead, we can split our data into three tables:
* **`orders`** would contain the information necessary to describe an order: `order_id`, `customer_id`, `product_id`, `quantity`, and `timestamp`
* **`products`** would contain the information to describe each product: `product_id`, `product_description` and `product_price`
* **`customers`** would contain the information for each customer: `customer_id`, `customer_name`, `customer_address`, and `customer_phone_number`

In this lesson, we will learn the Pandas commands that help us work with data stored in multiple tables.

# [Inner Merge I](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-multiple-tables/exercises/inner-merge)

Suppose we have the following three tables that describe our eCommerce business:

* `orders` — a table with information on each transaction:

| order_id |	customer_id |	product_id |	quantity |	timestamp
| --- | --- | --- | --- | --- 
| 1 |	2 |	3 |	1 |	2017-01-01
| 2 |	2 |	2 |	3 |	2017-01-01
| 3 |	3 |	1 |	1 |	2017-01-01
| 4 |	3 |	2 |	2 |	2017-02-01
| 5 |	3 |	3 |	3 |	2017-02-01
| 6 |	1 |	4 |	2 |	2017-03-01
| 7 |	1 |	1 |	1 |	2017-02-02
| 8 |	1 |	4 |	1 | 	2017-02-02

* `products` — a table with product IDs, descriptions, and prices:

| product_id |	description |	price
| --- | --- | ---
| 1 |	thing-a-ma-jig |	5
| 2 |	whatcha-ma-call-it |	10
| 3 |	doo-hickey |	7
| 4 |	gizmo |	3

* `customers` — a table with customer names and contact information:

| customer_id |	customer_name |	address |	phone_number
| --- | --- | --- | ---
| 1 |	John Smith |	123 Main St. |	212-123-4567
| 2 |	Jane Doe |	456 Park Ave. |	949-867-5309
| 3 |	Joe Schmo |	798 Broadway |	112-358-1321

If we just look at the **`orders`** table, we can’t really tell what’s happened in each order. 
However, if we refer to the other tables, we can get a more complete picture.

Let’s examine the order with an `order_id` of `1`. 
It was purchased by Customer 2. 
To find out the customer’s name, we look at the **`customers`** table and look for the item with a `customer_id` value of `2`. 
We can see that Customer 2’s name is Jane Doe and that she lives at 456 Park Ave.

Doing this kind of matching is called **merging** two DataFrames.

# [Inner Merge II](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-multiple-tables/exercises/inner-merge-ii)

It is easy to do this kind of matching for one row, but hard to do it for multiple rows.

Luckily, Pandas can efficiently do this for the entire table. 
We use the `.merge` method.

The `.merge` method looks for columns that are common between two DataFrames and then looks for rows where those column’s values are the same. 
It then combines the matching rows into a single row in a new table.

We can call the `pd.merge` method with two tables like this:
```
new_df = pd.merge(orders, customers)
```
This will match up all of the customer information to the orders that each customer made.

# [Inner Merge III](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-multiple-tables/exercises/inner-merge-iii)

In addition to using `pd.merge`, each DataFrame has its own `merge` method. 
For instance, if you wanted to merge `orders` with `customers`, you could use:
```
new_df = orders.merge(customers)
```
This produces the same DataFrame as if we had called `pd.merge(orders, customers)`.

We generally use this when we are joining more than two DataFrames together because we can “chain” the commands. 
The following command would merge `orders` to `customers`, and then the resulting DataFrame to `products`:
```
big_df = orders.merge(customers).merge(products)
```

# [Merge on Specific Columns](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-multiple-tables/exercises/left-on)

In the previous example, the `merge` function “knew” how to combine tables based on the columns that were the same between two tables. 
For instance, `products` and `orders` both had a column called `product_id`. 
This won’t always be true when we want to perform a merge.

Generally, the `products` and `customers` DataFrames would not have the columns `product_id` or `customer_id`. 
Instead, they would both be called `id` and it would be implied that the id was the `product_id` for the products table and `customer_id` for the customers table. 
They would look like this:

## Customers

| id |	customer_name |	address |	phone_number
| --- | --- | --- | ---
| 1 |	John Smith |	123 Main St. |	212-123-4567
| 2 |	Jane Doe |	456 Park Ave. |	949-867-5309
| 3	| Joe Schmo |	798 Broadway |	112-358-1321

## Products
| id |	description |	price
| --- | --- | ---
| 1 |	thing-a-ma-jig |	5
| 2 |	whatcha-ma-call-it |	10
| 3 |	doo-hickey |	7
| 4 |	gizmo |	3

**How would this affect our merges?**
Because the `id` columns would mean something different in each table, our default merges would be wrong.

One way that we could address this problem is to use `.rename` to rename the columns for our merges. 
In the example below, we will rename the column `id` to `customer_id`, so that `orders` and `customers` have a common column for the merge.
```
pd.merge(
    orders,
    customers.rename(columns = {'id': 'customer_id'})
)
```

# [Merge on Specific Columns II](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-multiple-tables/exercises/left-on-ii)

In the previous exercise, we learned how to use `rename` to merge two DataFrames whose columns don’t match.

If we don’t want to do that, we have another option. 
We could use the keywords `left_on` and `right_on` to specify which columns we want to perform the merge on. 
In the example below, the “left” table is the one that comes first (`orders`), and the “right” table is the one that comes second (`customers`). 
This syntax says that we should match the `customer_id` from orders to the `id` in customers.
```
pd.merge(
    orders,
    customers,
    left_on = 'customer_id',
    right_on = 'id'
)
```
If we use this syntax, we’ll end up with two columns called `id`, one from the first table and one from the second. 
Pandas won’t let you have two columns with the same name, so it will change them to `id_x` and `id_y`.

It will look like this:

| id_x |	customer_id |	product_id |	quantity |	timestamp |	id_y |	customer_name |	address	phone_number
| --- | --- | --- | --- | --- | --- | --- | --- 
| 1 |	2 |	3 |	1 |	2017-01-01 00:00:00 |	2 |	Jane Doe |	456 Park Ave |	949-867-5309
| 2 |	2 |	2 |	3 |	2017-01-01 00:00:00 |	2 |	Jane Doe |	456 Park Ave |	949-867-5309
| 3 |	3 |	1 |	1 |	2017-01-01 00:00:00 |	3 |	Joe Schmo |	789 Broadway |	112-358-1321
| 4 |	3 |	2 |	2 |	2016-02-01 00:00:00 |	3 |	Joe Schmo |	789 Broadway |	112-358-1321
| 5 |	3 |	3 |	3 |	2017-02-01 00:00:00 |	3 |	Joe Schmo |	789 Broadway |	112-358-1321
| 6 |	1 |	4 |	2 |	2017-03-01 00:00:00 |	1 |	John Smith |	123 Main St. |	212-123-4567
| 7 |	1 |	1 |	1 |	2017-02-02 00:00:00 |	1 |	John Smith |	123 Main St. |	212-123-4567
| 8 |	1 |	4 |	1 |	2017-02-02 00:00:00 |	1 |	John Smith |	123 Main St. |	212-123-4567

The new column names `id_x` and `id_y` aren’t very helpful for us when we read the table. 
We can help make them more useful by using the keyword `suffixes`. 
We can provide a list of suffixes to use instead of “_x” and “_y”.

For example, we could use the following code to make the suffixes reflect the table names:
```
pd.merge(
    orders,
    customers,
    left_on = 'customer_id',
    right_on = 'id',
    suffixes = ['_order', '_customer']
)
```
The resulting table would look like this:

| id_order |	customer_id |	product_id |	quantity |	timestamp |	id_customer |	customer_name |	address	phone_number
| --- | --- | --- | --- | --- | --- | --- | --- 
| 1 |	2 |	3 |	1 |	2017-01-01 00:00:00 |	2 |	Jane Doe |	456 Park Ave |	949-867-5309
| 2 |	2 |	2 |	3 |	2017-01-01 00:00:00 |	2 |	Jane Doe |	456 Park Ave |	949-867-5309
| 3 |	3 |	1 |	1 |	2017-01-01 00:00:00 |	3 |	Joe Schmo |	789 Broadway |	112-358-1321
| 4 |	3 |	2 |	2 |	2016-02-01 00:00:00 |	3 |	Joe Schmo |	789 Broadway |	112-358-1321
| 5 |	3 |	3 |	3 |	2017-02-01 00:00:00 |	3 |	Joe Schmo |	789 Broadway |	112-358-1321
| 6 |	1 |	4 |	2 |	2017-03-01 00:00:00 |	1 |	John Smith |	123 Main St. |	212-123-4567
| 7 |	1 |	1 |	1 |	2017-02-02 00:00:00 |	1 |	John Smith |	123 Main St. |	212-123-4567
| 8 |	1 |	4 |	1 |	2017-02-02 00:00:00 |	1 |	John Smith |	123 Main St. |	212-123-4567

# [Mismatched Merges](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-multiple-tables/exercises/mismatched-merge)

In our previous examples, there were always matching values when we were performing our merges. 
What happens when that isn’t true?

Let’s imagine that our `products` table is out of date and is missing the newest product: Product 5. 
What happens when someone orders it?

# [Outer Merge](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-multiple-tables/exercises/outer-merge)

In the previous exercise, we saw that when we merge two DataFrames whose rows don’t match perfectly, we lose the unmatched rows.

This type of merge (where we only include matching rows) is called an *inner merge*. 
There are other types of merges that we can use when we want to keep information from the unmatched rows.

Suppose that two companies, Company A and Company B have just merged. 
They each have a list of customers, but they keep slightly different data. 
Company A has each customer’s name and email. 
Company B has each customer’s name and phone number. 
They have some customers in common, but some are different.
<hr />
**`company_a`**

| name |	email
| --- | ---
| Sally Sparrow |	sally.sparrow@gmail.com
| Peter Grant |	pgrant@yahoo.com
| Leslie May |	leslie_may@gmail.com

**`company_b`**

| name |	phone
| --- | ---
| Peter Grant |	212-345-6789
| Leslie May |	626-987-6543
| Aaron Burr |	303-456-7891

If we wanted to combine the data from both companies without losing the customers who are missing from one of the tables, we could use an ***Outer Join***. 
An **Outer Join** would ***include all rows from both tables***, even if they don’t match. 
Any missing values are filled in with `None` or `nan` (which stands for “Not a Number”).
```
pd.merge(company_a, company_b, how = 'outer')
```
The resulting table would look like this:

| name |	email |	phone
| --- | --- | ---
| Sally Sparrow |	sally.sparrow@gmail.com |	nan
| Peter Grant |	pgrant@yahoo.com |	212-345-6789
| Leslie May |	leslie_may@gmail.com |	626-987-6543
| Aaron Burr |	nan |	303-456-7891

# [Left and Right Merge](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-multiple-tables/exercises/left-merge)

Let’s return to the merge of Company A and Company B.
<hr />

## Left Merge

Suppose we want to identify which customers are missing phone information. 
We would want a list of all customers who have `email`, but don’t have `phone`.

We could get this by performing a ***Left Merge***. 
A **Left Merge** includes *all rows from* the first (*left*) table, but *only rows from* the second (*right*) table *that match* the first table.

For this command, the order of the arguments matters. 
If the first DataFrame is `company_a` and we do a left join, we’ll only end up with rows that appear in `company_a`.

By listing `company_a` first, we get all customers from Company A, and only customers from Company B who are also customers of Company A.
```
pd.merge(company_a, company_b, how = 'left')
```
The result would look like this:

| name |	email |	phone
| --- | --- | ---
| Sally Sparrow |	sally.sparrow@gmail.com |	None
| Peter Grant |	pgrant@yahoo.com |	212-345-6789
| Leslie May |	leslie_may@gmail.com |	626-987-6543

Now let’s say we want a list of all customers who have phone but no email. 
We can do this by performing a **Right Merge**.

## Right Merge

Right merge is the exact opposite of left merge. 
Here, the merged table will include all rows from the second (right) table, but only rows from the first (left) table that match the second table.

By listing `company_a` first and `company_b` second, we get all customers from Company B, and only customers from Company A who are also customers of Company B.
```
pd.merge(company_a, company_b, how = "right")
```
The result would look like this:

| name |	email |	phone
| --- | --- | ---
| Peter Grant |	pgrant@yahoo.com |	212-345-6789
| Leslie May |	leslie_may@gmail.com |	626-987-6543
| Aaron Burr |	None |	303-456-7891

# [Concatenate DataFrames](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-multiple-tables/exercises/concatenate)

Sometimes, a dataset is broken into multiple tables. 
For instance, data is often split into multiple CSV files so that each download is smaller.

When we need to reconstruct a single DataFrame from multiple smaller DataFrames, we can use the method `pd.concat([df1, df2, df3, ...])`. 
This method only works ***if all of the columns are the same*** in all of the DataFrames.

For instance, suppose that we have two DataFrames:

**`df1`**
| name |	email
| --- | ---
| Katja Obinger |	k.obinger@gmail.com
| Alison Hendrix |	alisonH@yahoo.com
| Cosima Niehaus |	cosi.niehaus@gmail.com
| Rachel Duncan |	rachelduncan@hotmail.com

**`df2`**
| name |	email
| --- | ---
| Jean Gray |	jgray@netscape.net
| Scott Summers |	ssummers@gmail.com
| Kitty Pryde |	kitkat@gmail.com
| Charles Xavier |	cxavier@hotmail.com

If we want to combine these two DataFrames, we can use the following command:
```
pd.concat([df1, df2])
```
That would result in the following DataFrame:

| name |	email
| --- | ---
| Katja Obinger |	k.obinger@gmail.com
| Alison Hendrix |	alisonH@yahoo.com
| Cosima Niehaus |	cosi.niehaus@gmail.com
| Rachel Duncan |	rachelduncan@hotmail.com
| Jean Gray |	jgray@netscape.net
| Scott Summers |	ssummers@gmail.com
| Kitty Pryde |	kitkat@gmail.com
| Charles Xavier |	cxavier@hotmail.com

# [Review](https://www.codecademy.com/courses/data-processing-pandas/lessons/pandas-multiple-tables/exercises/review-ii)

This lesson introduced some methods for combining multiple DataFrames:

* Creating a DataFrame made by matching the common columns of two DataFrames is called a `merge`
* We can specify which columns should be matches by using the keyword arguments `left_on` and `right_on`
* We can combine DataFrames whose rows don’t all match using `left`, `right`, and `outer` merges and the `how` keyword argument
* We can stack or concatenate DataFrames with the same columns using `pd.concat`
