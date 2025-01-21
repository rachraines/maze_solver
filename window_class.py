from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        # Create the root widget
        self.root = Tk()
        self.root.title("Maze Solver") # Set the title of the window

        # Create a Canvas widget
        self.canvas = Canvas(self.root, width, height, background="black")
        self.canvas.pack(fill=BOTH, expand=True) # Pack the canvas so it can be drawn

        # Represents the running state
        self.running = False

        # Stops the program from running when window is closed
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    # Window will redraw itself when function is called
    def redraw(self):
        self.update_idletasks()
        self.update()

    # Coninues to draw window until it is closed
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    # Closes window
    def close(self):
        self.running = False