def topological_sort(graph):
    """Linear topological ordering of a directed graph.
    Algorithm is based on depth-first search. O(V+E)"""
    visited = set()
    result = []
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex, graph, visited, result)
    result[:] = result[::-1]
    return result


def dfs(vertex, graph, visited, result):
    visited.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs(neighbour, graph, visited, result)
    result.append(vertex)


if __name__ == '__main__':
    g1 = {1: {2, 3, 4}, 2: {5, 6}, 3: {6, 9}, 4: {7, 9}, 5: {8}, 6: {5, 7, 8},
         7: {8}, 8: set(), 9: set()}
    g2 = {'a': {'b', 'c'},
          'b': {'d', 'e'},
          'c': {'f', 'g'},
          'd': set(),
          'e': {'h'},
          'f': {'i', 'h'},
          'g': set(),
          'h': {'i'},
          'i': {'j'},
          'j': {'k', 'l'},
          'k': set(),
          'l': set()}
    print(topological_sort(g2))
