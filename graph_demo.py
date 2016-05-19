#Representation of an undirected graph using dictionary

graph = {
    "a": ["c"],
    "b":["c","e"],
    "c":["a","b","d","e"],
    "d":["c"],
    "e":["c","b"],
    "f":[]
    }

## function to generate the list of all edges:

def graph_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node,neighbour))
    return edges


def isolated_edges(graph):
    """returns a list of isolated nodes"""
    isolated_nodes = []
    for node in graph:
        if not graph[node]:
            isolated_nodes += node
    return isolated_nodes


 

















