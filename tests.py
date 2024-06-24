import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        colms = 12
        rows = 10
        m1 = Maze(0,0,rows, colms, 10, 10)
        self.assertEqual(len(m1._cells), colms)
        self.assertEqual(len(m1._cells[0]), rows)

    def test_maze_create_cells2(self):
        colms = 1
        rows = 100
        m1 = Maze(0,0,rows, colms, 10, 10)
        self.assertEqual(len(m1._cells), colms)
        self.assertEqual(len(m1._cells[0]), rows)


if __name__ == "__main__":
    unittest.main()
