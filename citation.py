from grafos import in_degree_distribution

filename = 'alg_phys-cite.txt'

def create_graph_from_file(fname):
    answer_graph = {}
    with open(fname) as fhandler:
        for line in fhandler:
            add_line_to_graph(answer_graph, line)
    return answer_graph

def add_line_to_graph(graph, line):
    neighbors = line.split(' ')
    node = int(neighbors[0])
    graph[node] = set([])
    for neighbor in neighbors[1 : -1]:
        graph[node].add(int(neighbor))

def compute_indegree_dist():
    g = create_graph_from_file(filename)
    indist= in_degree_distribution(g)
    print(indist)

#compute_indegree_dist()
