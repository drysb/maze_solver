#Creating Cell Class in seperate file
from visuals import Line, Point

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        fill_color = 'black'
        #Check each wall to see if it should be drawn
        if self.has_left_wall == True:
            left_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_line, fill_color)
        if self.has_right_wall == True:
            right_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_line, fill_color)
        if self.has_top_wall == True:
            top_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top_line, fill_color)
        if self.has_bottom_wall == True:
            bottom_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom_line, fill_color)

        