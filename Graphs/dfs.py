def dfs(vertex, graph, used):
    """Depth-first search is an algorithm for traversing
    and searching tree or graph data structures. O(V+E)"""
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


def dfs_using_stack(graph):
    used = set()
    stack = []
    ccs = 0
    for vertex in graph:
        if vertex not in used:
            stack.append(vertex)
            while stack:
                vertex = stack.pop()
                used.add(vertex)
                for neighbour in graph[vertex]:
                    if neighbour not in used:
                        stack.append(neighbour)
            ccs += 1
    return ccs


if __name__ == '__main__':
    undirected_graph = dict(a={'b'}, b={'a', 'c'}, c={'b'}, d=set())
    g2 = {'a': {'b', 'c'},
          'b': {'a', 'd', 'e'},
          'c': {'a', 'f', 'g'},
          'd': {'b'},
          'e': {'b', 'h'},
          'f': {'c', 'k'},
          'g': {'c'},
          'h': {'e'},
          'k': {'f'}}
    print(connect_component_search(undirected_graph))
    print(dfs_using_stack(g2))
