import random
import time


# TAREFA 2
# ALGORITHM - KELP HART (DYNAMIC PROGRAMMING)

# Example of a Structure
def create_structure():
    graph = [[0, 2, 3],
             [4, 0, 7],
             [7, 9, 0]]
    print(graph)


# Creates Map
def generate_map(number_of_cities):
    distances = get_distances(number_of_cities)
    graph = []
    counter = 0
    for i in range(number_of_cities):
        row = []
        for j in range(number_of_cities):
            if i != j:
                row.append(distances[counter])
                counter += 1
            else:
                row.append(0)
        graph.append(row)
    filename = "Tarefa_2_" + str(number_of_cities) + ".txt"
    write_map(filename, graph)
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
    number_of_cities = ""
    for i in range(9, len(filename) - 4):
        number_of_cities += filename[i]
    number_of_cities = int(number_of_cities)
    text = f.read()
    text = text.split("\n")
    graph = []
    for i in range(number_of_cities):
        row = []
        for j in range(number_of_cities):
            row.append(0)
        graph.append(row)
    for i in range(1, len(text) - 1):
        connection = text[i].split(",")
        graph[int(connection[1][1:])][int(connection[0][1:])] = int(connection[2])
    return graph


# Writes map into file
def write_map(filename, graph):
    f = open(filename, "w", encoding='utf-8')
    string = "start in C0\n"
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i != j:
                string += "C" + str(i) + ",C" + str(j) + "," + str(graph[i][j]) + "\n"
    f.write(string)
    f.close()


# Finds shortest path from start vertex, passing through all vertexes and ending in starting point
def find_shortest_path(graph):
    def get_minimum_distance_and_parent(target_city, combinations):
        if combinations:
            dists = []
            parent_cities = []
            for parent_city in combinations:
                dists.append(graph[parent_city][target_city] +
                             get_minimum_distance_and_parent(parent_city, combinations - set([parent_city]))[0])
                parent_cities.append(parent_city)
            minimum_distance = min(dists)
            return minimum_distance, parent_cities[dists.index(minimum_distance)]
        else:
            return graph[0][target_city], 0

    best_path = ["C0"]
    distances = []
    target_city = 0
    combinations = set(range(1, len(graph)))

    while True:
        distance, parent_city = get_minimum_distance_and_parent(target_city, combinations)
        if parent_city == 0:
            best_path.append("C" + str(parent_city))
            return best_path[::-1], distances[0]
        best_path.append("C" + str(parent_city))
        distances.append(distance)
        target_city = parent_city
        combinations = combinations - set([parent_city])


def maximum_number_of_cities_in_less_than_30_minutes():
    limit = 60 * 30  # 30 minutes
    number_of_cities = 2
    while True:
        unsorted_graph, graph = generate_map(number_of_cities)
        initial_time = time.time()
        print(graph)
        find_shortest_path(graph)
        final_time = time.time()
        operation_time = final_time - initial_time
        if operation_time > limit:
            return
        else:
            print(number_of_cities, operation_time)
            number_of_cities += 1
