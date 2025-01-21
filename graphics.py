from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        # Create the root widget
        self.__root = Tk()
        self.__root.title("Maze Solver") # Set the title of the window

        # Create a Canvas widget
        self.__canvas = Canvas(self.__root, bg="black", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1) # Pack the canvas so it can be drawn

        # Represents the running state
        self.__running = False

        # Stops the program from running when window is closed
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    # Window will redraw itself when function is called
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    # Coninues to draw window until it is closed
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    # Closes window
    def close(self):
        self.__running = False


    # Draws a line in the canvas
    def draw_line(self, line, fill_color="white"):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.start = point1
        self.end = point2

    # Draws line on a given canvas
    def draw(self, canvas, fill_color="white"):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2
        )