from window import Window
from cell import Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell1.has_bottom_wall = False
    #cell.has_left_wall = False
    #cell.has_right_wall = False
    cell1.has_top_wall = False
    cell1.draw(100,100,300,300)

    cell2 = Cell(win)
    cell2.draw(400,100, 600, 300)

    cell1.draw_move(cell2,True)

    win.wait_for_close()

if __name__ == "__main__":
    main()