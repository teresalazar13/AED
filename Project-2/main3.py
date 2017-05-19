import random
from Graph2 import *

"""Do you just need an ordered sequence of items? Go for a list.
Do you just need to know whether or not you've already got a particular value, but without ordering (and you don't need
to store duplicates)? Use a set.
Do you need to associate values with keys, so you can look them up efficiently (by key) later on? Use a dictionary."""


# TAREFA 2
# ALGORITHM - NEAREST NEIGHBOUR


# Example of a structure
def create_structure():
    graph = Graph2("A")
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_weight("A", "B", 3)
    graph.add_weight("A", "C", 2)
    graph.add_weight("A", "D", 1)
    graph.add_weight("B", "A", 3)
    graph.add_weight("B", "C", 4)
    graph.add_weight("B", "D", 6)
    graph.add_weight("C", "A", 2)
    graph.add_weight("C", "B", 4)
    graph.add_weight("C", "D", 5)
    graph.add_weight("D", "A", 1)
    graph.add_weight("D", "B", 6)
    graph.add_weight("D", "C", 5)
    return graph


# Generates map, given the number of cities
def generate_map(number_of_cities):
    graph = Graph2("A")
    distances = get_distances(number_of_cities)
    counter = 0
    for i in range(number_of_cities):
        graph.add_vertex(chr(65 + i))
    for i in range(number_of_cities):
        for j in range(number_of_cities):
            if i != j:
                graph.add_weight(chr(65 + i), chr(65 + j), distances[counter])
                counter += 1
    return graph


# Creates array of distances
def get_distances(n):
    range_of_distances = n * n - n
    distances = []
    for i in range(5, range_of_distances + 10):
        distances.append(i*5)
    random.shuffle(distances)
    return distances


# Reads map from file
def read_map(filename):
    f = open(filename, "r", encoding='utf-8')
    text = f.read()
    text = text.split("\n")
    graph = Graph2(text[0])
    for i in range(1, len(text) - 1):
        connection = text[i].split(",")
        graph.add_vertex_and_weight(connection[0], connection[1], int(connection[2]))
    return graph


# Writes map into file
def write_map(filename, graph):
    f = open(filename, "w", encoding='utf-8')
    string = "start in A\n"
    for i in range(len(graph.vertexes)):
        vertex = graph.vertexes[chr(i + 65)]
        for j in range(len(vertex)):
            string += chr(i + 65) + "," + vertex[j][0] + "," + str(vertex[j][1]) + "\n"
    f.write(string)
    f.close()


def find_shortest_path(graph):
    path = [graph.start, graph.nearest_neighbour([graph.start], graph.start)]
    current_vertex = path[-1]
    while current_vertex != graph.start:
        path.append(graph.nearest_neighbour(path, current_vertex))
        current_vertex = path[-1]
    print(path)


# Main function
if __name__ == '__main__':
    # graph = create_structure()
    graph2 = generate_map(20)
    print(graph2.vertexes)
    write_map("Tarefa_2_20.txt", graph2)
    print(read_map("Tarefa_2_20.txt").vertexes)
    # find_shortest_path(graph2)
