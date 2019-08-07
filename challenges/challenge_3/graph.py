from vertex import Vertex
# used for BFS will switch to a priority queue later
from collections import deque


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

    # get size - Meredith: might not need this above I got the size of the Graph by simply adding a property
    def get_size(self):
        neighbor_counts = map(lambda v: len(v.neighbors),
                              self.vert_list.values())
        return sum(neighbor_counts)

# Challenge 2
    # Breadth-First Search
    def breadth_first_search(self, vertex):
        # Start with an arbitrary vertex
            # mark as visited and add to queue
        visited = {vertex}
        queue = deque([vertex])
        # For each vertex v in queue
        while len(queue) != 0:
            # Remove v from the queue
            vertex_key = queue.popleft()
            # For each vertex u adjacent to v
            for u in self.get_vertex(vertex_key).neighbors:
                # If u has not been visited
                if u not in visited:
                    # Set parent of u to v
                    # Mark u as visited
                    visited.add(u)
                    # Add u to the queue
                    queue.append(u)
        return list(visited)

    # shortest_path
    def shortest_path(self, from_v, to_u):
        # Start with an arbitrary vertex v, mark v visited, add v to queue
        visited = {from_v: [from_v]}
        queue = deque(from_v)
        # print("wtf is this: ", self.get_vertex(from_v))
        # For each vertex v in queue
        while len(queue) != 0:
            # Remove v from queue
            vertex_key = queue.popleft()
            # For each vertex u adjacent to v
            for u in self.get_vertex(vertex_key).neighbors:
                # If u has not been visited
                if u not in visited:
                    # Set parent of u to v, mark u visited, add u to queue
                    visited[u] = visited[vertex_key] + [u]
                    if u == to_u:
                        return visited[u]
                    queue.append(u)
        return None
    
# Challenge 3
    # Depth-First Search
    # DFS(G, v)
    def r_depth_first_search(self, from_v, to_u, visited=None):
        """ Depth-frist search recursively """
    # label v as visited
        if visited == None:
            visited = {from_v}
        # for each edge from v to w:
        for u in self.get_vertex(from_v).neighbors:
        #     if vertex w is not visited
            if u == to_u:
                return True
            else:
                #     recursively call DFS(G,w)
                visited.add(u)
                return self.r_depth_first_search(u, to_u, visited)
    
    def i_depth_first_search(self, from_v, to_u):
        """ Depth-first search iteratively """
        # Start with a vertex v
        visited = {from_v}
        # Let S be a stack
        stack = deque()
        # S.push(v)
        stack.appendleft(from_v)
        # while S is not empty:
        while len(stack) != 0:
            # v = S.pop()
            vertex = stack.popleft()
            # Print v
            print(vertex)
            # if v is not labeled as discovered:
            if vertex in visited:
            #     label v as discovered
                visited.add(vertex)
            #     for each edge from v to w:
                for u in self.get_vertex(vertex).neighbors:
            #       S.push(w)
                    stack.appendleft(u)


# Challenge 3: Stretch Challenge
# Implement BinaryMinHeap using a dynamic array and then implement Priory Queue using BinaryMinHeap.

# Challenge 4
    





# Attribution: Meredith challenge 1 solution used the iter method, also used the slides pseudocode
