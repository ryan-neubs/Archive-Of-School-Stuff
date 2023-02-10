# quickhull.py
from graphics import *
from random import randint
from math import *
from time import sleep

convexhull = []
win = GraphWin("Quickhull",520,520)
win.setCoords(-10,-10,510,510)

def determ(p1,p2,p3):
    p1x,p1y = p1 #A
    p2x,p2y = p2 #C
    p3x,p3y = p3 #B

    #area = abs((p1x * (p3y-p2y) + p3x * (p2y-p1y) + p2x * (p1y-p3y))/2) - Will give pmax (not sure where to use yet)
    return (p1x * p2y) + (p3x * p1y) + (p2x * p3y) - (p3x * p2y) - (p2x * p1y) - (p1x * p3y)
    #Returns signed distance

def quickhull(s):
    # Find convex hull from the set of n points
    s.sort()
    convexhull.append(min(s))
    convexhull.append(max(s))
    p1 = min(s)
    pn = max(s)
    p1p = Point(p1[0], p1[1])
    pnp = Point(pn[0], pn[1])
    cp1 = Circle(p1p, 3)
    cpn = Circle(pnp, 3)
    cp1.draw(win)
    cpn.draw(win)
    cp1.setFill('red')
    cpn.setFill('red')
    line = Line(Point(p1[0], p1[1]), Point(pn[0], pn[1]))
    line.draw(win)
    
    halfhull(p1,pn,[p for p in s if determ(p1,pn,p) > 0])
    print('next half1')
    halfhull(p1,pn,[p for p in s if determ(p1,pn,p) < 0])

def halfhull(p1,pn,s):
    print(s)
    circles = []
    for x in s:
        po = Point(x[0], x[1])
        poc = Circle(po, 3)
        circles.append(poc)
        poc.draw(win)
        poc.setFill('green')
    area = lambda p1,p2,p3: abs((p1[0] * (p3[1]-p2[1]) + p3[0] * (p2[1]-p1[1]) + p2[0] * (p1[1]-p3[1]))/2)
    if len(s) == 0: return # if set is empty
        # dividing line is part of the convex hull so we return
    
    # Find farthest point from p1 to pn
    furthest = s[0]
    for point in s:
        if area(p1,pn,point) > area(p1,pn,furthest):
            s.remove(furthest)
            furthest = point

    p1p = Point(p1[0], p1[1])
    pnp = Point(pn[0], pn[1])
    cp1 = Circle(p1p, 3)
    cpn = Circle(pnp, 3)
    cp1.draw(win)
    cpn.draw(win)
    cp1.setFill('red')
    cpn.setFill('red')
    
    line1 = Line(Point(p1[0], p1[1]), Point(furthest[0], furthest[1]))
    line1.draw(win)
    line2 = Line(Point(pn[0], pn[1]), Point(furthest[0], furthest[1]))
    line2.draw(win)

    s.remove(furthest)
    ptest = Point(furthest[0], furthest[1])
    c = Circle(ptest, 2)
    c.draw(win)
    c.setFill('blue')
    win.getMouse()
    c.setFill('black')
    cp1.setFill('black')
    cpn.setFill('black')
    for circle in circles:
        circle.setFill('black')
    convexhull.insert(1, furthest)

    halfhull(p1,furthest,[p for p in s if determ(p1, furthest, p) > 0])
    print('pmax to pn')
    halfhull(furthest,pn,[p for p in s if determ(furthest, pn, p) < 0])

def main():
    points = []
    print("Welcome to quickhull.py")
    print("This program simulates the quickhull solution to convex hull.")
    n = int(input("Enter the amount of points that should be in the set: "))
    for i in range(n):
        p = tuple([randint(150,350), randint(150,350)])
        points.append(p)
        point = Point(p[0],p[1])
        point.draw(win)
    quickhull(points)
    print(len(convexhull))
    print(convexhull)
    win.getMouse()
    win.close()

main()
