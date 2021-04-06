import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')

cheap_shoes = orders.groupby("shoe_color").price.apply(lambda price: np.percentile(price, 25)).reset_index()
cheap_shoes.rename(columns = {"price": "cheap price"}, inplace = True)
print(cheap_shoes)
