def search_loop(graph):
    """Search for a loop in a graph.
    Algorithm is based on depth-first search. O(V+E)"""
    visited = set()
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, graph, visited, -1):
                return True
    return False


def dfs(vertex, graph, visited, parent):
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            if dfs(neighbor, graph, visited, vertex):
                return True
        elif parent != neighbor:
            return True


if __name__ == '__main__':
    g0 = {'a': {'b'},
          'b': {'a', 'c'},
          'c': {'b', 'd', 'e'},
          'd': {'c'},
          'e': {'c'}}
    print('g0: ', search_loop(g0))
    g1 = {'a': {'b'},
          'b': {'a', 'c'},
          'c': {'b', 'd', 'e'},
          'd': {'c', 'e'},
          'e': {'c', 'd'}}
    print('g1: ', search_loop(g1))
    g2 = {'a': {'b'},
          'b': {'a', 'c'},
          'c': {'b', 'd', 'e'},
          'd': {'c', 'f'},
          'e': {'c', 'f'},
          'f': {'d', 'e'}}
    print('g2: ', search_loop(g2))
    g3 = {'a': {'b'},
          'b': {'a', 'c'},
          'c': {'b', 'd', 'e'},
          'd': {'c', 'f', 'e'},
          'e': {'c', 'f', 'd'},
          'f': {'d', 'e'}}
    print('g3: ', search_loop(g3))
    g4 = {'a': {'b'},
          'b': {'a', 'c'},
          'c': {'b', 'd', 'e'},
          'd': {'c', 'e'},
          'e': {'c', 'd'},
          'f': {'a', 'g'},
          'g': {'a', 'f'}}
    print('g4: ', search_loop(g4))
