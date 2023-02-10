# polydraw.py
# this program converts numbers in a text document to a drawing of polygons
# by Ryan Neubauer

from graphics import *

def main():
    # get the file name
    fname = input("Enter name of file to draw: ")
    infile = open(fname, "r")

    # create graphic window
    winsize = infile.readline()
    width, height = winsize.split()
    win = GraphWin("polydraw", int(width), int(height))

    # set window coordinates
    wincoords = infile.readline()
    x1, y1, x2, y2 = wincoords.split()
    win.setCoords(int(x1), int(y1), int(x2), int(y2))
    
    # loop to draw and fill shapes

    for s in range(1876):
        line = infile.readline()
        data = line.split()
        rgbdata = data[:3]
        pointinfo = data[3:]
        points = []
        for i in range(0, len(pointinfo), 2):
            x = float(pointinfo[i])
            y = float(pointinfo[i + 1])
            p = Point(x,y)
            points.append(p)
        poly = Polygon(points)
        poly.draw(win)
        R = int(rgbdata[0])
        G = int(rgbdata[1])
        B = int(rgbdata[2])
        poly.setFill(color_rgb(R, G, B))
        #poly.setOutline(color_rgb(R, G, B))
    
    win.getMouse()
    win.close()
    

main()
