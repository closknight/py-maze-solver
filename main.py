from window import Line, Point, Window

def main():
    win = Window(800, 600)
    line1 = Line(Point(10,100), Point(200,300))
    win.draw_line(line1,"green")
    win.wait_for_close()

if __name__ == "__main__":
    main()