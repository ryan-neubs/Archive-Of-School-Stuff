# file: sunset.py
# by: John Zelle

"""
Simple image filter program applies a sunset effect
"""

import sys

from image import Image


def sunset(img, animate=False):
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b = img[x, y]
            img[x, y] = (r, int(round(.7*g)), int(round(.7*b)))
        if animate:
            img.show()


def main():

    if len(sys.argv) != 3:
        print("Usage: python sunset.py oldppm newppm")
        sys.exit()

    in_image = sys.argv[1]
    out_image = sys.argv[2]

    im = Image(in_image)
    sunset(im)
    im.save(out_image)


if __name__ == "__main__":
    main()
