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

class Cell:
    def __init__(self, x1, x2, y1, y2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    # Draws cells
    def draw(self, canvas, fill_color="white"):
        if self.has_left_wall:
            canvas.create_line(self._x1, self._y1, self._x1, self._y2, fill=fill_color, width=3)
        if self.has_top_wall:
            canvas.create_line(self._x1, self._y1, self._x2, self._y1, fill=fill_color, width=3)
        if self.has_right_wall:
            canvas.create_line(self._x2, self._y1, self._x2, self._y2, fill=fill_color, width=3)
        if self.has_bottom_wall:
            canvas.create_line(self._x1, self._y2, self._x2, self._y2, fill=fill_color, width=3)

    # Draws a line through the middle of the cell to track user movement throughout maze
    def draw_move(self, to_cell, canvas, undo=False):
        fill_color = "red" if not undo else "gray"

        # Center of the current cell
        mid_x1 = (self.x1 + self.x2) / 2
        mid_y1 = (self.y1 + self.y2) / 2

        # Center of the new cell
        mid_x2 = (to_cell.x1 + to_cell.x2)/2
        mid_y2 = (to_cell.y1 + to_cell.y2)/2

        canvas.create_line(mid_x1, mid_y1, mid_x2, mid_y2, fill=fill_color, width=2)