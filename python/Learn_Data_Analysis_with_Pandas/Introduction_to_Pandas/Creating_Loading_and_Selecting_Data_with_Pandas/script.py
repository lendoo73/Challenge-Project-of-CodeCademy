import codecademylib
import pandas as pd
# 1:
orders = pd.read_csv("shoefly.csv")
# 2:
print(orders.head())
# 3:
emails = orders.email
print(emails)
# 4:
frances_palmer = orders[
  (orders.first_name == "Frances") &
  (orders.last_name == "Palmer")
]
print(frances_palmer)
# 5:
comfy_shoes = orders[
  (orders.shoe_type == "clogs") |
  (orders.shoe_type == "boots") |
  (orders.shoe_type == "ballet flats")
]
print(comfy_shoes)
