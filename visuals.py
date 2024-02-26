#Importing necessary packages
from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Solve the Maze")

        self.canvas_w = Canvas(self.root, width = width, height = height)
        self.canvas_w.pack()
        self.window_run = False

        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def draw(self, Line, fill_color):
        Line.draw(self.canvas_w, fill_color)
    
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.window_run = True
        while self.window_run == True:
            self.redraw()

    def close(self):
        self.window_run = False

#Define a singular point 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Defines Line
class Line:
    def __init__(self, point_1, point_2):
        self.x1 = point_1.x
        self.y1 = point_1.y
        self.x2 = point_2.x
        self.y2 = point_2.y


    def draw(self, canvas, fill_color):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2)
        canvas.pack()