from maze import Maze
from window import Window

def main():
    win = Window(800, 600)
    rows = 5
    colms = 10
    maze = Maze(10,10,rows,colms,50,70,win)

    win.wait_for_close()

if __name__ == "__main__":
    main()