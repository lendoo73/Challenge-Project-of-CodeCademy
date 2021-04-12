from util import Loot

def knapsack(loot, weight_limit):
  grid = [[0 for col in range(weight_limit + 1)] for row in range(len(loot) + 1)]
  for row, item in enumerate(loot):
    row = row + 1
    for col in range(weight_limit + 1):
      weight_capacity = col
      if item.weight <= weight_capacity:
        item_value = item.value
        item_weight = item.weight
        previous_best_less_item_weight = grid[row - 1][weight_capacity - item_weight]
        capacity_value_with_item = item_value + previous_best_less_item_weight
        capacity_value_without_item = grid[row - 1][col]
        grid[row][col] = max(capacity_value_with_item, capacity_value_without_item)
      else:
        # If the item doesn’t fit, we want to use the previous best:
        grid[row][col] = grid[row - 1][col]

  return grid[-1][-1]
    
available_loot = [Loot("Clock", 3, 8), Loot("Vase", 4, 12), Loot("Diamond", 1, 7)]
weight_capacity = 4
best_combo = knapsack(available_loot, weight_capacity)
print("The ideal loot given capacity {0} is\n{1}".format(weight_capacity, best_combo))
