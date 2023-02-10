# face5.py
# by Ryan Neubauer

from graphics import *
import math

def main():

    win = GraphWin("5 Click Face", 300, 300)
    win.setCoords(0, 0, 300, 300)

    # Click for face center point
    msg = Text(Point(150, 10), "Click for the center of the face.")
    msg.draw(win)
    p1 = win.getMouse()

    # Click for face radius
    msg.setText("Click for the edge of the face.")
    p2 = win.getMouse()
    radius = math.hypot(p2.getX()- p1.getX(), p2.getY() - p1.getY())

    # Drawing of radius                    
    head = Circle(p1,radius)
    head.draw(win)
    head.setFill("yellow")

    # Click for top of the nose
    msg.setText("Click the lower-left corner of the nose.")
    p3 = win.getMouse()
    diff = p1.getX() - p3.getX()
    right = Point((p1.getX() + diff), p3.getY())
    nose = Polygon(p3,p1,right)
    nose.draw(win)
    nose.setFill("red")

    # Click for location of the left eye
    msg.setText("Click for the location of the left eye.")
    p4 = win.getMouse()
    eyeRad = radius/10
    leftEye = Circle(p4,eyeRad)
    rightEyeLoc = Point(p1.getX() + (p1.getX() - p4.getX()), p4.getY())
    rightEye = Circle(rightEyeLoc, eyeRad)
    leftEye.draw(win)
    rightEye.draw(win)
    leftEye.setFill("black")
    rightEye.setFill("black")

    # Lower-left click for mouth
    msg.setText("Click the lower left of the mouth")
    p5 = win.getMouse()
    tl = Point(p1.getX() + (p1.getX() - p5.getX()), p5.getY() + eyeRad)
    mouth = Oval(p5,tl)
    mouth.draw(win)
    mouth.setFill("Pink")

    # Finish message
    msg.setText("Nice Job! Click to quit.")
    win.getMouse()
    win.close()
    


main()
