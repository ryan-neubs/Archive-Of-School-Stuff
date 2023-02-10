# face.py
# This program draws a simple face
# By Ryan Neubauer

from graphics import *

def main():

    # Create Graphics Window
    win = GraphWin("Face", 500, 500)
    #win.setCoords(0.0, 0.0, 3.0, 4.0)

    # Draw Face
    center = Point(250, 250)
    face = Circle(center, 150)
    face.draw(win)
    face.setFill("peachpuff")

    # Draw Eyes
    center.move(-50,-15)
    for i in range(2):
        eye = Circle(center, 15)
        eye.draw(win)
        eye.setFill("Black")
        center.move(100,0)
    
    # Draw Mouth
    x = 180
    y = 290
    z = 320
    v = 335
    mouthPart1 = Oval(Point(x, y), Point(z, v))
    mouthPart1.draw(win)
    mouthPart1.setFill("Black")
    mouthPart2 = Oval(Point(x-10, y-10), Point(z+10, v-10))
    mouthPart2.draw(win)
    mouthPart2.setFill("peachpuff")
    mouthPart2.setOutline("peachpuff")

    # Wait for mouseclick to close
    win = win.getMouse()

main()

