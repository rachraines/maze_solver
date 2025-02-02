from graphics import Window, Line, Point, Cell, Maze

def main():
    # Define maze dimensions
    win_width = 800
    win_height = 600
    num_rows = 9
    num_cols = 10
    cell_size_x = 20
    cell_size_y = 20

    # Create the window
    win = Window(win_width, win_height)
    
    # Acccess the canvas from the window object
    canvas = win._Window__canvas

    # Create the maze
    maze = Maze(10, 10, num_rows, num_cols, cell_size_x, cell_size_y, win)
    
    # Generate the maze layout using recursive wall breaking
    maze._break_walls_r(0, 0)
    
    # Reset visited status for solving
    maze._reset_cells_visited

    # Solve the maze
    solved = maze._solve_r(0, 0)

    if solved:
        print("Maze solved successfully!")
    else:
        print("Maze could not be solved.")

    # Keep window open until closed by user
    win.wait_for_close()

main()