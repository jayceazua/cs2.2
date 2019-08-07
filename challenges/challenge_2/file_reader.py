from graph import Graph

def read_from_file(file_name):
    """
    This functions reads from a filename given and returns a graph object.
    """
    file = open(file_name, "r")
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
        if len(new_edge) == 3:
            weight = int(new_edge[2])
        else:
            weight = None

        # Add edge/s
        g.add_edge(v, u, weight)

        if is_bidirectional:
            g.add_edge(u, v, weight)

    return g


if __name__ == "__main__":
    read_from_file(
        "/Users/giru/Desktop/cs_2-2/challenges/challenge_2/graph_data.txt")
# Attribution: Challenge 1 solution Meredith and Jake Shams
