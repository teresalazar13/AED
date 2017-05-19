import operator as op
import random
from functools import reduce


# TAREFA 1
# ALGORITHM - NEAREST NEIGHBOUR

# Example of a structure
def create_structure():
    graph = [[{'A', 'B'}, 3], [{'A', 'C'}, 2], [{'A', 'D'}, 1],
             [{'B', 'C'}, 4], [{'B', 'D'}, 6],
             [{'C', 'D'}, 5]]
    graph.sort(key=lambda x: x[1])
    return graph


# Generates map, given the number of cities
def generate_map(number_of_cities):
    distances = get_distances(number_of_cities)
    cities = []
    # Creates cities
    for i in range(number_of_cities):
        cities.append(chr(i + 65))
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


# Finds the nearest neighbour of a given vertex that is not in path
def nearest_neighbour(graph, path_set, vertex):
    for i in range(len(graph)):
        # If vertex is in connection between 2 vertexes AND the other vertex is not in path
        if vertex in graph[i][0] and (graph[i][0] - {vertex}).pop() not in path_set:
            vertex = (graph[i][0] - {vertex}).pop()
            # Removes the connection from graph because we no longer need it
            # We can only go through an edge once
            graph.remove(graph[i])
            return vertex


# Finds shortest path from start vertex, passing through all vertexes and ending in starting point
def find_shortest_path(graph, start, number_of_cities):
    vertex_to_append = nearest_neighbour(graph, [start], start)
    path = [start, vertex_to_append]
    path_set = {start, vertex_to_append}
    vertex = path[-1]
    while len(path) != number_of_cities:
        vertex_to_append = nearest_neighbour(graph, path_set, vertex)
        path.append(vertex_to_append)
        path_set.add(vertex_to_append)
        vertex = path[-1]
    path.append(start)
    print(path)


if __name__ == '__main__':
    # graph = create_structure()
    unsorted_graph, graph = generate_map(10)
    write_map(unsorted_graph, "Tarefa_2_10.txt")
    graph2 = read_map("Tarefa_2_10.txt")
    print(graph2)
    start = "A"
    find_shortest_path(graph, start, 10)
