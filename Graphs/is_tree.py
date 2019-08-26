from Graphs.dfs import connect_component_search
from Graphs.number_of_edges import number_of_edges


def is_tree(graph):
    """Is the graph a tree."""
    ccs = connect_component_search(graph)
    edges = number_of_edges(graph)
    if ccs == 1 and edges == len(graph) - 1:
        return True
    return False


if __name__ == '__main__':
    g1 = {'a': {'b', 'c'},
          'b': {'a', 'd', 'e'},
          'c': {'a', 'f', 'g'},
          'd': {'b'},
          'e': {'b', 'h'},
          'f': {'c', 'i'},
          'g': {'c'},
          'h': {'e'},
          'i': {'f', 'j'},
          'j': {'k', 'l', 'i'},
          'k': {'j'},
          'l': {'j'}}
    print(is_tree(g1))
