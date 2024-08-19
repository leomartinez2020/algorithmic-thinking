from create_undirected_graph import make_er_ugraph, make_upa_graph

from module2_create_graph import load_graph, NETWORK_FILE

NUM_EDGES = 1239

def count_edges(graph):
    counter = 0
    for key in graph:
        counter += len(graph[key])
    return counter

def test():
    grafo_network = load_graph(NETWORK_FILE)
    network_edges = count_edges(grafo_network)

    grafo_er = make_er_ugraph(NUM_EDGES, 0.002)
    er_edges = count_edges(grafo_er)

    grafo_upa = make_upa_graph(NUM_EDGES, 3)
    upa_edges = count_edges(grafo_upa)

    print(f'length grafo network: {len(grafo_network)}')
    print(f'edges grafo network: {network_edges}')
    print()

    print(f'length grafo ER: {len(grafo_er)}')
    print(f'edges grafo network: {er_edges}')
    print()

    print(f'length grafo UPA: {len(grafo_upa)}')
    print(f'edges grafo UPA: {upa_edges}')

test()
