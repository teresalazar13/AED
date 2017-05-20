# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
#
import unittest


# this implementation of binary heap takes key value pairs,
# we will assume that the keys are all comparable

class PriorityQueue:
    def __init__(self):
        self.heapArray = [(0, 0)]
        self.currentSize = 0

    def buildHeap(self, alist):
        self.currentSize = len(alist)
        self.heapArray = [(0, 0)]
        for i in alist:
            self.heapArray.append(i)
        i = len(alist) // 2
        while (i > 0):
            self.percDown(i)
            i = i - 1

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapArray[i][0] > self.heapArray[mc][0]:
                tmp = self.heapArray[i]
                self.heapArray[i] = self.heapArray[mc]
                self.heapArray[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 > self.currentSize:
            return -1
        else:
            if i * 2 + 1 > self.currentSize:
                return i * 2
            else:
                if self.heapArray[i * 2][0] < self.heapArray[i * 2 + 1][0]:
                    return i * 2
                else:
                    return i * 2 + 1

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapArray[i][0] < self.heapArray[i // 2][0]:
                tmp = self.heapArray[i // 2]
                self.heapArray[i // 2] = self.heapArray[i]
                self.heapArray[i] = tmp
            i = i // 2

    def add(self, k):
        self.heapArray.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def delMin(self):
        retval = self.heapArray[1][1]
        self.heapArray[1] = self.heapArray[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapArray.pop()
        self.percDown(1)
        return retval

    def isEmpty(self):
        if self.currentSize == 0:
            return True
        else:
            return False

    def decreaseKey(self, val, amt):
        done = False
        i = 1
        myKey = 0
        while not done and i <= self.currentSize:
            if self.heapArray[i][1] == val:
                done = True
                myKey = i
            else:
                i = i + 1
        if myKey > 0:
            self.heapArray[myKey] = (amt, self.heapArray[myKey][1])
            self.percUp(myKey)

    def __contains__(self, vtx):
        for pair in self.heapArray:
            if pair[1] == vtx:
                return True
        return False

"""
    # GRAPH
    def calculate_less_distance(self, number_of_cities):
        array_of_paths = []

        while len(array_of_paths) < math.factorial(number_of_cities - 1):
            array_of_cities = [self.start]
            array_of_distances = []

            while len(array_of_cities) < number_of_cities:
                for k, v in self.vert_list.items():
                    for kk, vv in v.connected_to.items():
                        if str(v.id) == array_of_cities[-1] and str(kk.id) not in array_of_cities:
                            array_of_cities.append(kk.id)
                            array_of_distances.append(vv)
                        elif str(kk.id) == array_of_cities[-1] and str(v.id) not in array_of_cities:
                            array_of_cities.append(v.id)
                            array_of_distances.append(vv)

            last_city = self.get_vertex(array_of_cities[-1])
            start_city = self.get_vertex(self.start)
            array_of_distances.append(last_city.get_weight(start_city) or start_city.get_weight(last_city))
            array_of_cities.append(self.start)

            if array_of_cities not in array_of_paths:
                array_of_paths.append(array_of_cities)
                array_of_distances.append(array_of_distances)
            else:
                print("Already here", array_of_cities)
                break
        print(array_of_paths)

    # MAIN
    # graph.calculate_less_distance(3)
    # dijkstra(graph, graph.get_vertex(graph.start))
    def dijkstra(aGraph, start):
        pq = PriorityQueue()
        start.set_distance(0)
        pq.buildHeap([(v.get_distance(), v) for v in aGraph])
        while not pq.isEmpty():
            current_vert = pq.delMin()
            for next_vert in current_vert.get_connections():
                new_dist = current_vert.get_distance() + current_vert.get_weight(next_vert)
                if new_dist < next_vert.get_distance():
                    next_vert.set_distance(new_dist)
                    next_vert.set_pred(current_vert)
                    pq.decreaseKey(next_vert, new_dist)
        print(new_dist)

    # VERTEX
    self.dist = 0
    self.pred = None

    def set_distance(self, d):
        self.dist = d

    def get_distance(self):
        return self.dist

    def set_pred(self, p):
        self.pred = p


    MAIN2
    time1 = time.time()
    print(find_shortest_path(graph))
    time2 = time.time()
    print(time2 - time1)
    time3 = time.time()
    print(tsp_rec_solve(graph))
    time4 = time.time()
    print(time4 - time3)
    # Difference of time execution between the two approaches
    print((time4 - time3) - (time2 - time1))

    def tsp_rec_solve(d):
        def rec_tsp_solve(c, ts):
            assert c not in ts
            if ts:
                return min((d[lc][c] + rec_tsp_solve(lc, ts - set([lc]))[0], lc)
                           for lc in ts)
            else:
                return (d[0][c], 0)
        best_tour = []
        c = 0
        cs = set(range(1, len(d)))
        while True:
            l, lc = rec_tsp_solve(c, cs)
            if lc == 0:
                break
            best_tour.append(lc)
            c = lc
            cs = cs - set([lc])
        best_tour = tuple(reversed(best_tour))
        return best_tour


    """
