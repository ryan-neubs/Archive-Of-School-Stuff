# Circles.py
# by Ryan Neubauer
# This program creates 5 identical circles to span accross an 800x600 window

from graphics import *

def main():
    win = GraphWin("Cirlce.py", 600, 800)
    p = Point(60,400)
    p.draw(win)
    for i in range(5):
        circ = Circle(p,60)
        circ.draw(win)
        circ.setFill('red')
        p.move(120,0)
    win.getMouse()
        
main()
    
