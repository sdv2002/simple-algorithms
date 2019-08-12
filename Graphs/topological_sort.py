def topological_sort(graph):
    """Linear topological ordering of a directed graph"""
    visited = set()
    ans = []
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex, graph, visited, ans)
    ans[:] = ans[::-1]
    return ans


def dfs(start, graph, visited, ans):
    visited.add(start)
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(neighbour, graph, visited, ans)
    ans.append(start)


if __name__ == '__main__':
    g = {1: {2, 3, 4}, 2: {5, 6}, 3: {6, 9}, 4: {7, 9}, 5: {8}, 6: {5, 7, 8},
         7: {8}, 8: set(), 9: set()}
    print(topological_sort(g))
