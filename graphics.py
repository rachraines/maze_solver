from tkinter import Tk, BOTH, Canvas
import time

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
    def __init__(self, x1, x2, y1, y2, win=None):
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

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        # Initialize all cells list as a list of lists
        self._cells = []
        
        for col in range(self.num_cols):            
            # Creates a new list for each column
            col_list = []
            
            # Creates a cell for each row item in the column
            for row in range(self.num_rows):
                x1, x2, y1, y2 = self._draw_cell(row, col)
                cell = Cell(x1, x2, y1, y2, self.win)
                col_list.append(cell)
            
            self._cells.append(col_list)

    def _draw_cell(self, i, j):
        # Calculates left and right side of the cell
        x1 = self.x1 + j * self.cell_size_x
        x2 = x1 + self.cell_size_x

        # Calculates top and bottom of the cell
        y1 = self.y1 + i * self.cell_size_y
        y2 = y1 + self.cell_size_y

        # Draws the cell
        if self.win is not None:
            canvas = self.win._Window__canvas
            cell = Cell(x1, x2, y1, y2)
            cell.draw(canvas)
        
            self._animate()
        return x1, x2, y1, y2

    def _animate(self):
        if self.win is not None:
            self.win.redraw()
            time.sleep(0.05)
            