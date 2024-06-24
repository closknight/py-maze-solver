from maze import Maze
from window import Window

def main():
    win = Window(800, 600)
    rows = 10
    colms = 10
    maze = Maze(10,10,rows,colms,10,10,win)
    solved = maze.solve()
    if solved:
        print("Congrats")
    else:
        print("you lose")
    win.wait_for_close()

if __name__ == "__main__":
    main()