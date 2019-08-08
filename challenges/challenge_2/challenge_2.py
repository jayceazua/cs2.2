import sys
from file_reader import read_from_file


if __name__ == "__main__":
    file_name = sys.argv[1]
    g = read_from_file(file_name)
    from_v = sys.argv[2]

    to_u = sys.argv[3]

    shortest_path = g.shortest_path(from_v, to_u)
    print(f'Vertices in shortest path: {", ".join(shortest_path)}')
    print(f'Number of edges in shortest path: {len(shortest_path) - 1}')


# Need help debugging but it should work once i fix the bug of the vertex_key
# got pseudocode from the slides for this problem of challenge 2
