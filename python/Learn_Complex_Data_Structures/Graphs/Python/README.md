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

We’re keeping things organized by storing our classes in separate files, so let’s do a brief review on how to use code from another file.

Python gives us the ability to import code from another file. 
Here’s how we can use our `Vertex` class from within **graph.py**.
```py
# from <file_name> import <class>
 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# inside of ./vertex.py file
class Vertex
  # code for the class...
 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# inside of ./graph.py file
from vertex import Vertex
 
my_vertex = Vertex("Import Accomplished!")
```

# [Building the Graph II](https://www.codecademy.com/courses/complex-data-structures/lessons/python-graphs/exercises/python-graphs-graph-ii)

We’d like our `Graph` class to be able to set edges between the stored vertices. 
An instance of `Graph` is either directed or undirected, which affects how edges work between two vertices. 
As a reminder, the `Graph` class defaults to being undirected with edges being set in both directions.

The good news is our `Vertex` class already has an `.add_edge()` method, so we can delegate most of the work.

The `Graph` version of `.add_edge()` will take a “from” and a “to” vertex, and set the appropriate edges by calling the `Vertex` instance’s own `.add_edge()`.
```py
undirected_railway = Graph()
directed_railway = Graph(True)
 
callan_station = Vertex('callan')
peel_station = Vertex('peel')
 
undirected_railway.add_vertex(callan_station)
undirected_railway.add_vertex(peel_station)
 
directed_railway.add_vertex(callan_station)
directed_railway.add_vertex(peel)
 
directed_railway.add_edge(callan_station, peel_station)
# directed graph will set the edge one-way
print(callan_station.get_edges())
# ['peel']
print(peel_station.get_edges())
# []
 
undirected_railway.add_edge(callan_station, peel_station)
# directed graph will set the edge both ways
print(callan_station.get_edges())
# ['peel']
print(peel_station.get_edges())
# ['callan']
```
Within **graph.py**:
```py
  def add_edge(self, from_vertex, to_vertex):
    print(f"Adding edge from {from_vertex.value} to {to_vertex.value}")
    self.graph_dict[from_vertex.value].add_edge(to_vertex.value)

    if not self.directed:
      # bi-direction graph
      self.graph_dict[to_vertex.value].add_edge(from_vertex.value)
```

# [Adding Weight](https://www.codecademy.com/courses/complex-data-structures/lessons/python-graphs/exercises/python-graphs-weight)

So far our `Vertex` class has stored edges inside of a dictionary with keys of the connected vertex’s name and the value simply set to `True`.

We can make our implementation support edge weights with a few small changes. 
To keep this class as flexible as possible, we’ll introduce a default `weight` argument to `.add_edge()` in the `Graph` and `Vertex` classes. 
With no explicit `weight` argument, it will default to `0`. 
We’ll then set the appropriate value in the dictionary to that `weight`.

Weighted edges allow us to make graphs that represent rail systems with a travel-time between stations.
```py
railway = Graph()
 
callan = Vertex('callan')
peel = Vertex('peel')
harwick = Vertex('harwick')
 
railway.add_vertex(callan)
railway.add_vertex(peel)
railway.add_vertex(harwick)
 
# Travel-time between callan and peel: 12
railway.add_edge(callan, peel, 12)
# Travel-time between harwick and callan: 7
railway.add_edge(harwick, callan, 7)
 
print(callan.edges)
# { 'peel': 12 }
print(harwick.edges)
# { 'callan': 7 }
```
Inside **vertex.py**:
```py
  def add_edge(self, vertex, weight = 0):
    self.edges[vertex] = weight
```
Tab over to **graph.py**:
```py
  def add_edge(self, from_vertex, to_vertex, weight = 0):
    self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
    if not self.directed:
      self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)
```

# [Finding a Path I](https://www.codecademy.com/courses/complex-data-structures/lessons/python-graphs/exercises/python-graphs-path-i)

