import sys
from file_reader import read_from_file



if __name__ == "__main__":
  file_name = sys.argv[1]
  from_v = sys.argv[2]
  to_u = sys.argv[3]
  g = read_from_file(file_name)
  