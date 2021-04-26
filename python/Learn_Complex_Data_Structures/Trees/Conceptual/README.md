#### [Cheatsheet](https://www.codecademy.com/learn/complex-data-structures/modules/cspath-trees/cheatsheet)

#### TREES: CONCEPTUAL

# [Trees Introduction](https://www.codecademy.com/courses/complex-data-structures/lessons/learn-trees-general/exercises/general-trees-intro)

Trees are an essential data structure for storing hierarchical data with a directed flow.

Similar to linked lists and graphs, trees are composed of nodes which hold data. 
The diagram represents nodes as rectangles and data as text.

Nodes also store references to zero or more other tree nodes. 
Data moves down from node to node. 
We depict those references as lines drawn between rectangles.

Trees are often displayed with a single node at the top and connected nodes branching downwards.

![Tree](TreeNode.svg)

# [Tree Detail](https://www.codecademy.com/courses/complex-data-structures/lessons/learn-trees-general/exercises/general-trees-detail)

Trees grow downwards in computer science, and a root node is at the very top. 
The ***root*** of this tree is `/photos`.

`/photos` references to two other nodes: 
* `/safari` 
* and `/wedding`. 

`/safari` and `/wedding` are ***children*** or ***child*** nodes of `/photos`.

Conversely, `/photos` is a ***parent*** node because it ***has child nodes***.

`/safari` and `/wedding` ***share the same parent*** node, which makes them ***siblings***.

Note that the `/safari` node is child (to `/photos`) and parent (to `lion.jpg` and `giraffe.jpg`). 
It’s extremely common to have nodes act as both parent and child to different nodes within a tree.

When a node has ***no children***, we refer to it as a ***leaf*** node.






















