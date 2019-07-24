import unittest
from graph import Vertex, Graph


class VertexTest(unittest.TestCase):

    def test_init(self):
        vertex_1 = Vertex('A')
        assert vertex_1.getId() is 'A'
        assert vertex_1.neighbors == {}


class GraphTest(unittest.TestCase):
    pass
