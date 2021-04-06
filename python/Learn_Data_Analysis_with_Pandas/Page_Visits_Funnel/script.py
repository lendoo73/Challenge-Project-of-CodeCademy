import pandas as pd

visits = pd.read_csv(
    'visits.csv',
    parse_dates = [1]
)
cart = pd.read_csv(
    'cart.csv',
    parse_dates = [1]
)
checkout = pd.read_csv(
    'checkout.csv',
    parse_dates = [1]
)
purchase = pd.read_csv(
    'purchase.csv',
    parse_dates = [1]
)
# 1:
#print(visits.head())
#print(cart.head())
#print(checkout.head())
#print(purchase.head())

# 2:
visits_cart = visits.merge(cart, how = "left")
#print(visits_cart)
# 3:
len_visits_cart = len(visits_cart)
#print(visits_cart.shape[0])
#print(len_visits_cart)
# 4:
no_checkout = len(visits_cart[visits_cart.cart_time.isnull()])
#print(no_checkout)
# 5:
percent_no_checkout = no_checkout / float(len_visits_cart) * 100
#print(percent_no_checkout)
# 6:
cart_checkout = cart.merge(checkout, how ="left")
#print(cart_checkout)
null_in_cart_checkout = len(cart_checkout[cart_checkout.checkout_time.isnull()])
percentage_null_in_cart_checkout = float(null_in_cart_checkout) / len(cart_checkout) * 100
#print(percentage_null_in_cart_checkout)
# 7:
all_data = visits.merge(cart, how = "left").merge(checkout, how = "left").merge(purchase, how = "left")
#print(all_data.head())
#print(all_data.shape[0])
only_checkout = all_data[(all_data.checkout_time.notnull()) & (all_data.purchase_time.isnull())]
#print(only_checkout)
#print(only_checkout.shape[0] / float(all_data.shape[0]) * 100)
# 8:
def percentage_of_null(step1, step2):
  return all_data[
      (all_data[step1 + "_time"].notnull()) & 
      (all_data[step2 + "_time"].isnull())
  ].shape[0] / float(all_data[all_data[step1 + "_time"].notnull()].shape[0]) * 100
# 9:
visit_to_cart = percentage_of_null("visit", "cart")
cart_to_checkout = percentage_of_null("cart", "checkout")
checkout_to_purchase = percentage_of_null("checkout", "purchase")

weakest = visit_to_cart if visit_to_cart > cart_to_checkout  else cart_to_checkout
weakest = weakest if weakest > checkout_to_purchase else checkout_to_purchase
#print(weakest)
# 10:
all_data["time_to_purchase"] = all_data.purchase_time - all_data.visit_time
# 11:
#print(all_data.time_to_purchase)
# 12:
print(all_data.time_to_purchase.mean())

