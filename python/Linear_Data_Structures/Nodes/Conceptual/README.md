#### NODES: CONCEPTUAL
# [Nodes Introduction](https://www.codecademy.com/courses/linear-data-structures/lessons/learn-nodes-general/exercises/general-nodes-intro)
Nodes are the fundamental building blocks of many computer science data structures. 
They form the basis for **linked lists**, **stacks**, **queues**, **trees**, and more.

An individual node contains data and links to other nodes. 
Each data structure adds additional constraints or behavior to these features to create the desired structure.

[Cheatsheet](https://www.codecademy.com/learn/linear-data-structures/modules/cspath-nodes/cheatsheet)

# [Nodes Detail](https://www.codecademy.com/courses/linear-data-structures/lessons/learn-nodes-general/exercises/general-nodes-detail)
The data contained within a node can be a variety of types, depending on the language you are using. 
In the previous example, it was an integer (the number `5`), but it could be a string (`"five"`), decimal (`5.1`), an array (`[5,3,4]`) or nothing (`null`).

The link or links within the node are sometimes referred to as pointers. 
This is because they “point” to another node.

Typically, data structures implement nodes with one or more links. 
If these links are `null`, it denotes that you have reached the end of the particular node or link path you were previously following.

# [Node Linking](https://www.codecademy.com/courses/linear-data-structures/lessons/learn-nodes-general/exercises/general-nodes-link)
Often, due to the data structure, nodes may only be linked to from a single other node. 
This makes it very important to consider how you implement modifying or removing nodes from a data structure.

If you inadvertently remove the single link to a node, that node’s data and any linked nodes could be “lost” to your application. 
When this happens to a node, it is called an *orphaned* node.

# [Nodes Review](https://www.codecademy.com/courses/linear-data-structures/lessons/learn-nodes-general/exercises/general-nodes-review)
Nodes:
* Contain data, which can be a variety of data types
* Contain links to other nodes. If a node has no links, or they are all null, you have reached the end of the path you were following.
* Can be orphaned if there are no existing links to them
