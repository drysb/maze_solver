#Importing necessary packages
from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.title("Solve the Maze")

        self.canvas_w = Canvas()
        self.canvas_w.pack()
        self.window_run = False

        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.window_run = True
        while self.window_run == True:
            self.redraw()

    def close(self):
        self.window_run = False

def main(self):
    win = Window(800, 600)
    win.wait_for_close()