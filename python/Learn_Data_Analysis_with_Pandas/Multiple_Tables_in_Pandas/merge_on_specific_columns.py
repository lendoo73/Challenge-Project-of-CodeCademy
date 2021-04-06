import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)

orders_products = orders.merge(products.rename(columns = {"id": "customer_id"}))
print(orders_products)
