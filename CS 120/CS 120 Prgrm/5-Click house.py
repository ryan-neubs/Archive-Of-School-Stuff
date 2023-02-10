# house.py


from graphics import *

def main():

    # Creates window for program
    win = GraphWin("5-Click House", 400, 400)
    win.setCoords(0,0,10,10)

    
    # Creates text at the bottom of the screen
    # Drawing a point for one of the corners of the frame
    msg = Text(Point(5, .5),"Click lower-left corner of the house")
    msg.draw(win)
    p1 = win.getMouse()
    p1.draw(win)

    # Creating the main frame of the house
    msg.setText("Click the upper right corner of the house.")
    p2 = win.getMouse()
    frame = Rectangle(p1,p2)
    frame.draw(win)
    frame.setFill("brown")

    # Drawing of the door
    msg.setText("Click center of the top of the door")
    p3 = win.getMouse()
    houseWidth = p2.getX()- p1.getX()
    xdll = p3.getX() - (0.1 * houseWidth)
    dll = Point(xdll, p1.getY())
    dll.draw(win)
    xdur = p3.getX() + (0.1 * houseWidth)
    dur = Point(xdur,p3.getY())
    door = Rectangle(dll, dur)
    door.draw(win)
    door.setFill("red")

    # Draws the window
    msg.setText("Click center of the window")
    p4 = win.getMouse()
    winwidth = (0.1 * houseWidth)
    wll = p4.clone()
    wll.move(-winwidth/2, -winwidth/2)
    wur = wll.clone()
    wur.move(winwidth, winwidth)
    window = Rectangle(wll, wur)
    window.setFill("black")
    window.draw(win)

    # Drawing for roof
    msg.setText("Click on peak of the roof.")
    p5 = win.getMouse()
    rp = Point(p1.getX(), p2.getY())
    roof = Polygon(p5, p2, rp)
    roof.setFill("Green")
    roof.draw(win)

    # Waiting for click to change background to night time
    msg.setText("Click for nightfall")
    win.getMouse()
    win.setBackground("black")
    window.setFill("yellow")

    # Closes window on final mouse click
    win.getMouse()
    win.close()



main()
