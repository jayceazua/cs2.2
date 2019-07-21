class Graph():
  # creates a new, empty graph.

  def addVertex(self, vert):
    pass  # adds an instance of Vertex to the graph.

  def addEdge(self, fromVert, toVert):
    pass  # Adds a new, directed edge to the graph that connects two vertices.

  def addEdgeWithWeight(self, fromVert, toVert, weight):
    # Adds a new, weighted, directed edge to the graph that connects two vertices.
    pass

  def getVertex(self, vertKey):
    pass  # finds the vertex in the graph named vertKey.

  def getVertices(self, ):
    pass  # returns the list of all vertices in the graph.

  def getNeighbors(self, x):
    pass  # lists all vertices y such that there is an edge from the vertex x to the vertex y;
