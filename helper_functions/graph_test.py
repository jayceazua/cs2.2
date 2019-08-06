import unittest
from graph import Graph
from vertex import Vertex


class GraphTest(unittest.TestCase):
    def test_add_vertex(self):
        g = Graph()
        g.add_vertex("A")
        g.add_vertex("B")

        assert g.get_order() == 2
        self.assertIsInstance(g.get_vertex("A"), Vertex)

    def test_add_edge(self):
        g = Graph()
        g.add_vertex("A")
        g.add_vertex("B")
        g.add_vertex("C")

        g.add_edge("A", "B")
        g.add_edge("A", "C", 3)

        assert g.get_order() == 3
        assert g.get_size() == 2

        g.add_edge("D", "F")

        assert g.get_order() == 5
        assert g.get_size() == 3


if __name__ == "__main__":
    unittest.main()

