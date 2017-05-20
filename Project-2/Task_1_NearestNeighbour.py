import operator as op
import random
from functools import reduce
import time


# TAREFA 1
# ALGORITHM - NEAREST NEIGHBOUR

# Example of a structure
def create_structure():
    graph = [[{'A', 'D'}, 1], [{'A', 'C'}, 2], [{'A', 'B'}, 3], [{'B', 'C'}, 4], [{'C', 'D'}, 5], [{'B', 'D'}, 6]]
    return graph


# Generates map, given the number of cities
def generate_map(number_of_cities):
    distances = get_distances(number_of_cities)
    cities = []
    # Creates cities
    for i in range(number_of_cities):
        # TODO->CHANGE
        # cities.append(chr(i + 65))
        cities.append(str(i))
    # Creates Graph and selects random city to start
    graph = []
    counter = 0
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            graph.append([{cities[i], cities[j]}, distances[counter]])
            counter += 1
    sorted_graph = list(graph)
    sorted_graph.sort(key=lambda x: x[1])
    return graph, sorted_graph


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
    graph = []
    for i in range(1, len(text) - 1):
        connection = text[i].split(",")
        graph.append([{connection[0], connection[1]}, int(connection[2])])
    graph.sort(key=lambda x: x[1])
    return graph


# Writes map into file
def write_map(graph, filename):
    f = open(filename, "w", encoding='utf-8')
    string = "start in A\n"
    for i in range(len(graph)):
        string += min(graph[i][0]) + "," + max(graph[i][0]) + "," + str(graph[i][1]) + "\n"
    f.write(string)
    f.close()


# Finds the nearest neighbour of a given vertex that is not in path
def nearest_neighbour(graph, path_set, vertex):
    for i in range(len(graph)):
        # If vertex is in connection between 2 vertexes AND the other vertex is not in path
        if vertex in graph[i][0] and (graph[i][0] - {vertex}).pop() not in path_set:
            vertex = (graph[i][0] - {vertex}).pop()
            return vertex


# Finds shortest path from start vertex, passing through all vertexes and ending in starting point
def find_shortest_path(graph, start, number_of_cities):
    path = [start]
    path_set = {start}
    current_vertex = start
    # While the path's length is smaller than the number of cities, find the nearest neighbour of a city
    while len(path) != number_of_cities:
        current_vertex = nearest_neighbour(graph, path_set, current_vertex)
        path.append(current_vertex)
        path_set.add(current_vertex)
    path.append(start)
    # print(path)


def number_maximum_of_cities_in_less_than_30_minutes():
    limit = 60 * 30  # 30 minutes
    number_of_cities = 2
    while True:
        unsorted_graph, graph = generate_map(number_of_cities)
        initial_time = time.time()
        find_shortest_path(graph, "1", number_of_cities)
        final_time = time.time()
        operation_time = final_time - initial_time
        if operation_time > limit:
            return
        else:
            print(number_of_cities, operation_time)
            number_of_cities += 100


# Main function
if __name__ == '__main__':
    # number_maximum_of_cities_in_less_than_30_minutes()
    # graph = create_structure()

    unsorted_graph, graph = generate_map(6000)
    initial_time = time.time()
    find_shortest_path(graph, "1", 6000)
    final_time = time.time()
    operation_time = final_time - initial_time
    print(6000, operation_time)

    # write_map(unsorted_graph, "Tarefa_2_1000.txt")
    # graph2 = read_map("Tarefa_2_1000.txt")
    # print(graph2)
    # start = "A"
    # find_shortest_path(graph, start, 1000)
