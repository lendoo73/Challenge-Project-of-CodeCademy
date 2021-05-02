from vertex import Vertex

class Graph:
  def __init__(self):
    self.graph_dict = {}

  def add_vertex(self, node):
    self.graph_dict[node.value] = node

  def add_edge(self, from_node, to_node, weight = 0):
    self.graph_dict[from_node.value].add_edge(to_node.value, weight)
    self.graph_dict[to_node.value].add_edge(from_node.value, weight)

  def explore(self):
    print("Exploring the graph....\n")
    #FILL IN EXPLORE METHOD BELOW
    # 18.
    current_room = "entrance"
    path_total = 0
    # 19.
    print(f"\nStarting off at the {current_room}\n")
    # 21.
    while current_room != "treasure room":
      # 22.
      node = self.graph_dict[current_room]
      # 26. gather the user’s input:
      valid_choices = set()
      
      # 23.
      for connected_room, weight in node.edges.items():
        # 24.
        key = connected_room[0]
        valid_choices.add(key)
        # 25.
        print(f"enter {key} for {connected_room}: {weight} cost")
      # 27.
      print(f"\nYou have accumulated: {path_total} cost")
      # 28 - 29.
      choice = input("\nWhich room do you move to? ")
      # 30. check to see if the user did NOT enter valid choice:
      if choice not in valid_choices:
        print(f"please select from these letters: {valid_choices}")
      # 31. the user selected a valid choice:
      else: 
        for room in node.edges.keys():
          # 32. 
          if room.startswith(choice):
            # 33.
            current_room = room
            # 34.
            path_total += node.edges[room]
        
        # 35.   
        print(f"\n*** You have chosen: {current_room} ***\n")
    
    # 36.
    print(f"Made it to the treasure room with {path_total} cost")

  def print_map(self):
    print("\nMAZE LAYOUT\n")
    for node_key in self.graph_dict:
      print("{0} connected to...".format(node_key))
      node = self.graph_dict[node_key]
      for adjacent_node, weight in node.edges.items():
        print("=> {0}: cost is {1}".format(adjacent_node, weight))
      print("")
    print("")

def build_graph():
  graph = Graph()
  
  # MAKE ROOMS INTO VERTICES BELOW...
  # 3.
  entrance = Vertex("entrance")
  # 6.
  ante_chamber = Vertex("ante-chamber")
  # 7.
  kings_room = Vertex("king's room")
  # 12.
  grand_gallery = Vertex("grand gallery")
  # 14.
  treasure_room = Vertex("treasure room")

  # ADD ROOMS TO GRAPH BELOW...
  # 4 - 5.
  graph.add_vertex(entrance)
  graph.add_vertex(ante_chamber)
  graph.add_vertex(kings_room)
  # 13.
  graph.add_vertex(grand_gallery)
  graph.add_vertex(treasure_room)


  # ADD EDGES BETWEEN ROOMS BELOW...
  # 9.
  graph.add_edge(entrance, ante_chamber, 7)
  graph.add_edge(entrance, kings_room, 3)
  # 11.
  graph.add_edge(kings_room, ante_chamber, 1)
  graph.add_edge(grand_gallery, ante_chamber, 2)
  graph.add_edge(grand_gallery, kings_room , 2)
  # 15.
  graph.add_edge(treasure_room, ante_chamber, 6)
  graph.add_edge(treasure_room, grand_gallery, 4)

  # DON'T CHANGE THIS CODE
  graph.print_map()
  return graph
