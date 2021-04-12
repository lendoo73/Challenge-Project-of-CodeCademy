#### TECHNICAL INTERVIEW PROBLEMS: DYNAMIC PROGRAMMING

# [Knapsack Without Memoization](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-dynamic-programming/exercises/dynamic-programming-naive-knapsack)

Dynamic programming is especially helpful for problems where there are many different options and we have a particular goal we’re trying to maximize.

For the sake of learning, we’re going to imagine ourselves as burglars. 
We’ve broken into someone’s home and there are many different things we can steal.

Each item has a weight and a value. 
Our goal is to maximize the total value of items while remaining within the weight we can fit in our knapsack.

This is another ideal situation to apply dynamic programming, but to start we’ll use the brute force approach and generate every single possible combination.

We can total each combination’s weight and value to find the most lucrative collection.

To help, we’re given a `Loot` class with `name`, `weight`, and `value` properties.

computer = Loot("Computer", 2, 12)
print(computer)
# Computer: 
#     weighs 2,
#     valued at 12, 
We also have a powerset() function which creates a list of all combinations.

fruits = ['apple', 'orange', 'grape']
fruit_combinations = power_set(fruits)
print(fruit_combinations)
#[(), ('apple',), ('orange',), ('grape',), ('apple', 'orange'), ('apple', 'grape'), ('orange', 'grape'), ('apple', 'orange', 'grape')]
 
Note: Codecademy does not endorse thievery!
