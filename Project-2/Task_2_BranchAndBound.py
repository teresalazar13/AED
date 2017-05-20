from DictGraph import *
import random
import time


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
    return graph


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
    graph = Graph(text[0])
    for i in range(1, len(text) - 1):
        connection = text[i].split(",")
        graph.add_edge(connection[0], connection[1], int(connection[2]))
    return graph


def find_shortest_path(graph):
    weight, path = graph.shortest_path()
    return path


def maximum_number_of_cities_in_less_than_30_minutes():
    limit = 60 * 30  # 30 minutes
    number_of_cities = 2
    while True:
        graph = generate_map(number_of_cities)
        initial_time = time.time()
        find_shortest_path(graph)
        final_time = time.time()
        operation_time = final_time - initial_time
        if operation_time > limit:
            return
        else:
            print(number_of_cities, operation_time)
            number_of_cities += 1
