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

    def test_maze_entrence_and_exit(self):
        colms = 15
        rows = 10
        m1 = Maze(0,0,rows, colms, 10, 10)
        m1._break_entrance_and_exit()
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[14][9].has_bottom_wall)

        m2 = Maze(0, 0, 1, 1, 10, 10)
        m2._break_entrance_and_exit()
        self.assertFalse(m2._cells[0][0].has_top_wall)
        self.assertFalse(m2._cells[0][0].has_bottom_wall)

    def test_maze_visited_reset(self):
            rows = 20
            colms = 20
            maze = Maze(10,10,rows,colms,10,10,seed=0)
            maze._break_entrance_and_exit()
            maze._break_walls_r(5,5)
            self.assertTrue(maze._cells[0][0].visited)
            maze._reset_cells_visited()
            for col in maze._cells:
                for cell in col:
                    self.assertFalse(cell.visited)




if __name__ == "__main__":
    unittest.main()
