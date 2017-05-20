from DictGraph import *
import random
import time


# TAREFA 2
# ALGORITHM - BRANCH & BOUND

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

"""
    Generates a map with a certain number of cities
"""
def map_generator(number_of_cities):
    if(number_of_cities < 1):
        return 

    distances = get_distances(number_of_cities)

    cities = []
    
    # Creates cities
    for i in range(number_of_cities):
        cities.append("C"+str(i))
    
    # Creates Graph 
    graph = Graph(cities[0])
    counter = 0
    
    for i in range(len(cities)):
        for j in range(len(cities)):
            if(i != j):
                graph.add_edge(cities[i], cities[j], distances[counter])
                counter += 1
    
    return graph


"""
    Writes map into file
    A   -> All cities
    A,B,10   -> Weight from one city to another 
    A,C,15      |
    B,A,13      V
    ...
"""
def write_map(filename, graph):
    f = open(filename, "w", encoding='utf-8')
    f.writelines(graph.print_file())
    f.close()


"""
    Reads map from file
"""
def read_map(filename):
    f = open(filename, "r", encoding='utf-8')
    text = f.read()
    text = text.split("\n")

    graph = Graph(text[0])

    for i in range(1, len(text) - 1):
        connection = text[i].split(",")
        graph.add_edge(connection[0], connection[1], int(connection[2]))
    
    return graph

# Creates array of distances
def get_distances(n):
    range_of_distances = n*(n-1)
    distances = []
    for i in range(5, range_of_distances + 10):
        distances.append(i*5)
    random.shuffle(distances)
    return distances


# Main function
if __name__ == '__main__':
    n=18

    start = time.time()
    graph = map_generator(n)
    stop = time.time()
    print("generate time",stop-start)

    start = time.time()
    write_map("Tarefa_2_"+str(n)+".txt",graph)
    stop = time.time()
    print("write time",stop-start)

    start = time.time()
    graph = read_map("Tarefa_2_"+str(n)+".txt")
    stop = time.time()
    print("read time",stop-start)

    start = time.time()
    weight, path = graph.shortestPath()
    stop = time.time()
    print("find shortest path time",stop-start)
    path_ids = [v.id for v in path]
    print(weight,path_ids)
    



    