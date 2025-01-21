from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        # Create the root widget
        self.root = Tk()
        self.root.title("Maze Solver") # Set the title of the window

        # Create a Canvas widget
        self.canvas = (self.root, width, height, background="black")
        self.canvas.pack(fill=Both, expand=True) # Pack the canvas so it can be drawn

        # Represents the running state
        self.running = False

        