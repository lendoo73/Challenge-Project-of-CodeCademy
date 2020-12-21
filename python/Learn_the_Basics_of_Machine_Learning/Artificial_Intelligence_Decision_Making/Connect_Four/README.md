# [Connect Four](https://www.codecademy.com/courses/machine-learning/lessons/advanced-minimax/exercises/tree-size)

In our Tic-Tac-Toe on the minimax algorithm, we wrote a program that could play the perfect game of Tic-Tac-Toe. 
Our AI looked at all possible future moves and chose the one that would be most beneficial. 
This was a viable strategy because Tic Tac Toe is a small enough game that it wouldn’t take too long to reach the leaves of the game tree.

However, there are games, like Chess, that have much larger trees. 
There are 20 different options for the first move in Chess, compared to 9 in Tic-Tac-Toe.
On top of that, the number of possible moves often increases as a chess game progresses. 
Traversing to the leaves of a Chess tree simply takes too much computational power.

We’ll investigate two techniques to solve this problem:
* The first technique puts a hard limit on how far down the tree you allow the algorithm to go.
* The second technique uses a clever trick called pruning to avoid exploring parts of the tree that we know will be useless.

---
## `tree_size()`
