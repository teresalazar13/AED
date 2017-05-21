class Graph2:
    def __init__(self, start):
        self.vertexes = {}
        self.start = start
        self.number_of_vertexes = 0

    def add_vertex(self, vertex):
        self.vertexes[vertex] = []
        self.number_of_vertexes += 1

    def add_weight(self, vertex, other_vertex, weight):
        self.vertexes[vertex].append([other_vertex, weight])
        self.vertexes[vertex].sort(key=lambda x: x[1])  # Sorts by weight

    # Used for reading form file. Check if vertex exist
    def add_vertex_and_weight(self, vertex, other_vertex, weight):
        if vertex not in self.vertexes:
            self.add_vertex(vertex)
        if other_vertex not in self.vertexes:
            self.add_vertex(other_vertex)
        self.add_weight(vertex, other_vertex, weight)

    def nearest_neighbour(self, path_set, vertex):
        for i in range(len(self.vertexes[vertex])):
            if self.vertexes[vertex][i][0] not in path_set:
                return self.vertexes[vertex][i][0], 0
        return self.start
