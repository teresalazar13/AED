from Vertex import *
from Graph import *


def create_structure():
    graph = Graph()
    graph.add_vertex("V1")
    graph.add_vertex("V2")
    graph.add_vertex("V3")
    graph.add_edge("V1", "V3", 5)
    graph.add_edge("V1", "V2", 3)
    graph.print()

if __name__ == '__main__':
    create_structure()
