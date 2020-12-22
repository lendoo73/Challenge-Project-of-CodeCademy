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
This will show you the number of game states in the tree.
parameters:
* `board`: 
* `turn`: `"X"` or `"O"`

## `select_space()`
parameters:
* `board`: The board that you’re making the move on.
* `column`: The column you’re selecting.
* `turn`: `"X"` or `"O"`; The type of piece you’re putting in column.

---
## [Depth and Base Case](https://www.codecademy.com/courses/machine-learning/lessons/advanced-minimax/exercises/base-case)

The first strategy we’ll use to handle these enormous trees is stopping the recursion early. 
There’s no need to go all the way to the leaves! 
We’ll just look a few moves ahead.

Being able to stop before reaching the leaves is critically important for the efficiency of this algorithm. 
It could take literal days to reach the leaves of a game of chess. 
Stopping after only a few levels limits the algorithm’s understanding of the game, but it makes the runtime realistic.

In order to implement this, we’ll add another parameter to our function called `depth`. Every time we make a recursive call, we’ll decrease `depth` by `1`.
We’ll also have to edit our base case condition. We now want to stop if the game is over (we’ve hit a leaf), or if `depth` is `0`.
```
def minimax(input_board, minimizing_player, depth):
  # Base Case:
  if game_is_over(input_board) or depth == 0:
    ...
    ...
  
  # Recursive Call:
  hypothetical_value = minimax(new_board, True, depth - 1)[0]
```

## [Evaluation Function](https://www.codecademy.com/courses/machine-learning/lessons/advanced-minimax/exercises/evaluation-function)

By adding the depth parameter to our function, we’ve prevented it from spending days trying to reach the end of the tree. 
But we still have a problem: our evaluation function doesn’t know what to do if we’re not at a leaf.
Right now, we’re returning positive infinity if Player 1 has won, negative infinity if Player 2 has won, and `0` otherwise. 
Unfortunately, since we’re not making it to the leaves of the board, neither player has won and we’re always returning `0`.

Writing an evaluation function takes knowledge about the game you’re playing.
It is the part of the code where a programmer can infuse their creativity into their AI.
If you’re playing Chess, your evaluation function could count the difference between the number of pieces each player owns. 
If white had 15 pieces, and black had 10 pieces, the evaluation function would return `5`. 
This evaluation function would make an AI that prioritizes capturing pieces above all else.

You could go even further — some pieces might be more valuable than others. 
Your evaluation function could keep track of the value of each piece to see who is ahead. 
This evaluation function would create an AI that might really try to protect their queen. 
You could even start finding more abstract ways to value a game state. 
Maybe the position of each piece on a Chess board tells you something about who is winning.

It’s up to you to define what you value in a game. 
These evaluation functions could be incredibly complex.
If the maximizing player is winning (by your definition of what it means to be winning), then the evaluation function should return something greater than 0. 
If the minimizing player is winning, then the evaluation function should return something less than 0.

## [Alpha-Beta Pruning](https://www.codecademy.com/courses/machine-learning/lessons/advanced-minimax/exercises/pruning)

By writing an evaluation function that works on non-leaf game states, we can stop the recursion early. 
But in a perfect world, we’d still want to reach the leaves of the tree. 
In order to traverse farther down the tree without dramatically increasing the runtime, we can implement a technique called alpha-beta pruning.
The core idea behind alpha-beta pruning is to ignore parts of the tree that we know will be dead ends.
For example, consider the gif.
When determining the “value” of the node labeled E, we can stop looking at possible moves as soon as it discovers the `8` node.

We know that B will only consider values less than or equal to `5`, and E will only consider values greater than or equal to `8`. We know that node B will never care about E’s value and we can stop looking through E’s moves.
![Alpha-Beta Pruning]()




