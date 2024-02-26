from visuals import Window, Point, Line
from cell import Cell   

#Currently used to test output
def main():
    win = Window(800, 600)
    cell_1 = Cell(win)
    cell_2 = Cell(win)
    cell_2.has_right_wall = False
    cell_2.has_bottom_wall = False

    cell_1.draw(100,300,200,350)
    cell_2.draw(400,450,500,550)

    win.wait_for_close()

main()
