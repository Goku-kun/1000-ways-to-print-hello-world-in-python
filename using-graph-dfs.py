# A program to print 'Hello, World!' by Depth-first search in graph

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

  def DFS(self, visited, start, goal):
    visited.append(self.graph[start])
    print(self.graph[start]["value"], end='')

    for neighbour in self.graph[start]["connections"]:
      if neighbour not in visited:
        self.DFS(visited, neighbour, goal)

  def start_DFS(self, start, goal):
    visited = []
    self.DFS(visited, start, goal)
    print()

#


graph = Graph()

graph.addEdge(0,  'h', [1, 7])
graph.addEdge(1,  'e', [2, 5])
graph.addEdge(2,  'l', [3, 4])
graph.addEdge(3,  'l', [])
graph.addEdge(4,  'o', [])
graph.addEdge(5,  ',', [6])
graph.addEdge(6,  ' ', [])
graph.addEdge(7,  'w', [8])
graph.addEdge(8,  'o', [9, 12])
graph.addEdge(9,  'r', [10, 11])
graph.addEdge(10, 'l', [])
graph.addEdge(11, 'd', [])
graph.addEdge(12, '!', [])

graph.start_DFS(0, 12)
