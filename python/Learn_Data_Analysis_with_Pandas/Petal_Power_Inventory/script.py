import codecademylib
# 1:
import pandas as pd

inventory = pd.read_csv("inventory.csv")

# 2:
#print(inventory.head(10))
# 3:
staten_island = inventory.head(10)
#print(staten_island)
# 4:
product_request = staten_island.product_description
#print(product_request)
# 5:
seed_request = inventory[(inventory.location == "Brooklyn") & (inventory.product_type == "seeds")]
#print(seed_request)
# 6:
is_in_stock = lambda row: True if row.quantity else False
inventory["in_stock "] = inventory.apply(is_in_stock, axis = 1)
#print(inventory.head())
# 7:
inventory["total_value"] = inventory.price * inventory.quantity
#print(inventory.head())
# 8-9:
combine_lambda = lambda row: "{} - {}".format(row.product_type, row.product_description)
inventory["full_description"] = inventory.apply(combine_lambda, axis = 1)
print(inventory.head())

