# graphalgs.py
# by Ryan Neubauer and Jacob Vanderwilt
# Program uses the graph.py module to represent some graphing
# algorithms in python
from graph import *
from itertools import *

def bruteclique(g, k):
    # Brute force solution to k-clique
    cliques = []
    for comb in combinations(g.vertices, k):
        if isclique(comb, g):
            cliques.append(comb)
    return cliques

def isclique(comb, g):
    # Helper function for the brute force solution to k-clique
    for perm in permutations(comb, len(comb)):
        # This part ends up calling has_edge more than it needs to
        # if this comment is still here, that means I never got the time
        # to come try and fix it.
        for p in perm[1:]:
            if not(g.has_edge(perm[0], p)):
                return False
    return True


def DFS(g, start):
    return dfs(g, start, [])

def dfs(g, v, path):
    path.append(v)
    for w in g.adjacent(v):
        if w not in path:
            dfs(g, w, path)
    return path