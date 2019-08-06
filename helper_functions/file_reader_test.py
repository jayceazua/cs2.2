import unittest
from file_reader import read_from_file


class FileInputTest(unittest.TestCase):

    def test_input(self):
        result_graph = read_from_file("test_inputs/simple.txt")
        self.assertEqual(4, result_graph.num_vertices)
        self.assertCountEqual(
            result_graph.get_vertices(),
            ['1', '2', '3', '4'])

        self.assertEqual(6, result_graph.get_num_edges())
        self.assertCountEqual(
            [('1', '2'), ('1', '3'), ('2', '1'),
             ('2', '4'), ('3', '1'), ('4', '2')],
            result_graph.get_edges())

    def test_weighted(self):
        result_graph = read_from_file("test_inputs/weighted.txt")
        self.assertEqual(5, result_graph.num_vertices)
        self.assertCountEqual(
            result_graph.get_vertices(),
            ['1', '6', '10', '15', '21'])

        self.assertEqual(6, result_graph.get_num_edges())
        self.assertCountEqual(
            [
                ('1', '6', 9),
                ('6', '10', 4),
                ('6', '15', 2),
                ('21', '10', 3),
                ('15', '1', 10),
                ('1', '21', 5)
            ],
            result_graph.get_edges_weighted())


if __name__ == "__main__":
    unittest.main()


# Attribution: Challenge 1 solution Meredith, and Jake Shams
