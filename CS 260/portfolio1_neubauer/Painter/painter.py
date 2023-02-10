# painter.py

"""
Class for simple 2D drawing

A Painter wraps a raw raster image to make drawing into the image
more convenient. Whereas pixel coordinates are integers, a painter allows
floating point coordinates and provides methods for drawing geometric figures.
"""


from collections import namedtuple
from math import pi, sin, cos, floor, ceil
from random import randrange

# Image is in another directory for organization purposes so I
# added the file path here.
import sys
sys.path.insert(1, '..\Image')


location2d = namedtuple("location2d", 'x y')
# named tuple to represent locations in an image
#   A location2d is a tuple (x, y) and functions like a
#   regular tuple, but also allows access via attributes x and y
#   example:
#      p = location2d(3, 5)
#      x, y = p
#      total = x + y
#    or
#      total = p.x + p.y


def _pixloc(loc):
    """returns the pixloc that is closest to Painter location

    Note: Painter locations are in natural image coordinates (x, y)
          where x and y are floats: -0.5 < x < width - 0.5 and -0.5 <
          y < height - 0.5

    """
    x, y = loc
    return location2d(round(x), round(y))

def genlinefunc(a, b):
        x0, y0 = a
        x1, y1 = b
        def fn(p):
            x, y = p
            return (y0 - y1) * x + (x1 - x0) * y + (x0 * y1 - x1 * y0)
        return fn


class Painter:
    """Tool for drawing geometric figures into images

    A Painter wraps an Image and supplies two conveniences
    1) A continuous image coordinate system (location coords can be floats)
    2) Drawing primitives for points, lines, circles, triangles, and polygons
    """

    def __init__(self, image):
        self.color = (0, 0, 0)  # default drawing color is black
        self.image = image
        self.viewport = (0, 0, self.image.size[0], self.image.size[1])

    def draw_point(self, loc):
        """draw point at loc"""
        pixloc = _pixloc(loc)
        if self.viewport[0] <= loc[0] <= self.viewport[2] and self.viewport[1] <= loc[1] < self.viewport[3]:
            self.image[pixloc] = self.color

    def draw_line(self, a, b):
        """  draw line segment from point a to point b """
        a = _pixloc(a)
        b = _pixloc(b)
        if a == b:
            self.draw_point(a)
        else:
            if a[0] > b[0]:
                a, b = b, a
            x0, y0 = a
            x1, y1 = b
            dx = x1 - x0
            dy = y1 - y0
            x, y = x0, y0
            if (abs(dx) >= abs(dy)):
                for x in range(x0, x1):
                    self.draw_point((x, y))
                    y += dy/dx
            else:
                if a[1] > b[1]:
                    y0, y1 = y1, y0
                    x = x1
                for y in range(y0, y1):
                    self.draw_point((x, y))
                    x += dx/dy
        
    

    def draw_lines(self, points):
        """draw polyline that connects the given points"""
        for i in range(len(points)-1):
            self.draw_line(points[i], points[i+1])

    def draw_polygon(self, vertices):
        """ draw polygon with given vertices """
        self.draw_lines(vertices)
        self.draw_line(vertices[-1], vertices[0])
        

    def draw_circle(self, center, radius, segments=50):
        """draw a cricle with the given center and radius 

        note: actually draws a regular polygon having segments sides

        """
        pts = []
        dtheta = (2*pi)/segments
        theta = 0
        while theta < 2*pi:
            x = radius * cos(theta) + center[0]
            y = radius * sin(theta) + center[1]
            pts.append((x,y))
            theta += dtheta
        self.draw_polygon(pts)

    def draw_filled_triangle(self, a, b, c):
        """ draw filled triangle with vertices a, b, and c """
        fac = genlinefunc(a, c)
        fbc = genlinefunc(b, c)
        fab = genlinefunc(a, b)
        minx = min(a[0], b[0], c[0])
        maxx = max(a[0], b[0], c[0])
        miny = min(a[1], b[1], c[1])
        maxy = max(a[1], b[1], c[1])
        for x in range(floor(minx), ceil(maxx)+1):
            for y in range(floor(miny), ceil(maxy) + 1):
                alpha = fbc((x,y))/fbc(a)
                beta = fac((x,y))/fac(b)
                gamma = fab((x,y))/fab(c) # Could also be 1 - alpha - beta
                if alpha >= 0 and beta >= 0 and gamma >= 0:
                    self.draw_point((x,y))

    def draw_filled_polygon(self, vertices):
        """draw filled polygon with the given vertices

        note: vertices should describe a convex polygon

        """
        p1 = vertices[0]
        p2 = vertices[1]
        for v in vertices[2:len(vertices)]:
            p3 = v
            self.draw_filled_triangle(p1,p2,p3)
            p2 = v
        

    def draw_filled_circle(self, center, radius, segments = 50):
        center = _pixloc(center)
        xlow = int(center[0] - radius)
        xhigh = int(center[0] + radius)
        ylow = int(center[1] - radius)
        yhigh = int(center[1] + radius)
        for x in range(xlow, xhigh + 1):
            for y in range(ylow, yhigh + 1):
                if (((x-center[0])**2) + ((y-center[1])**2) - radius**2) < 0:
                    self.draw_point((x,y))
                

        
if __name__ == "__main__":
    from image import Image
    img = Image((400, 300))
    img.clear((255, 255, 255))
    s = Painter(img)
    s.draw_point((100, 25))
    s.color = (255, 0, 0)
    s.draw_point((200.7, 295.3))
    s.draw_line((0.5, 0), (200, 30.4))
    s.draw_line((50.2, 100.6), (60, 250))
    s.draw_circle((200.4, 150.1), 100, 50)
    s.color = (0, 255, 0)
    s.draw_lines([(0, 0), (10.3, 30), (10, 50)])
    s.draw_polygon([(50, 50.1), (100, 50), (100, 100), (50, 100)])
    s.color = (255, 0, 0)
    s.draw_filled_triangle((150, 150), (250, 150), (200, 200))
    s.color = (128, 46, 243)
    s.draw_filled_circle((350.5, 75.2), 30)
    s.color = (86, 37, 28)
    s.draw_filled_polygon([(380, 225.25), (359, 254), (326, 243),
                           (326, 207), (359, 196)])
    img.save("painter_test.ppm")
    img.show()
    input("Press Enter to close.")
    img.unshow()
    input("Press Enter to view next image.")
    img = Image((400,400))
    img.clear((255,255,255))
    s = Painter(img)
    radius = 100
    while radius > 5:
        s.draw_filled_circle((200,200), radius, 50)
        s.color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
        radius -= 5
    img.show()
    input("Press Enter to close.")
    img.unshow()
    input("Press Enter to view next image.")
    img = Image((400,400))
    img.clear((255,255,255))
    s = Painter(img)
    radius = 100
    r = 255
    g = 255
    b = 255
    while radius > 1:
        s.draw_filled_circle((200,200), radius, 50)
        r -= 1
        g -= 3
        b -= 5
        s.color = (r, g, b)
        radius -= 3
    img.show()
    input("Press Enter to close.")
    img.unshow()
    
