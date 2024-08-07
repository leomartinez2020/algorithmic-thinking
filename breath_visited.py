from collections import deque

def bfs_visited(ugraph, start_node):
    """
    input: undirected graph g,
    output: set of all nodes visited by the algorithm
    uses deque data structure
    """
    queue = deque()
    visited = set([start_node])
    queue.append(start_node)
    while queue:
        j = queue.pop()
        for node in ugraph[j]:
            if node not in visited:
                visited.add(node)
                queue.append(node)
    return visited

def bfs_visited2(graph, i):
    """
    input: undirected graph g,
    output: set of all nodes visited by the algorithm
    """
    q = list()
    visited = set([i])
    q.append(i)
    while q:
        j = q.pop()
        for h in graph[j]:
            if h not in visited:
                visited.add(h)
                q.append(h)
    return visited

def cc_visited(ugraph):
    """
    input: an undirected graph
    output: set of connected components
    """
    remaining_nodes = set(ugraph.keys())
    connected_component = []
    while remaining_nodes:
        node = remaining_nodes.pop()
        visited = bfs_visited(ugraph, node)
        connected_component.append(visited)
        remaining_nodes -= visited
    return connected_component

def largest_cc_size(ugraph):
    """
    takes the undirected graph ugraph
    and returns the size of the
    largest connected component in ugraph
    """
    return max([len(item) for item in cc_visited(ugraph)])

def compute_resilience(ugraph, attack_order):
    """
    input: undirected graph ugraph and a list of nodes attack_order
    For each node in the list, the function removes the given node and its
    edges from the graph and then computes the size of the largest connected
    component for the resulting graph.

    output: a list whose k+1th entry is the size of the largest connected component
    in the graph after the removal of the first k nodes in attack_order. The first entry
    (indexed by zero) is the size of the largest connected component in the original graph.
    """
    components_sizes = [largest_cc_size(ugraph)]
    for node in attack_order:
        for elem in ugraph[node]:
            ugraph[elem].discard(node)
        del ugraph[node]
        current_size = largest_cc_size(ugraph)
        components_sizes.append(current_size)
    return components_sizes

from grafos import GRAPH2

def test_graphs():
    grafos = [GRAPH1, GRAPH2]
    for GRAPH in grafos:
        print('nuevo grafo')
        print(f'graph: {GRAPH}')
        print(f'visited: {cc_visited(GRAPH)}')
        print(f'largest size: {largest_cc_size(GRAPH)}')
        print()

def test_resilience():
    grafos = [GRAPH1, GRAPH2]
    nodos = [1, 3]
    for ugraph in grafos:
        print(f'ugraph: {ugraph}')
        print(compute_resilience(ugraph, nodos))
        print()

import random

def test_seven():
    ugraph = GRAPH2
    nodes = list(range(len(ugraph)))
    random.shuffle(nodes)
    nodos = nodes[:5]
    print(compute_resilience(ugraph, nodos))

test_seven()
