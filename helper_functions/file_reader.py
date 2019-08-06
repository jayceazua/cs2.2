from graph import Graph


def read_from_file(filename):
    """
    This functions reads from a filename given and returns a graph object.
    """
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    # is graph undirected or directed
    if len(lines) > 0:
        directed_or_undirected = lines[0].strip()
    else:
        directed_or_undirected = None

    if directed_or_undirected != "G" and directed_or_undirected != "D":
        raise Exception("You must have a Digraph or Graph")
    is_bidirectional = directed_or_undirected == "G"

    g = Graph()
    # add the vertices
    for vertex_key in lines[1].strip("() \n").split(","):
        g.add_vertex(vertex_key)

    # add all edges
    for line in lines[2:]:
        new_edge = line.strip("() \n").split(",")
        if 2 > len(new_edge) > 3:
            raise Exception("Invalid edge")

           # Get vertices
        v, u = new_edge[:2]

        # Get weight
        weight = int(new_edge[2]) if len(new_edge) == 3 else None

        # Add edge/s
        g.add_edge(v, u, weight)

        if is_bidirectional:
            g.add_edge(u, v, weight)

    return g


# Attribution: Challenge 1 solution Meredith and Jake Shams
