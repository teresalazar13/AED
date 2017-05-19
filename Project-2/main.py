from Graph import *
import operator as op
from functools import reduce
import random


# TAREFA 2
# ALGORITHM - BRUTE FORCE


# Example of a Structure
def create_structure():
    graph = Graph("A")
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_edge("A", "B", 20)
    graph.add_edge("B", "A", 20)
    graph.add_edge("A", "C", 42)
    graph.add_edge("C", "A", 42)
    graph.add_edge("A", "D", 35)
    graph.add_edge("D", "A", 35)
    graph.add_edge("B", "C", 34)
    graph.add_edge("C", "B", 34)
    graph.add_edge("B", "D", 30)
    graph.add_edge("D", "B", 30)
    graph.add_edge("C", "D", 12)
    graph.add_edge("D", "B", 12)
    graph.print()


# Generates a map with a certain number of cities
def map_generator(number_of_cities):
    distances = get_distances(number_of_cities)
    cities = []
    # Creates cities
    for i in range(number_of_cities):
        cities.append(chr(i + 65))
    # Creates Graph and selects random city to start
    graph = Graph(cities[random.randint(0, number_of_cities-1)])
    counter = 0
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            graph.add_edge(cities[i], cities[j], distances[counter])
            graph.add_edge(cities[j], cities[i], distances[counter])
            counter += 1
    return graph


# Creates array of distances
def get_distances(n):
    range_of_distances = combinations(n, 2)
    distances = []
    for i in range(5, range_of_distances + 10):
        distances.append(i*5)
    random.shuffle(distances)
    return distances


# Returns number of distances needed according to number of cities
def combinations(n, r):
    r = min(r, n-r)
    if r == 0:
        return 1
    numerator = reduce(op.mul, range(n, n-r, -1))
    denominator = reduce(op.mul, range(1, r+1))
    return numerator // denominator


# Reads map from file
def read_map(filename):
    f = open(filename, "r", encoding='utf-8')
    text = f.read()
    text = text.split("\n")
    graph = Graph(text[0])
    for i in range(1, len(text) - 1):
        connection = text[i].split(",")
        graph.add_edge(connection[0], connection[1], connection[2])
        graph.add_edge(connection[1], connection[0], connection[2])
    return graph


# Writes map into file
def write_map(filename, graph):
    f = open(filename, "w", encoding='utf-8')
    f.writelines(graph.print_file())
    f.close()


# Prints each possible path and its distance
def prints_paths_and_distances(graph):
    for k, v in graph.vert_list.items():
        if k != graph.start:
            paths = graph.find_all_paths(graph.num_vertices, graph.start, k)
            for path in paths:
                path.append(graph.start)
                print(path, graph.path_length(path))


# Main function
if __name__ == '__main__':
    # create_structure()
    # graph = read_map("Tarefa_1_4.txt")
    # write_map("Tarefa_1_5.txt", graph)
    graph = map_generator(10)
    # graph.print()
    prints_paths_and_distances(graph)
