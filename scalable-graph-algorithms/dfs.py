from collections import defaultdict

class Graph:
  def __init__(self, V):
    self.V = V;
    self.g = defaultdict(list);

  def addEdge(self, s, e):
    self.g[s].append(e);


  def dfs(self, s):
    visited = set()
    stk = [s]
    while(len(stk)>0):
      v = stk.pop()

      if(v not in visited):
        visited.add(v);
        stk.extend(self.g[v])
        print(v)



g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)

s = 2 ; d = 3

g.dfs(s)
