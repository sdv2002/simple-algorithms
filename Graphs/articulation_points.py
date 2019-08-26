from Graphs.dfs import connect_component_search


def get_articulation_points(graph):
    """Articulation points (or cut vertex) is any vertex
    whose removal increases the number of connected components.
    Algorithm runs in linear time, and is based on depth-first search."""
    result = []
    visited = set()
    parent = {}
    depth = {}
    low = {}
    deep = 0

    def dfs(vertex, d):
        visited.add(vertex)
        depth[vertex] = d
        low[vertex] = d
        child_count = 0
        is_articulation = False
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                parent[neighbor] = vertex
                dfs(neighbor, d + 1)
                child_count += 1
                if low[neighbor] >= depth[vertex]:
                    is_articulation = True
                low[vertex] = min(low[vertex], low[neighbor])
            elif neighbor != parent[vertex]:
                low[vertex] = min(low[vertex], depth[neighbor])
        if (parent[vertex] is not None and is_articulation) or (
                parent[vertex] is None and child_count > 1):
            result.append(vertex)

    for start_vertex in graph:
        parent[start_vertex] = None
        dfs(start_vertex, deep)
        break
    return result


def get_articulation_points_naive(graph):
    """The algorithm removes a vertex from the graph and
    checks if the number of connected components has changed. O(n**2)"""
    result = []
    cropped_graph = graph.copy()
    for vertex in graph:
        tmp = cropped_graph[vertex]

        # Delete vertex:
        for neighbor in cropped_graph[vertex]:
            cropped_graph[neighbor].remove(vertex)
        del cropped_graph[vertex]

        if connect_component_search(cropped_graph) > 1:
            result.append(vertex)

        # Insert the vertex back:
        cropped_graph[vertex] = tmp
        for neighbor in cropped_graph[vertex]:
            cropped_graph[neighbor].add(vertex)

    return result


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
          'l': {'j', 'k'}}
    print(get_articulation_points_naive(g1))
    print(get_articulation_points(g1))
