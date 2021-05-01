#### GRAPHS: CONCEPTUAL

# [Introduction to Graphs](https://www.codecademy.com/courses/complex-data-structures/lessons/conceptual-graphs/exercises/conceptual-graphs-intro)

Graphs are the perfect data structure for modeling networks, which make them an indispensable piece of your data structure toolkit. 
They’re composed of nodes, or vertices, which hold data, and edges, which are a connection between two vertices. 
A single node is a vertex.

Consider a map of the area where you live. 
As a graph, we could model bus stops as vertices, with bus routes between stops functioning as the edges.

What about the internet? 
Web pages can be vertices, and the hyperlinks which connect them are edges.

Real-world relationships modeled as graphs are numerous, making them an essential concept to master.
<p align="center">
  <img src="route_map.svg" width="600" alt="Introduction to Graphs" />
</p>

# [To Connect, or Not to Connect?](https://www.codecademy.com/courses/complex-data-structures/lessons/conceptual-graphs/exercises/conceptual-graphs-connected)

Graphs have varying degrees of connection. 
The higher the ratio of edges to vertices, the more connected the graph.

This graph represents a social network; 
people are vertices and edges are friendships. 
`Ted` is adjacent to `Patty`, `Ron`, and `Alice` because an edge **directly connects** them.

We use a single line for an edge, but these friendships are **bi-directional**. 
`Patty` is friends with `Ron` and `Ron` is friends with `Patty`.

A ***path*** is vertices which are connected by any number of intermediate edges. 
The paths from `Alice` to `Patty` could go 
* `Alice` to `Ted` to `Patty` 
* **or**, `Alice` to `Ted` to `Ron` to `Patty`.

No path exists between `Sally` and `Ted`. 
When *no path exists between two vertices*, a graph is ***disconnected***.
<p align="center">
  <img src="disconnected_graph.svg" width="600" alt="disconnected graph" />
</p>








