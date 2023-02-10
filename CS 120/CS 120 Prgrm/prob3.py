# prob3.py
# by Ryan Neubauer

from button import Button
from graphics import *

def buttonClick():
    win = GraphWin("5 Tap Button", 200, 200)
    button = Button(win, Point(100, 100), 70, 20, "Click Me")
    button.activate()
    clicks = 0
    while clicks != 5:
        p = win.getMouse()
        if button.clicked(p) == True:
            clicks += 1
            print(clicks)
    win.close()

buttonClick()


