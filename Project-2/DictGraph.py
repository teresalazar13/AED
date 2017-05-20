from Vertex import *
import math


class Graph:
    def __init__(self, start):
        self.vert_list = {}
        self.num_vertices = 0
        self.start = self.add_vertex(start)

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

    def print_file(self):
        string = self.start.id+"\n"
        # Connections
        vertices = list(self.vert_list.items())
        vertices.sort(key=lambda tup: tup[0])
        for k, v in vertices:
            connections = list(v.connected_to.items())
            connections.sort(key=lambda tup: tup[0].id)
            for kk, vv in connections:
                string += str(v.id) + "," + str(kk.id) + "," + str(vv) + "\n"
        return string

    def print(self):
        print("start in", self.start.id)
        string = "start in" + self.start.id + "\n"
        vertices = list(self.vert_list.items())
        vertices.sort(key=lambda tup: tup[0])
        for k, v in vertices:
            connections = list(v.connected_to.items())
            connections.sort(key=lambda tup: tup[0].id)
            for kk, vv in connections:
                string += str(v.id) + "," + str(kk.id) + "," + str(vv) + "\n"
        print(string)

    def medium_weight(self):
        total_weight = 0
        for vertex in self.vert_list.values():
            for weight in vertex.connected_to.values():
                total_weight += weight
        return total_weight/self.num_vertices/(self.num_vertices-1)

    def shortest_path(self):

        def do_it(vertex, unused, shortest_weight=math.inf, path=[],  previous_local_weight=0, local_path=[]):

            if local_path:
                current_local_weight = previous_local_weight + local_path[-1].get_weight(vertex)
            else:
                current_local_weight = 0

            # Branch and Bound condition (we wont find the shortest path if we proceed here)
            if current_local_weight >= shortest_weight:
                return shortest_weight, path

            local_path.append(vertex)
            if len(local_path) == self.num_vertices:
                current_local_weight += local_path[-1].get_weight(self.start)
                if current_local_weight < shortest_weight:
                    path = list(local_path)
                    path.append(self.start)
                    local_path.pop()
                    return current_local_weight, path
            unused.discard(vertex)

            for v in unused:
                shortest_weight, path = do_it(v, unused, shortest_weight, path, current_local_weight, local_path)

            local_path.pop()
            unused.add(vertex)
            return shortest_weight, path

        medium_path_weight = self.medium_weight() * self.num_vertices
        return do_it(self.start, set(list(self.vert_list.values())), medium_path_weight + 1)
