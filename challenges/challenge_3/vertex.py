class Vertex(object):
    def __init__(self, _id):
        self.id = _id
        # would like to learn how to make a adjacent list for neighbors
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=1):
        if vertex != self.neighbors:
            self.neighbors[vertex] = weight

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_id(self):
        return self.id

    def get_edge_weight(self, vertex):
        return self.neighbors[vertex]

# Attribution: better version of what I had in my challenge one,
# edited code with pair programming with Jake Shams
