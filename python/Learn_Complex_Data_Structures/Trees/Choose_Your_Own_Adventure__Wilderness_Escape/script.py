# Our Story Begins
# 1 - 2.
print("Once upon a time...")
######
# TREENODE CLASS
######
# 3. Define a TreeNode class
class TreeNode():
  # 4 - 5. constructor
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []

  # 12 - 13.
  def add_child(self, node):
    self.choices.append(node)
  
  # 19.
  def traverse(self):
    # 20. This variable will track the current portion of the story:
    story_node = self
    print(story_node.story_piece)
    # 23.
    while len(story_node.choices):
      # 24.
      choice = input("Enter 1 or 2 to continue the story: ")
      # 25.
      if choice not in ["1", "2"]:
        print("Please enter a valid choice...")
      else:
        # 26 - 27. the user has made a valid choice
        chosen_index = int(choice) - 1
    # the story is over
        # 28.
        chosen_child = story_node.choices[chosen_index]
        # 29.
        print(chosen_child.story_piece)
        # 30.
        story_node = chosen_child



######
# VARIABLES FOR TREE
######
# 6.
story_root = TreeNode(
  """
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
"""
)
# 14 - 15.
choice_a = TreeNode(
  """
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
"""
)

choice_b = TreeNode(
  """
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
"""
)

# 32.
choice_a_1 = TreeNode(
  """
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.
 
YOU HAVE ESCAPED THE WILDERNESS.
"""
)
# 33.
choice_a_2 = TreeNode(
  """
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.
 
YOU REMAIN LOST.
"""
)

# 36.
choice_b_1 = TreeNode(
  """
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.
 
YOU REMAIN LOST.
"""
)

# 37.
choice_b_2 = TreeNode(
  """
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.
 
YOU HAVE ESCAPED THE WILDERNESS.
"""
)

# 16 - 17 - 18.
story_root.add_child(choice_a)
story_root.add_child(choice_b)

# 34.
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)

# 38.
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)

# Taking Input From the User
# 8 - 9 - 10 - 11.
user_choice = input("What is your name? ")
print(user_choice)

######
# TESTING AREA
######
# 7.
#print(story_root.story_piece)
# 21, 31., 35, 39.. 
story_root.traverse()
