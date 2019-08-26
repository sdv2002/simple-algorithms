def number_of_edges(graph):
    """Count the number of edges in a graph."""
    edges = set()
    for vertex in graph:
        for neighbor in graph[vertex]:
            if (neighbor + vertex) not in edges:
                edges.add(vertex + neighbor)
    return len(edges)


if __name__ == '__main__':
    g1 = {'a': {'b', 'c'},
          'b': {'a', 'd', 'e'},
          'c': {'a', 'f', 'g'},
          'd': {'b'},
          'e': {'b', 'h'},
          'f': {'c', 'i', 'g', 'h'},
          'g': {'c', 'f'},
          'h': {'e', 'f', 'i'},
          'i': {'f', 'h', 'j'},
          'j': {'k', 'l', 'i'},
          'k': {'j', 'l'},
          'l': {'j', 'k'},
          'm': {'n'},
          'n': {'m'}}
    print(number_of_edges(g1))
