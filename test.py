import unittest
from main import dfs
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestBfs(TestCase):
    def test_output_contains_header(self):
        graph = {1: {2}, 2: {1}}
        start_vertex = 1
        with patch('sys.stdout', new=StringIO()) as fake_output:
            dfs(graph, start_vertex)
            self.assertIn("vertex\tDFS \tStack", fake_output.getvalue())

class TestBFS(unittest.TestCase):

    def setUp(self):
        self.graph = {
            0: {1, 2},
            1: {0, 2, 3},
            2: {0, 1, 3},
            3: {1, 2}
        }
        self.start_vertex = 0
        self.expected_output = "vertex\tDFS \tStack"

    def test_bfs_output(self):
        buffer = StringIO()



if __name__ == '__main__':
    unittest.main()

