# ----- Ground Shipping ----- 
def cost_ground_shipping(weight):
  ground_flat_charge = 20
  if weight <= 2:
    price = 1.50
  elif weight <= 6:
    price = 3
  elif weight <= 10:
    price = 4
  else:
    price = 4.75
  return price * weight + ground_flat_charge


# ----- Ground Shipping Premium ----- 
cost_ground_shipping_premium = 125

# ----- Drone Shipping ----- 
def cost_drone_shipping(weight):
  if weight <= 2:
    price = 4.50
  elif weight <= 6:
    price = 9
  elif weight <= 10:
    price = 12
  else:
    price = 14.25
  return price * weight


def get_cheapest(weight):
  ground_shipping = cost_ground_shipping(weight)
  drone_shipping = cost_drone_shipping(weight)
  price = ground_shipping

  if ground_shipping < drone_shipping:
    method = "Ground Shipping"
  elif ground_shipping > drone_shipping:
    method = "Drone Shipping"
    price = drone_shipping
  else:
    method = "Ground or Drone Shipping"
  
  if price > cost_ground_shipping_premium:
    method = "Ground Shipping Premimium"
    price = cost_ground_shipping_premium
  elif price == cost_ground_shipping_premium:
    method = "Any Shipping"
  
  return method, price

weight = 4.8
print(f"Ground Shipping ${cost_ground_shipping(weight):.2f}")
print(f"Ground Shipping Premimium ${cost_ground_shipping_premium:.2f}")
print(f"Drone Shipping ${cost_drone_shipping(weight):.2f}")

# What is the cheapest method of shipping a 4.8 pound package and how much would it cost?
method, price = get_cheapest(weight)
print("\nWhat is the cheapest method of shipping a 4.8 pound package and how much would it cost?")
print(f"The cheapest method: {method}")
print(f"The price is: ${price:.2f}")
