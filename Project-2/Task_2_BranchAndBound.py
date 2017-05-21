from DictGraph import *
import random
import time
import os.path
import main


# TAREFA 2
# ALGORITHM - BRANCH AND BOUND


# Example of a Structure
def create_structure():
    graph = Graph("A")
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_edge("A", "B", 20)
    graph.add_edge("A", "C", 20)
    graph.add_edge("B", "A", 34)
    graph.add_edge("B", "C", 30)
    graph.add_edge("C", "A", 30)
    graph.add_edge("C", "B", 12)
    graph.print()


def print_map(graph):
    vertices = list(graph.vert_list.items())
    vertices.sort(key=lambda tup: tup[0])
    for k, v in vertices:
        connections = list(v.connected_to.items())
        connections.sort(key=lambda tup: tup[0].id)
        string = str(v.id) + " {"
        for kk, vv in connections:
            string += "(" + str(kk.id) + "," + str(vv) + ")"
        string += "}"
        print(string)


# Generates a map with a certain number of cities
def generate_map(number_of_cities):
    if number_of_cities < 1:
        return
    distances = get_distances(number_of_cities)
    cities = []
    # Creates cities
    for i in range(number_of_cities):
        cities.append("C" + str(i))
    # Creates Graph 
    graph = Graph(cities[0])
    counter = 0
    for i in range(len(cities)):
        for j in range(len(cities)):
            if i != j:
                graph.add_edge(cities[i], cities[j], distances[counter])
                counter += 1
    filename = "Tarefa_2_" + str(number_of_cities) + ".txt"
    write_map(graph, filename)
    return graph, graph


# Creates array of distances
def get_distances(n):
    range_of_distances = n * (n-1)
    distances = []
    for i in range(5, range_of_distances + 10):
        distances.append(i*5)
    random.shuffle(distances)
    return distances


# Writes map into file
def write_map(graph, filename):
    f = open(filename, "w", encoding='utf-8')
    f.writelines(graph.print_file())
    f.close()


# Reads map from file
def read_map(filename):
    f = open(filename, "r", encoding='utf-8')
    text = f.read()
    text = text.split("\n")
    graph = Graph("C0")
    for i in range(1, len(text) - 1):
        connection = text[i].split(",")
        graph.add_edge(connection[0], connection[1], int(connection[2]))
    f.close()
    return graph


def find_shortest_path(graph):
    initial_time = time.time()
    distance, path = graph.shortest_path()
    final_time = time.time()
    operation_time = final_time - initial_time
    print("Path: ", path)
    print("Total Distance", )
    print("Operation time: ", operation_time)
    return path, distance, operation_time


def maximum_number_of_cities_in_less_than_30_minutes():
    limit = 60 * 30  # 30 minutes
    number_of_cities = 2
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
            print("Number of cities: ", number_of_cities)
            number_of_cities += 1
