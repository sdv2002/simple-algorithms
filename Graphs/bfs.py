from collections import deque
from pprint import pprint


def bfs(graph, start_vertex, end_vertex):
    """Breadth-first search is an algorithm for traversing
    and searching tree or graph data structures. O(V+E)"""
    distances = {vertex: None for vertex in graph}
    parents = {vertex: None for vertex in graph}
    path = []
    distances[start_vertex] = 0
    queue = deque([start_vertex])

    while queue:
        current_vertex = queue.popleft()
        for neighbour in graph[current_vertex]:
            if distances[neighbour] is None:
                distances[neighbour] = distances[current_vertex] + 1
                parents[neighbour] = current_vertex
                queue.append(neighbour)

    while parents[end_vertex] is not None:
        path.append(end_vertex)
        end_vertex = parents[end_vertex]
    path.append(start_vertex)
    path[:] = path[::-1]

    return [distances, parents, path]


if __name__ == '__main__':
    g1 = {0: {1, 10, 11, 12},
          1: {0, 7},
          2: {6},
          3: {11},
          4: {6, 10},
          5: {8, 13},
          6: {2, 4, 10},
          7: {1, 13},
          8: {5, 12},
          9: {11},
          10: {0, 4, 6},
          11: {0, 3, 9, 12, 14},
          12: {0, 8, 11},
          13: {5, 7},
          14: {11}}
    g2 = {'a': {'b', 'c'},
          'b': {'a', 'd', 'e'},
          'c': {'a', 'f', 'g'},
          'd': {'b'},
          'e': {'b', 'h'},
          'f': {'c', 'k'},
          'g': {'c'},
          'h': {'e'},
          'k': {'f'}}

    pprint(bfs(g2, 'a', 'k')[2])
    pprint(bfs(g1, 0, 5)[2])
