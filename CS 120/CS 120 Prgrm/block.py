# jumpy.py
# by: Ryan Neubauer
# This program draws a square where you click your mouse

from graphics import *

def main():
    win = GraphWin("Click Window", 400, 400)
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    
    for i in range(20):
        p = win.getMouse()
        px = p.getX() - 10
        py = p.getY() - 10
        dx = px + 20
        dy = py + 20
        shape = Rectangle(Point(px, py), Point(dx, dy))
        shape.setFill("red")
        shape.setOutline("red")
        shape.draw(win)

    win.close()


main()
