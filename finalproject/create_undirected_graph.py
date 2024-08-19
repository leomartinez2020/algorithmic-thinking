
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

from collections import deque
import csv
import itertools
import random
import pandas as pd

from alg_upa_trial import UPATrial

from module2_create_graph import load_graph, NETWORK_FILE

NUM_EDGES = 1239

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

def random_order(graph):
    """
    Takes a graph and returns a list of the nodes in the graph in
    some random order
    """
    nodes = list(graph.keys())
    random.shuffle(nodes)
    return nodes

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
    try:
        return max([len(item) for item in cc_visited(ugraph)])
    except ValueError:
        return 0

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
        if ugraph.get(node):
            for elem in ugraph[node]:
                ugraph[elem].discard(node)
            del ugraph[node]
        current_size = largest_cc_size(ugraph)
        components_sizes.append(current_size)
    return components_sizes

def test():
    grafo_network = load_graph(NETWORK_FILE)
    grafo_er = make_er_ugraph(NUM_EDGES, 0.002)
    grafo_upa = make_upa_graph(NUM_EDGES, 3)

    attack_order = random_order(grafo_network)

    list_net = compute_resilience(grafo_network, attack_order)
    net_text = ' '.join([str(elem) for elem in list_net])

    list_er = compute_resilience(grafo_er, attack_order)
    er_text = ' '.join([str(elem) for elem in list_er])

    list_upa = compute_resilience(grafo_upa, attack_order)
    upa_text = ' '.join([str(elem) for elem in list_upa])

    # dictionary of lists
    diccio = {'network': list_net, 'er_net': list_er, 'upa_net': list_upa}
    df = pd.DataFrame(diccio)
    # saving the dataframe
    df.to_csv('resilience.csv')

test()
