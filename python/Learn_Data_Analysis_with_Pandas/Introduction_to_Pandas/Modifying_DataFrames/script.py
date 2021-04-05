import codecademylib
import pandas as pd

orders = pd.read_csv('shoefly.csv')
# 1:
print(orders.head())
# 2:
orders["shoe_source"] = orders.shoe_material.apply(lambda material: "animal" if material == "leather" else "vegan")
# 3:
orders["salutation"] = orders.apply(lambda row: "Dear Mr. " + row.last_name if row.gender == "male" else "Dear Ms. " + row.last_name, axis = 1)

print(orders.head())
