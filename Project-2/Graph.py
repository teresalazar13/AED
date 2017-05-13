from Vertex import *


class Graph:
    def __init__(self, start):
        self.vert_list = {}
        self.num_vertices = 0
        self.start = start

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vert_list

    def add_edge(self, f, t, cost=0):
        if f not in self.vert_list:
            nv = self.add_vertex(f)
        if t not in self.vert_list:
            nv = self.add_vertex(t)
        self.vert_list[f].add_neighbour(self.vert_list[t], cost)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())

    def print(self):
        print("start in", self.start)
        string = ""
        for k, v in self.vert_list.items():
            for kk, vv in v.connected_to.items():
                string += str(v.id) + " -> " + str(kk.id) + " " + str(vv) + "\n"
        print(string)
