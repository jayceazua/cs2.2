from vertex import Vertex
import unittest


class VertexTest(unittest.TestCase):
    def test_add_neighbor(self):
        v1 = Vertex("A")
        v2 = Vertex("B")
        v3 = Vertex("C")

        v1.add_neighbor(v2)
        v1.add_neighbor(v3, 3)

        assert len(v1.neighbors) == 2
        assert v1.neighbors[v2] == 1
        assert v1.neighbors[v3] == 3


if __name__ == "__main__":
    unittest.main()
