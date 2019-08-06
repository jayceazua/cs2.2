from vertex import Vertex


class Graph:
    def __init__(self):
        self.vert_list = {}
        # Graph property Order means the number of vertices
        self.order = 0
        # number of edges
        self.size = 0
        self.DEFAULT_WEIGHT = 1

    def __iter__(self):
        """
        Iterate over the vertex objects in the graph,
        to use sytax; v in g
        """
        return iter(self.vert_list.values())

    # add vertex
    def add_vertex(self, key):
        self.order += 1
        self.vert_list[key] = Vertex(key)
        return self.vert_list[key]

    # get vertex
    def get_vertex(self, key):
        return self.vert_list[key]

    # add edge
    def add_edge(self, v, u, weight=None):
        self.size += 1

        if weight == None:
            weight = self.DEFAULT_WEIGHT

        if v not in self.vert_list:
            self.add_vertex(v)

        if u not in self.vert_list:
            self.add_vertex(u)

        self.vert_list[v].add_neighbor(self.vert_list[u], weight)

    # get vertices
    def get_vertices(self):
        return list(self.vert_list.keys())

    # get order
    def get_order(self):
        return self.order

    # get edges
    def get_edges(self):
        edges = []
        for v in self.vert_list.values():
            for u in v.neighbors:
                edges.append((v.id, u.id))
        return edges

    # get edges with weight
    def get_edges_weighted(self):
        edges = []
        for v in self.vert_list.values():
            for u in v.neighbors:
                edges.append((v.id, u.id, v.neighbors[u]))
        return edges

    # get size
    def get_size(self):
        neighbor_counts = map(lambda v: len(v.neighbors),
                              self.vert_list.values())
        return sum(neighbor_counts)

    # Breadth-First Search
    # Depth-First Search


# Attribution: Meredith challenge 1 solution used the iter method
