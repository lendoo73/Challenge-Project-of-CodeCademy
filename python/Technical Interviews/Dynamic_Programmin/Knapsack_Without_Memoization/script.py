from util import powerset, Loot

def knapsack(loot, weight_limit):
  best_value = None
  all_combo = powerset(loot)

  for combo in all_combo:
    combo_weight = sum([item.weight for item in combo])
    combo_value = sum([item.value for item in combo])
    if combo_weight <= weight_limit:
      if not best_value or combo_value > best_value:
        best_value = combo_value
  
  if best_value == None:
    print("knapsack couldn't fit any items")
  return best_value
    
available_loot = [Loot("Clock", 3, 8), Loot("Vase", 4, 12), Loot("Diamond", 1, 7)]
weight_capacity = 4
best_combo = knapsack(available_loot, weight_capacity)
print("The ideal loot given capacity {0} is\n{1}".format(weight_capacity, best_combo))
