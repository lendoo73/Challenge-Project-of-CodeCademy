# Define your functions
def coffe_bot():
  print("Welcome to the cafe!")
  ordered = {}
  order_coffe(ordered)
  while reorder_coffe() == "y":
    order_coffe(ordered)
  drinks = ""
  for drink, qty in ordered.items():
    drinks += "\n    * {} {}".format(qty, drink)
  print("Alright, that's a {}!".format(drinks))
  name = ""
  while name == "":
    name = input("Can I get your name please?\n> ")
  print("Thanks, {}! Your drink will be ready shortly.".format(name))

def order_coffe(ordered):
  print("ordered", ordered)
  size = get_size()
  drink_type = get_drink_type()
  order = "{} {}".format(size, drink_type)
  if order not in ordered:
    ordered[order] = 1
  else:
    ordered[order] += 1

def reorder_coffe():
  res = input("""Would you like to order another drink?
[Y]es
[N]o
> """)
  return res if res == "y" or res == "n" else print_message(reorder_coffe)


def get_size():
  res = input("'What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ")
  size = {
    "a": "small",
    "b": "medium",
    "c": "large"
  }
  return size[res] if res in size else print_message(get_size)

def get_drink_type():
  res = input("""What type of drink would you like?
[a] Brewed Coffee
[b] Mocha
[c] Latte
> """)
  drink_type = {
    "a": "brewed coffee",
    "b": "mocha",
    "c": order_latte
  }

  if res == "c": return drink_type["c"]()

  return drink_type[res] if res in drink_type else print_message(get_drink_type)

def order_latte():
  res = input("""And what kind of milk for your latte?
[a] 2% milk
[b] Non-fat milk
[c] Soy milk
> """)
  latte_type = {
    "a": "latte",
    "b": "non-fat latte",
    "c": "soy latte"
  }
  return latte_type[res] if res in latte_type else print_message(order_latte)

def print_message(callback):
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
  return callback()

# Call coffee_bot()!
coffe_bot()
