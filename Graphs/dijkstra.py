from collections import deque


def dijkstra(graph, start, stop):
    """Dijkstra's algorithm is an algorithm for finding
    the shortest path between nodes in arbitrary-directed
    graphs with unbounded non-negative weights. O(V**2)"""
    queue = deque()
    label = dict()
    label[start] = 0
    queue.append(start)
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            distance = label[vertex] + graph[vertex][neighbor]
            if neighbor not in label or distance < label[neighbor]:
                label[neighbor] = distance
                queue.append(neighbor)

    path = [stop]
    r = revers_graph(graph)
    while start not in path:
        for neighbor in r[path[-1]]:
            if label[neighbor] == label[path[-1]] - r[path[-1]][neighbor]:
                path.append(neighbor)
                break
    return path[::-1], label[stop]


def revers_graph(graph):
    """Returns an inverse directed graph."""
    rev_graph = {vertex: {} for vertex in graph}
    for vertex in graph:
        for neighbour in graph[vertex]:
            rev_graph[neighbour].update({vertex: graph[vertex][neighbour]})
    return rev_graph


if __name__ == '__main__':
    g = {1: {2: 3, 4: 2},
         2: {3: 2, 5: 1},
         3: {6: 1},
         4: {5: 1, 7: 3},
         5: {6: 3, 8: 2},
         6: {9: 3},
         7: {8: 1},
         8: {9: 2},
         9: {}}
    print(*dijkstra(g, 1, 6))
