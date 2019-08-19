from collections import deque


def dijkstra(graph, start, stop):
    """Dijkstra's algorithm is an algorithm for finding
    the shortest paths between nodes in arbitrary directed
    graphs with unbounded non-negative weights. O(V**2)"""
    queue = deque()
    path = [stop]
    short = dict()
    short[start] = 0
    queue.append(start)
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in short or \
                    short[neighbor] > short[vertex] + graph[vertex][neighbor]:

                short[neighbor] = short[vertex] + graph[vertex][neighbor]
                queue.append(neighbor)

    while start not in path:
        for neighbor in graph[path[-1]]:
            if short[neighbor] == short[path[-1]] - graph[path[-1]][neighbor]:
                path.append(neighbor)
                break
    return path[::-1]


if __name__ == '__main__':
    g = {
        'a': {'b': 3},
        'b': {'a': 3, 'c': 2, 'd': 4, 'e': 7},
        'c': {'b': 2, 'e': 5},
        'd': {'b': 4, 'e': 1},
        'e': {'b': 7, 'c': 5, 'd': 1, 'f': 3},
        'f': {'e': 3}}
    print(dijkstra(g, 'b', 'e'))

