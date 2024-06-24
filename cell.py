from window import Line, Point, Window

class Cell():
    def __init__(self, win: Window = None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win: Window = win
        self.visited = False

    def draw(self, x1:int, y1:int, x2:int, y2:int) -> None:        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        top_left = Point(x1, y1)
        top_right = Point(x2, y1)
        bottom_left = Point(x1, y2)
        bottom_right = Point(x2, y2)
        color = "black" if self.has_left_wall else "white"
        self._win.draw_line(Line(top_left, bottom_left), fill_color=color)
        color = "black" if self.has_right_wall else "white"
        self._win.draw_line(Line(top_right, bottom_right), fill_color=color)
        color = "black" if self.has_top_wall else "white"
        self._win.draw_line(Line(top_left, top_right), fill_color=color)
        color = "black" if self.has_bottom_wall else "white"
        self._win.draw_line(Line(bottom_left, bottom_right), fill_color=color)


    def center(self) -> Point:
        return Point((self._x1 + self._x2)//2, (self._y1 + self._y2)//2)

    def draw_move(self, to_cell: "Cell", undo: bool=False):
        fill_color = "gray" if undo else "red"
        move_line = Line(self.center(), to_cell.center())
        self._win.draw_line(move_line, fill_color=fill_color)