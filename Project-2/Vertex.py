class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def add_neighbour(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connectedTo:' + str([x.id for x in self.connectedTo])

    def get_connections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def get_weight(self,nbr):
        return self.connectedTo[nbr]
