# topsort.py
# by Ryan Neubauer and Jacob Vanderwilt
from graph import *

def topsort(g):
    indegree = {}
    result = []
    for v in g.vertex_iter():
        indegree[v] = 0
    for v in g.vertex_iter():
        for v2 in g.adjacent(v):
            indegree[v2] += 1
    while indegree:
        source = None
        for v in sorted(indegree):
            if indegree[v] == 0:
                source = v
                result.append(source)
                break
        if source == None:
            return -1
        indegree.pop(source)
        for v in g.adjacent(source):
            indegree[v] -= 1
    return result
