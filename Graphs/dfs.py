def dfs(vertex, graph, used):
    """Depth-first search is an algorithm for traversing
    or searching tree or graph data structures."""
    used.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs(neighbour, graph, used)


def connect_component_search(graph):
    """Search connected components of an undirected graph"""
    used = set()
    n = 0
    for vertex in graph:
        if vertex not in used:
            dfs(vertex, graph, used)
            n += 1
    return n


if __name__ == '__main__':
    undirected_graph = dict(a={'b'}, b={'a', 'c'}, c={'b'}, d=set())
    print(connect_component_search(undirected_graph))
