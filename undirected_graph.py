
"""
Input: nodes, n, probability p

Output: a graph g = (V, E) where g belongs to G(n, p)

V <- {0, 1, ..., n - 1}
E <- {}
foreach {i, j} subset of V, where i != j do
    a <- random(0, 1)
    if a < p then
        E <- E Union {{i, j}}
return g = (V, E)
"""

import itertools
import random

def grow_graph(ugraph, pair):
    ugraph[pair[0]].add(pair[1])
    ugraph[pair[1]].add(pair[0])
    return ugraph

def make_ugraph(n, p):
    nodes = range(n)
    seqs = [set([]) for _ in nodes]
    ugraph = dict(zip(nodes, seqs))
    v_perm = itertools.permutations(nodes, 2)
    for pair in v_perm:
        a = random.random()
        if a < p:
            ugraph = grow_graph(ugraph, pair)
    return ugraph

print(make_ugraph(5, 0.3))
