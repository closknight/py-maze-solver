import random
from time import sleep
from cell import Cell
from window import Window

ANIMATION_DELAY = 0.05

class Maze():
    def __init__(self,
                x1: int,
                y1: int,
                rows: int,
                colms: int,
                cell_size_x: int,
                cell_size_y: int,
                win: Window = None,
                seed = None
                ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.rows = rows
        self.colms = colms
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells: list[list[Cell]] = []
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()


    
    def solve(self) -> bool:
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j) -> bool:
        self._animate()
        cell: Cell = self._cells[i][j]
        cell.visited = True
        if i == self.colms - 1 and j == self.rows - 1:
            return True
        # left
        if not cell.has_left_wall and i - 1 >= 0 and not self._cells[i - 1][j].visited:
            print(i,j, "left")
            cell.draw_move(self._cells[i - 1][j])
            solved = self._solve_r(i - 1, j)
            if solved:
                return True
            cell.draw_move(self._cells[i - 1][j], undo=True)
        # right
        if not cell.has_right_wall and i + 1 < self.colms and not self._cells[i + 1][j].visited:
            print(i,j, "right")
            cell.draw_move(self._cells[i + 1][j])
            solved = self._solve_r(i + 1, j)
            if solved:
                return True
            cell.draw_move(self._cells[i + 1][j], undo=True)
        # up
        if not cell.has_top_wall and j - 1 >= 0 and not self._cells[i][j - 1].visited:
            print(i,j, "up")
            cell.draw_move(self._cells[i][j - 1])
            solved = self._solve_r(i, j - 1)
            if solved:
                return True
            cell.draw_move(self._cells[i][j - 1], undo=True)
        #down
        if not cell.has_bottom_wall and j + 1 < self.rows and not self._cells[i][j + 1].visited:
            print(i,j, "down")
            cell.draw_move(self._cells[i][j + 1])
            solved = self._solve_r(i, j + 1)
            if solved:
                return True
            cell.draw_move(self._cells[i][j + 1], undo=True)
        return False
        
    def _create_cells(self) -> None:
        for _ in range(self.colms):
            colm = []
            for _ in range(self.rows):
                colm.append(Cell(self.win))
            self._cells.append(colm)

        for i in range(self.colms):
            for j in range(self.rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j) -> None:
        if self.win is None:
            return
    
        x1 = self.x1 + (i * self.cell_size_x)
        y1 = self.y1 + (j * self.cell_size_y)
        self._cells[i][j].draw(x1, y1, x1 + self.cell_size_x, y1 + self.cell_size_y)
        self._animate()

    def _break_entrance_and_exit(self):
        if len(self._cells) < 1 or len(self._cells[0]) < 1:
            return
        
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)

        i = self.colms - 1
        j = self.rows - 1
        self._cells[i][j].has_bottom_wall = False
        self._draw_cell(i, j)

    def _reset_cells_visited(self):
        for col in range(self.colms):
            for cell in self._cells[col]:
                cell.visited = False
        

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i - 1 >= 0 and not self._cells[i - 1][j].visited:
                to_visit.append("left")
            if j - 1 >= 0 and not self._cells[i][j - 1].visited:
                to_visit.append("up")
            if i + 1 < self.colms and not self._cells[i + 1][j].visited:
                to_visit.append("right")
            if j + 1 < self.rows and not self._cells[i][j + 1].visited:
                to_visit.append("down")
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                break
            direction = random.choice(to_visit)
            # print(i, j, direction)
            if direction == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
                self._break_walls_r(i - 1, j)
            elif direction == "up":
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
                self._break_walls_r(i, j - 1)
            elif direction == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
                self._break_walls_r(i + 1, j)
            else: #direction == "down"
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
                self._break_walls_r(i, j + 1)
            
    def _animate(self) -> None:
        self.win.redraw()
        sleep(ANIMATION_DELAY)
