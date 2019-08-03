class Vertex(object):

    def __init__(self, vertex):
        self.id = vertex
        self.neighbors = {}

    def __str__(self):
        return f'{self.id} adjacent to {[x.id for x in self.neighbors]}'

    def addNeighbor(self, vertex, weight=0):
        self.neighbors[vertex] = weight

    def getNeighbors(self):
        return self.neighbors.keys()

    def getId(self):
        return self.id

    def getEdgeWeight(self, vertex):
        return self.neighbors[vertex]

    def getEdges(self):
        return len(self.neighbors.keys())


class Graph:
    # creates a new, empty graph.
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def addVertex(self, vert):
        self.num_vertices += 1
        # create a new vertex
        new_vertex = Vertex(vert)
        # add the new vertex to the vertex dictionry
        self.vert_dict[vert] = new_vertex
        # return the new vertex
        return new_vertex

    def addEdgeWithWeight(self, fromVert, toVert, weight=0):
        """Adds a new, weighted, directed edge to the graph that connects two vertices."""
        if fromVert not in self.vert_dict or toVert not in self.vert_dict:
                # add it - or return an error (choice is up to you).
            raise ValueError("something went wrong...")
        else:
            self.vert_dict[fromVert].addNeighbor(
                self.vert_dict[toVert], weight)

    def getVertex(self, vertKey):
        """finds the vertex in the graph named vertKey."""
        if vertKey in self.vert_dict.keys():
            return vertKey
        else:
            raise ValueError("Vertex not found!")

    def getVertices(self):
        """returns the list of all vertices in the graph."""
        return self.vert_dict.keys()

    def getAllEdges(self):
        """Return number of all edges in the graph"""
        sum = 0
        for vert in self:
            sum += vert.getEdges()
        return sum


# Attribution:
# Pair Programming session and study session with:
# 1. Nathan
# 2. Jake
