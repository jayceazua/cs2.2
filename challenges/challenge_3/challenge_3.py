import sys
from file_reader import read_from_file



if __name__ == "__main__":
  file_name = sys.argv[1]
  from_v = sys.argv[2]
  to_u = sys.argv[3]
  g = read_from_file(file_name)
  is_path = g.r_depth_first_search(from_v, to_u)
  print(f'There exists a path between vertex {from_v} and {to_u}: {is_path}')
  print("Vertices in the path:", g.dfs_path)


# There exists a path between vertex 1 and 5: TRUE
# Vertices in the path: 1, 2, 3, 5
