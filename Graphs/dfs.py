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
    ccs = 0
    for vertex in graph:
        if vertex not in used:
            dfs(vertex, graph, used)
            ccs += 1
    return ccs


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
    g1 = dict(a={'b'}, b={'a', 'c'}, c={'b'}, d=set())
    g2 = {'a': {'b', 'c'},
          'b': {'a', 'd', 'e'},
          'c': {'a', 'f', 'g'},
          'd': {'b'},
          'e': {'b', 'h'},
          'f': {'c', 'i', 'g', 'h'},
          'g': {'c', 'f'},
          'h': {'e', 'f', 'i'},
          'i': {'f', 'h'},
          'j': {'k', 'l'},
          'k': {'j', 'l'},
          'l': {'j', 'k'}}
    print(connect_component_search(g1))
    print(dfs_using_stack(g2))
