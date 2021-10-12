# A program to print 'Hello, World!' by Breadth-first search in graph

class Graph:
  def __init__(self):
    self.graph = {}

  def addEdge(self, uid, value, connections):
    vertex = {
      "uid": uid,
      "value": value,
      "connections": connections
    }
    self.graph[uid] = vertex

  def BFS(self, start):
    visited = [self.graph[start]]
    queue = [self.graph[start]["uid"]]
    
    while queue:
      current_vertex_i = queue.pop(0)
      print (self.graph[current_vertex_i]["value"], end='')

      for neighbour in self.graph[current_vertex_i]["connections"]:
        if neighbour not in visited:
          queue.append(neighbour)
          visited.append(neighbour)
    print()
#


graph = Graph()

graph.addEdge(0,  'h', [1,2,3,4])
graph.addEdge(1,  'e', [5,6])
graph.addEdge(2,  'l', [7,8])
graph.addEdge(3,  'l', [9,10])
graph.addEdge(4,  'o', [11,12])
graph.addEdge(5,  ',', [])
graph.addEdge(6,  ' ', [])
graph.addEdge(7,  'w', [])
graph.addEdge(8,  'o', [])
graph.addEdge(9,  'r', [])
graph.addEdge(10, 'l', [])
graph.addEdge(11, 'd', [])
graph.addEdge(12, '!', [])

graph.BFS(0)
