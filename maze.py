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
                win: Window
                ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.rows = rows
        self.colms = colms
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells: list[list[Cell]] = []
        self._create_cells()

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

    def _animate(self) -> None:
        self.win.redraw()
        sleep(ANIMATION_DELAY)
