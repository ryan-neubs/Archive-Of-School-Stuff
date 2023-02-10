# sierpinski.py
#  by John Zelle

"""
Fractal dust drawing of Sierpinski triangle as an illustration of using
the Image class for computer graphics.
"""

import sys
import random
import time
from image import Image


ANIMATE = True
BACKGROUND = (255, 255, 255)  # white
COLOR = (0, 0, 0)  # black


def make_image(points, size):
    im = Image(size)
    im.clear(BACKGROUND)
    for p in points:
        im[p] = COLOR
    return im


def number_of_points():
    # get number of points from command line or user
    try:
        n = int(sys.argv[1])
    except IndexError:
        n = int(input("How many points? "))
    return n


def draw_fractal_dust(image, triangle, n):
    pt = random.choice(triangle)
    for i in range(n):
        pt = midpoint(pt, random.choice(triangle))
        image[pt] = COLOR
        if ANIMATE and i % 1000 == 0:
            image.show()


def midpoint(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (intavg(x1, x2), intavg(y1, y2))


def intavg(a, b):
    return int(round(a+b)/2)


def main():
    triangle = [(50, 50), (250, 450), (450, 50)]
    img = make_image(triangle, (500, 500))

    # time drawing of  siepinski points
    n = number_of_points()
    start = time.time()
    draw_fractal_dust(img, triangle, n)
    stop = time.time()

    # report results
    img.show()
    print("Time: ", stop-start)
    img.save("triangle.ppm")
    input("Press Enter to quit")
    img.unshow()


if __name__ == "__main__":
    main()
