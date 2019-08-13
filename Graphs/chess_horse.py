"""Restoration of the trajectory of a chess horse using the BFS algorithm"""
from pprint import pprint
from Graphs.bfs import bfs


if __name__ == '__main__':
    letters = 'abcdefgh'
    numbers = '12345678'
    vertexes = [x + y for x in letters for y in numbers]
    graph = {vertex: set() for vertex in vertexes}
    for vertex in vertexes:
        n1 = chr(ord(vertex[0]) + 2) + str(int(vertex[1]) + 1)
        n2 = chr(ord(vertex[0]) + 2) + str(int(vertex[1]) - 1)
        n3 = chr(ord(vertex[0]) - 2) + str(int(vertex[1]) - 1)
        n4 = chr(ord(vertex[0]) - 2) + str(int(vertex[1]) + 1)
        n5 = chr(ord(vertex[0]) + 1) + str(int(vertex[1]) + 2)
        n6 = chr(ord(vertex[0]) + 1) + str(int(vertex[1]) - 2)
        n7 = chr(ord(vertex[0]) - 1) + str(int(vertex[1]) - 2)
        n8 = chr(ord(vertex[0]) - 1) + str(int(vertex[1]) + 2)
        moving_options = {n1, n2, n3, n4, n5, n6, n7, n8}
        graph[vertex] = moving_options.intersection(vertexes)
    pprint(bfs(graph, 'a1', 'g7')[2])
