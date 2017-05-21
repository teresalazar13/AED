import random
from Graph2 import *
import time
import os.path
import main


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


def print_map(graph):
    for k, v in graph.vertexes.items():
        print(k, v)


# Generates map, given the number of cities
def generate_map(number_of_cities):
    graph = Graph2("C0")
    distances = get_distances(number_of_cities)
    counter = 0
    for i in range(number_of_cities):
        graph.add_vertex("C" + str(i))
    for i in range(number_of_cities):
        for j in range(number_of_cities):
            if i != j:
                graph.add_weight("C" + str(i), "C" + str(j), distances[counter])
                counter += 1
    filename = "Tarefa_2_" + str(number_of_cities) + ".txt"
    write_map(filename, graph)
    return graph, graph


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
    graph = Graph2("C0")
    for i in range(1, len(text) - 1):
        connection = text[i].split(",")
        graph.add_vertex_and_weight(connection[0], connection[1], int(connection[2]))
    f.close()
    return graph


# Writes map into file
def write_map(filename, graph):
    f = open(filename, "w", encoding='utf-8')
    string = "start in " + graph.start + "\n"
    for i in range(len(graph.vertexes)):
        vertex = graph.vertexes["C" + str(i)]
        for j in range(len(vertex)):
            string += "C" + str(i) + "," + vertex[j][0] + "," + str(vertex[j][1]) + "\n"
    f.write(string)
    f.close()


def find_shortest_path(graph):
    initial_time = time.time()
    distance = 0
    path = [graph.start]
    path_set = {graph.start}
    current_vertex = graph.start
    while len(path) != graph.number_of_vertexes:
        current_vertex, d = graph.nearest_neighbour(path_set, current_vertex)
        path.append(current_vertex)
        path_set.add(current_vertex)
        distance += d
    path.append(graph.start)
    final_time = time.time()
    operation_time = final_time - initial_time
    print("Number of cities: ", graph.number_of_vertexes)
    print("Path: ", path)
    print("Total Distance", distance)
    print("Operation time: ", operation_time)
    return path, distance, operation_time


def maximum_number_of_cities_in_less_than_30_minutes():
    limit = 60 * 30  # 30 minutes
    number_of_cities = 1702
    while True:
        filename = "Tarefa_2_" + str(number_of_cities) + ".txt"
        if os.path.exists(filename):
            print("Map exists. Starting calculations")
            graph = read_map(filename)
        else:
            print("Map doesn't exist. Creating map for ", number_of_cities)
            main.generate_map_2(number_of_cities)
            graph = read_map(filename)
            print("Map created. Starting calculations")

        path, distance, operation_time = find_shortest_path(graph)
        if operation_time > limit:
            return
        else:
            number_of_cities += 100
