from Graph import *
import random


def create_structure():
    graph = Graph("A")
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_edge("A", "B", 20)
    graph.add_edge("A", "C", 42)
    graph.add_edge("A", "D", 35)
    graph.add_edge("B", "C", 34)
    graph.add_edge("B", "D", 30)
    graph.add_edge("C", "D", 12)
    graph.print()


def read_map(filename):
    f = open(filename, "r", encoding='utf-8')
    text = f.read()
    text = text.split("\n")
    graph = Graph(text[0])
    for i in range(1, len(text) - 1):
        connection = text[i].split(",")
        graph.add_edge(connection[0], connection[1], connection[2])
    return graph


# TODO -> different distances
def map_generator(number_of_cities):
    cities = []
    for i in range(number_of_cities):
        cities.append(chr(i + 65))
    graph = Graph(cities[random.randint(0, number_of_cities-1)])
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            graph.add_edge(cities[i], cities[j], random.randint(10, 100))
    return graph


def write_map(filename, graph):
    f = open(filename, "w", encoding='utf-8')
    f.writelines(graph.print_file())
    f.close()


if __name__ == '__main__':
    # create_structure()
    # read_map("Tarefa_1_4.txt").print()
    graph = map_generator(5)
    write_map("Tarefa_1_5.txt", graph)
