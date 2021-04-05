import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')

pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()
print(type(pricey_shoes))
pricey_shoes.rename(columns = {"price": "Most Expensive"}, inplace = True)
print(pricey_shoes)
