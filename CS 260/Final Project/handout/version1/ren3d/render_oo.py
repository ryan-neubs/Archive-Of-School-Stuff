# render_oo.py

from collections import namedtuple
import ren3d.matrix as mat


def render_wireframe(scene, img):
    """Render wireframe view of scene into img
    """


# ---------------------------------------------------------------------------
# Helper class
pixloc = namedtuple("pixloc", "x y")


class FrameBuffer:
    """ Wrapper for images to provide a window mapping and drawing primitives.
    This is a stripped down combination of elements from our Painter
    and Render2d projects 
    """

    def __init__(self, img, window):
        self.img = img
        self.size = img.size
        # viewport dimensions are 1 unit larger than pixel dimensions
        w, h = self.size[0] + 1, self.size[1] + 1
        l, b, r, t = window
        self.transform = [[w/(r-l), 0.0, (-.5*r-(w-.5)*l)/(r-l)],
                          [0.0, h/(t-b), (-.5*t-(h-.5)*b)/(t-b)],
                          [0.0, 0.0, 1.0]]

    def transpt(self, point):
        # Transform point from window (world) coordinates to pixel coordinates
        x, y, _ = mat.apply(self.transform, point+(1,))
        return pixloc(round(x), round(y))

    def draw_line(self, a, b, rgb):
        # pre: a and b are pixel locations with int components
        if a == b:   # handle degenerate case
            self.img[a] = rgb
            return
        # Otherwise, handle the general case
        dx = b.x - a.x
        dy = b.y - a.y
        if abs(dx) > abs(dy):  # x changes faster, walk it
            if a.x > b.x:
                a, b = b, a
            yinc = dy/dx
            y = a.y
            for x in range(a.x, b.x + 1):
                self.img[x, round(y)] = rgb
                y += yinc
        else:                  # y changes faster, walk it
            if a.y > b.y:
                a, b = b, a
            xinc = dx/dy
            x = a.x
            for y in range(a.y, b.y + 1):
                self.img[round(x), y] = rgb
                x += xinc

    def draw_polygon(self, points, color):
        # points are window points (floats)
        pixels = [self.transpt(p) for p in points]
        for i in range(len(pixels) - 1):
            self.draw_line(pixels[i], pixels[i+1], color)
        self.draw_line(pixels[-1], pixels[0], color)
