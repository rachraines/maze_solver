from graphics import Window, Line, Point, Cell

def main():
    # Create a window with dimensions 800x600
    win = Window(800, 600)
    
    # Acccess the canvas from the window object
    canvas = win._Window__canvas

    #line1 = Line(Point(50, 50), Point(100, 100))
    #win.draw_line(line1)
   
    cell1 = Cell(50, 100, 50, 100, win)
    cell1.draw(canvas)
    
    cell2 = Cell(110, 160, 50, 100, win)
    cell2.has_top_wall = False
    cell2.draw(canvas)

    cell3 = Cell(170, 220, 50, 100, win)
    cell3.has_left_wall = False
    cell3.has_bottom_wall = False
    cell3.draw(canvas)

    cell4 = Cell(230, 280, 50, 100, win)
    cell4.has_top_wall = False
    cell4.has_left_wall = False
    cell4.has_bottom_wall = False
    cell4.draw(canvas)

    win.wait_for_close()

main()