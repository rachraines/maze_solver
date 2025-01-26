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
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    # Draws cells
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        fill_color = "white"
        background_color = "black"  # Matches the background color of the canvas
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        # Draw the left wall or erase it
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, fill_color)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, background_color)

        # Draw the top wall or erase it
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, fill_color)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, background_color)

        # Draw the right wall or erase it
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, fill_color)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, background_color)

        # Draw the bottom wall or erase it
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, fill_color)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, background_color)

    # Draws a line through the middle of the cell to track user movement throughout maze
    def draw_move(self, to_cell, undo=False):
        fill_color = "red" if not undo else "gray"

        # Center of the current cell
        mid_x1 = (self.x1 + self.x2) / 2
        mid_y1 = (self.y1 + self.y2) / 2

        # Center of the new cell
        mid_x2 = (to_cell.x1 + to_cell.x2)/2
        mid_y2 = (to_cell.y1 + to_cell.y2)/2

        line = Line(Point(mid_x1, mid_y1), Point(mid_x2, mid_y2))
        self._win.draw_line(line, fill_color, width=2)

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
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return

        # Calculates left and right side of the cell
        x1 = self._x1 + i * self._cell_size_x
        x2 = x1 + self._cell_size_x

        # Calculates top and bottom of the cell
        y1 = self._y1 + j * self._cell_size_y
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        
        self._animate()

    def _animate(self):
        if self._win is not None:
            self._win.redraw()
            time.sleep(0.05)
        else:
            return
    
    def _break_entrance_and_exit(self):
        # Removes top wall from top left cell
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        # Removes bottom wall from bottom right cell
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)