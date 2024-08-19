
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

from alg_upa_trial import UPATrial

def grow_er_graph(ugraph, pair):
    """
    Add links to nodes
    """
    node0 = pair[0]
    node1 = pair[1]
    ugraph[node0].add(node1)
    ugraph[node1].add(node0)
    return ugraph

def make_er_ugraph(n, p):
    """
    Create a random undirected ER graph
    n is number of nodes, p is probability
    output is an undirected graph like {0: {2}, 1: {2}, 2: {0, 1}}
    """
    nodes = range(n)
    seqs = [set([]) for _ in nodes]
    ugraph = dict(zip(nodes, seqs))
    v_perm = itertools.permutations(nodes, 2)
    for pair in v_perm:
        a = random.random()
        if a < p:
            ugraph = grow_er_graph(ugraph, pair)
    return ugraph

def make_upa_graph(n, m):
    """
    n is the final number of node
    m is the number of existing nodes, m is fixed
    generate undirected UPA graphs, makes use of the UPATrial class
    """
    graph = make_er_ugraph(m, 1.0)
    #print(f'graph init: {graph}')
    upa = UPATrial(m)
    for val in range(m, n):
        new_set = upa.run_trial(m)
        #print(f'new_set: {new_set}')
        graph[val] = new_set
        for node in new_set:
            graph[node].add(val)
    #print(f'graph final: {graph}')
    return graph

#make_upa_graph(5, 3)
