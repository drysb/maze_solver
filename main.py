#Currently used to test output
def main():
    win = Window(800, 600)
    p1 = Point(1,2)
    p2 = Point(50,100)
    p3 = Point(100,450)
    new_line = Line(p1, p2)
    new_line2 = Line(p2, p3)
    win.draw(new_line, "yellow")
    win.draw(new_line2, "blue")
    win.wait_for_close()

main()
