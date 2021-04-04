from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
# 2-3.:
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
# 4.:
stacks.extend([left_stack, middle_stack, right_stack])
#Set up the Game
# 5-6.:
num_disks = int(input("""
How many disks do you want to play with?
"""))

# 7-8.:
while num_disks < 3:
  num_disks = int(input("""
Enter a number greater than or equal to 3
"""))
# 9-10.:
for disk in range(num_disks, 0, -1):
  left_stack.push(disk)

# 11-12.:
num_optimal_moves = 2 ** num_disks - 1
print(f"""
The fastest you can solve this game is in {num_optimal_moves} moves
""")

#Get User Input
# 13-14.:
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  # 15-17.:
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      # 18.:
      print(f"Enter {letter} for {name}")
    # 19-20.:
    user_input = input("").upper()
    # 21.:
    if user_input in choices:
      for i in range(len(stacks)):
        # 22-23.:
        if user_input == choices[i]:
          return stacks[i]
        
#Play the Game
# 24.:
num_user_moves = 0
# 25:
while right_stack.get_size() != num_disks:
  # 26.:
  print("""


...Current Stacks...""")
  for stack in stacks:
    stack.print_items()
  
  # 27-28.:
  while True:
    print("""
Which stack do you want to move from?
""")
    from_stack = get_input()
    print("""
Which stack do you want to move to?
""")
    to_stack = get_input()
    # 29.:
    if from_stack.is_empty():
      print("""
Invalid Move. Try Again
""")
    # 30.:
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    # 31.:
    else: print("""
Invalid Move. Try Again
""")

# 32-33.:
print(f"""
You completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}
""")
