import itertools
import random

def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and returns
    a dictionary corresponding to a complete directed
    graph with the specified number of nodes
    """
    if num_nodes <= 0:
        return dict()
    graph = dict()
    nodes = list(range(num_nodes))
    for node in nodes:
        graph[node] = set(nodes) - set([node])
    return graph

def compute_in_degrees(digraph):
    """
    Takes a directed graph digraph
    (represented as a dictionary) and computes
    the in-degrees for the nodes in the graph
    """
    all_nodes = set(digraph.keys())
    nodes_added = set()
    in_degrees = dict()
    for node in digraph:
        for out_node in digraph[node]:
            if out_node not in in_degrees:
                in_degrees[out_node] = 1
                nodes_added.add(out_node)
            else:
                in_degrees[out_node] += 1
    nodes_missing = all_nodes - nodes_added
    for node in nodes_missing:
        in_degrees[node] = 0
    return in_degrees

def in_degree_distribution(digraph):
    """
    Takes a directed graph digraph
    (represented as a dictionary) and computes
    the unnormalized distribution of the in-degrees
    of the graph
    """
    in_degrees_distribution = dict()
    in_degrees = compute_in_degrees(digraph)
    for value in in_degrees.values():
        if value not in in_degrees_distribution:
            in_degrees_distribution[value] = 1
        else:
            in_degrees_distribution[value] += 1
    return in_degrees_distribution


def get_random_directed_graph(n, p):
    """
    n is the number of nodes, p is probability
    """
    graph = dict()
    vertices = range(n)
    print(f'vertices: {vertices}')
    #for node in vertices:
    #    graph[node] = set([])
    print(f'grafo: {graph}')
    v_perm = itertools.permutations(vertices, 2)
    for pair in v_perm:
        print(f'edge: {pair}')
        node1, node2 = pair
        if not graph.get(node1):
            graph[node1] = set([])
        a = random.random()
        if a < p:
            graph[node1].add(node2)
    return graph

def erre(n, p):
    graph = dict()
    vertices = range(n)
    print(f'vertices: {vertices}')
    for node in vertices:
        graph[node] = set([])
    print(f'grafo: {graph}')
    v_perm = itertools.permutations(vertices, 2)
    for pair in v_perm:
        print(f'edge: {pair}')
        a = random.random()
        if a < p:
            graph[pair[0]].add(pair[1])
    return graph

val = erre(4, 0.5)
print(val)
print('===' * 12)
print(in_degree_distribution(val))

print()
grafo = get_random_directed_graph(4, 0.5)
print(grafo)
print(in_degree_distribution(grafo))
