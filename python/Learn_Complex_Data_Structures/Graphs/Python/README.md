#### GRAPHS: PYTHON

# [Introduction to Graphs](https://www.codecademy.com/courses/complex-data-structures/lessons/python-graphs/exercises/python-graphs-intro)

In this lesson, we’ll build a robust implementation of the graph data structure. 
With just two classes, `Vertex` and `Graph`, we can implement a variety of graphs that satisfy the requirements of many algorithms.

Let’s detail the functionality we require from these classes:
* `Vertex` stores some data.
* `Vertex` stores the edges to connected vertices and their weight.
* `Vertex` can add a new edge to its collection.
* `Graph` stores all the vertices.
* `Graph` knows if it is directed or undirected.
* `Graph` can add a new vertex to its collection.
* `Graph` can add a new edge between stored vertices.
* `Graph` can tell whether a path exists between stored vertices.

Since we’re dealing with multiple classes, we’ll use multiple files for this implementation. 
To keep the concepts grounded in a real-world application, we’ll build up a transportation network of railroads and train stations as we go.

# [Building the Vertex](https://www.codecademy.com/courses/complex-data-structures/lessons/python-graphs/exercises/python-graphs-vertex-i)

Let’s start with our `Vertex` class. 
This class is responsible for storing information about individual vertices in our graph. 
In our railway network, instances of `Vertex` will represent train stations.

An instance of `Vertex` will store data and a Python dictionary which tracks other `Vertex` instances connected to `self`.
```py
class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def get_edges(self): 
    return list(self.edges.keys())

station = Vertex("Cronk")
```

# [Building the Vertex II](https://www.codecademy.com/courses/complex-data-structures/lessons/python-graphs/exercises/python-graphs-vertex-ii)

We’ll continue building out the `Vertex` class. Remember, it’s responsible for knowing which other vertices are connected. 
These connections are the edges of our graph implementation.

A key in the `Vertex` instance’s `edges` dictionary represents a connection to that other vertex. 
For now, we can just set the value to be `True`.
```py
grand_central = Vertex('Grand Central Station')
forty_second_street = Vertex('42nd Street Station')
 
print(grand_central.get_edges())
# []
 
grand_central.add_edge(forty_second_street)
print(grand_central.edges)
# { "42nd Street Station": True }
print(grand_central.get_edges())
# ["42nd Street Station"]
```
Let’s add this functionality to our `Vertex` class!
```py
  def add_edge(self, vertex):
    print(f"Adding edge to {vertex}")
    self.edges[vertex] = True
```

# [Building the Graph I](https://www.codecademy.com/courses/complex-data-structures/lessons/python-graphs/exercises/python-graphs-graph-i)

We’ve built a class to store information and connections between individual vertices, but we need another class that keeps track of the big picture.

Our `Graph` class will track all the vertices and handle higher level concerns like whether the graph is **directed**, 
requiring edges to have a set direction, **or undirected**, allowing bi-directional movement across edges.

We’ll start by giving `Graph` the functionality to add vertices. 
We’ll use an internal `graph_dict` property to store every vertex by its value pointing to the vertex instance itself.

We want to do the following:
```py
grand_central = Vertex("Grand Central Station")
railway = Graph()
 
print(railway.graph_dict)
# {}
railway.add_vertex(grand_central)
print(railway.graph_dict)
# {"Grand Central Station": grand_central}
```
```py
class Graph:
  def __init__(self, directed = False):
    self.directed = directed
    self.graph_dict = {}
  
  def add_vertex(self, vertex):
    print(f"Adding {vertex.value}")
    self.graph_dict[vertex.value] = vertex
```

# [Import Interlude](https://www.codecademy.com/courses/complex-data-structures/lessons/python-graphs/exercises/python-graphs-import-interlude)









