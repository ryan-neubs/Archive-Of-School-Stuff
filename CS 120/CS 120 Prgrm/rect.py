# rect.py
# By Ryan Neubauer
# This program makes a rectangle out of two selected points

from graphics import *

def main():
    win = GraphWin("Draw a rectangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on two points")
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    rect = Rectangle(p1,p2)
    rect.setFill("peachpuff")
    rect.setOutline("black")
    rect.draw(win)

    message.setText("Click to quit.")
    win.getMouse()
    win.close()

main()
