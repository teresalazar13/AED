import random


# Example of a Structure
def create_structure():
    graph = [[1, 2, 3],
             [4, 6, 7],
             [7, 9, 8]]
    print(graph)


# Finds shortest path from start vertex, passing through all vertexes and ending in starting point
def find_shortest_path(graph):
    def get_minimun_distance_and_parent(target_city, combinations):
        if combinations:
            dists = []
            parent_cities = []
            for parent_city in combinations:
                dists.append(graph[parent_city][target_city] +
                             get_minimun_distance_and_parent(parent_city, combinations - set([parent_city]))[0])
                parent_cities.append(parent_city)
            minimum_distance = min(dists)
            return minimum_distance, parent_cities[dists.index(minimum_distance)]
        else:
            return graph[0][target_city], 0

    best_path = []
    distances = []
    target_city = 0
    combinations = set(range(1, len(graph)))

    while True:
        distance, parent_city = get_minimun_distance_and_parent(target_city, combinations)
        if parent_city == 0:
            return best_path[::-1], distances[0]
        best_path.append(parent_city)
        distances.append(distance)
        target_city = parent_city
        combinations = combinations - set([parent_city])


# Creates Map
def create_map(number_of_cities):
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
def read_map(filename, number_of_cities):
    f = open(filename, "r", encoding='utf-8')
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
        graph[ord(connection[1]) - 65][ord(connection[0]) - 65] = int(connection[2])
    return graph


# Writes map into file
def write_map(filename, graph):
    f = open(filename, "w", encoding='utf-8')
    string = "start in A\n"
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i != j:
                string += chr(j + 65) + "," + chr(i + 65) + "," + str(graph[i][j]) + "\n"
    f.write(string)
    f.close()


# Main function
if __name__ == '__main__':
    graph = create_map(10)
    write_map("Tarefa_2_10.txt", graph)
    graph2 = read_map("Tarefa_2_10.txt", 10)
    print(graph2)
    print(find_shortest_path(graph))


