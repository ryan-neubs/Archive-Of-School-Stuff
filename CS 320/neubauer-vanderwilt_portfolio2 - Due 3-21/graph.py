# graph.py
# by Ryan Neubauer and Jacob Vanderwilt
# Graph class to allow implementation of graph algorithms

class Graph:
    def __init__(self, vertices, directed=False):
        self.vertices = vertices
        self.directed = directed
        self.adjacency = {}
        for v in vertices:
            self.adjacency[v] = {}

    def add_edge(self, vertex1, vertex2, weight=1):
        self.adjacency[vertex1][vertex2] = weight
        if not self.directed: self.adjacency[vertex2][vertex1] = weight

    def has_edge(self, v1, v2):
        "returns a Boolean indicating v1 is adjacent"
        return v2 in self.adjacency[v1]
    
    def weight(self, v1, v2):
        "returns the weight of edge from v2 to v1"
        return self.adjacency[v1][v2]

    def vertex_iter(self):
        "returns an iterator for vertices"
        return iter(self.adjacency.keys())

    def edge_iter(self):
        "returns iterator for edges"
        return iter(self.adjacency.values())

    def adjacent(self, v):
        "returns adjacency list from v as a dictionary"
        return self.adjacency[v]

def fromfile(file):
    with open(file) as f:
        d = f.readline().strip()
        if d == 'directed':
            d = True
        else: d = False
        v = f.readline().strip().split()
        g = Graph(v,d)
        for line in f:
            edge = line.split()
            v1, v2 = edge[0], edge[1]
            if len(edge) == 3:
                w = int(edge[2])
                g.add_edge(v1,v2,w)
            else: g.add_edge(v1,v2)
    return g
