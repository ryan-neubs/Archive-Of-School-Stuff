# test_buttton.py

from button import Button
from graphics import *

def main():

    win = GraphWin()
    b = Button(win, Point(100, 100), 70, 40, "Click Me!")
    b.activate()
    
    while True:

        p = win.getMouse()
        if b.clicked(p):
            if b.getLabel() == "Quit":
                break
            b.setLabel("Quit")

    win.close()


if __name__ == "__main__":
    main()
