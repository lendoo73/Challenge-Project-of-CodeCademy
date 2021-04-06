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





















