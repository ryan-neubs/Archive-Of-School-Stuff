# hello_graphics.py

from graphics import *

def main():

    # opens a graphics window titles hello with the dimensions of 500x300 pixels
    win = GraphWin("hello", 500, 300)
    # creates the greeting which will be at point (250, 150) witht the string
    # Hello, CS 120
    greeting = Text(Point(250, 150), "Hello, CS 120")
    # sets the text size to 32 pixels
    greeting.setSize(32)
    # draws the text on the GraphWin
    greeting.draw(win)

    # wait for a mouse click in the window object
    win.getMouse()

main()
