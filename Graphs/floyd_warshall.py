from pprint import pprint


def floyd_warshall(graph):
    """Floyd–Warshall algorithm is an algorithm for finding
    shortest paths in a weighted graph with positive or
    negative edge weights (but with no negative cycles). O(n**3)"""

    # fill in the adjacency matrix:
    s = len(graph) + 1
    f = [[0 if i == j else float('inf') for i in range(s)] for j in range(s)]
    for i, vertex in enumerate(graph, 1):
        f[0][i] = f[i][0] = vertex
    for i, vertex in enumerate(graph, 1):
        for neighbor in graph[vertex]:
            f[i][f[0].index(neighbor)] = graph[vertex][neighbor]

    # algorithm:
    for k in range(1, s):
        for i in range(1, s):
            for j in range(1, s):
                f[i][j] = min(f[i][j], f[i][k] + f[k][j])
    return f


if __name__ == '__main__':
    g = {
        'a': {'b': 3},
        'b': {'a': 3, 'c': 2, 'd': 4, 'e': 7},
        'c': {'b': 2, 'e': 5},
        'd': {'b': 4, 'e': 1},
        'e': {'b': 7, 'c': 5, 'd': 1, 'f': 3},
        'f': {'e': 3}}
    pprint(floyd_warshall(g))