Our railway has grown to four stations with two connecting tracks. 
How can we tell a passenger which stations are reachable from Harwick?
```py
undirected_railway = Graph()
 
callan_station = Vertex('callan')
peel_station = Vertex('peel')
ulfstead_station = Vertex('ulfstead')
harwick_station = Vertex('harwick')
 
undirected_railway.add_vertex(callan_station)
undirected_railway.add_vertex(peel_station)
undirected_railway.add_vertex(harwick_station)
undirected_railway.add_vertex(ulfstead_station)
 
undirected_railway.add_edge(peel_station, harwick_station)
undirected_railway.add_edge(peel_station, callan_station)
```
Our `Graph` class needs to determine whether a path exists between two vertices. 
A path means two vertices which are connected by a sequence of one or more intermediary edges and graphs.
```py
  def find_path(self, start_vertex, end_vertex):
    print(f"Searching from {start_vertex} to {end_vertex}...")
    start = [start_vertex]

    while len(start):
      current_vertex = start.pop(0)
      print(current_vertex)
```

# [Finding a Path II](https://www.codecademy.com/courses/complex-data-structures/lessons/python-graphs/exercises/python-graphs-path-ii)

Our pathfinding method is almost complete. 
Let’s take a step back and think how a passenger in Harwick station could find their way to Callan.

First, they’d look for all the stations connected to Harwick. 
If one of those stations was Callan, they’re in luck!

Otherwise, they would look for the connections from each of those stations excluding Harwick because they’ve already crossed it off their list.

We’ll take the same strategy with our pathfinding method.
```py
while len(start) > 0:
  current_vertex = start.pop(0)
  # current_vertex is end_vertex
    # a path exists!
  # current_vertex is not end_vertex
    # add vertices connected to 
    # current_vertex onto the list
    # to keep searching for a path
```
```py
  def find_path(self, start_vertex, end_vertex):
    start = [start_vertex]
    while len(start) > 0:
      current_vertex = start.pop(0)
      print("Visiting " + current_vertex)
      #START CODE HERE
      if current_vertex == end_vertex:
        return True
      
      vertex = self.graph_dict[current_vertex]
      next_vertices = vertex.get_edges()
      start += next_vertices
    
    return False
```

# [Refactoring Path-Finding](https://www.codecademy.com/courses/complex-data-structures/lessons/python-graphs/exercises/python-graphs-path-refactor)

Our pathfinding method works when a path exists, but there is a serious bug! 
We’re not accounting for cycles in our graph.

Consider the following undirected `Graph`:
```py
railway = Graph()
 
callan = Vertex('callan')
peel = Vertex('peel')
ulfstead = Vertex('ulfstead')
harwick_station = Vertex('harwick')
 
railway.add_vertex(callan)
railway.add_vertex(peel)
railway.add_vertex(harwick)
railway.add_vertex(ulfstead)
 
railway.add_edge(peel, harwick)
railway.add_edge(harwick, callan)
railway.add_edge(callan, peel)
 
railway.find_path(peel, ulfstead)
```
Peel connects to Harwick and Callan. 
We look for a path starting at `peel`, adding `harwick` and `callan` to the start list. 
Next, we look at `harwick`, adding `peel` and `callan`. 
We’ll keep adding the same vertices, and our loop will never terminate.

When a path exists, return `True` will exit the loop. 
When a path does not exist, it’s a major problem!

We’ll use a dictionary to track which stations we’ve visited. 
This will stop our passengers from riding around in circles.
```py
  def find_path(self, start_vertex, end_vertex):
    start = [start_vertex]
    # Checkpoint 1, replace these comments:
    # Use a dictionary to track which
    # vertices we've already visited
    seen = {}

    while len(start) > 0:
      current_vertex = start.pop(0)
      # Checkpoint 2, replace these comments:
      # Update the `seen` variable
      # now that we've visited current_vertex
      seen[current_vertex] = True
      print("Visiting " + current_vertex)
      if current_vertex == end_vertex:
        return True
      else:
        vertex = self.graph_dict[current_vertex]
        next_vertices = vertex.get_edges()
        
        # Filter next_vertices so it only
        # includes vertices NOT IN seen
        
        # Checkpoint 3, uncomment and replace the question marks:
        next_vertices = [vertex for vertex in next_vertices if vertex not in seen]
        start.extend(next_vertices)
        
    return False
 ```
