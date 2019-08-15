def kosaraju(graph):
    """Kosaraju's algorithm is a linear time algorithm to find
    the strongly connected components of a directed graph. O(V+E)"""
    used = set()
    stack = []
    for vertex in graph:
        if vertex not in used:
            dfs_pass_one(vertex, graph, used, stack)
    reversed_graph = revers_graph(graph)
    used = set()
    scc = []
    while stack:
        vertex = stack.pop()
        if vertex not in used:
            scc.append(dfs_pass_two(vertex, reversed_graph, used))
    return scc


def dfs_pass_one(vertex, graph, used, stack):
    """Using the DFS algorithm, fill the stack with
    vertices for the second pass."""
    used.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs_pass_one(neighbour, graph, used, stack)
    stack.append(vertex)


def revers_graph(graph):
    """Returns an inverse directed graph."""
    rev_graph = {vertex: set() for vertex in graph}
    for vertex in graph:
        for neighbour in graph[vertex]:
            rev_graph[neighbour].add(vertex)
    return rev_graph


def dfs_pass_two(vertex, reversed_graph, used, scc=None):
    """Filling the list strongly connected components."""
    scc = scc or set()
    used.add(vertex)
    scc.add(vertex)
    for neighbor in reversed_graph[vertex]:
        if neighbor not in used:
            dfs_pass_two(neighbor, reversed_graph, used, scc)
    return scc


if __name__ == '__main__':
    directed_graph = dict(a={'b'}, b={'c', 'd'}, c={'a'}, d={'e'}, e={'f'},
                          f={'d'}, g={'h', 'f'}, h={'i'}, i={'j'},
                          j={'g'}, k={'j'})
    print(kosaraju(directed_graph))
