# grayscale.py
# By Ryan Neubauer
# Color grayscaling for ppm file

import sys

from image import Image

def sunset(img, animate=False):
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b = img[x, y]
            img[x, y] = (int(round(r*0.299)), int(round(g*0.587)), int(round(b*0.114)))
        if animate:
            img.show()


def main():

    if len(sys.argv) != 3:
        print("Usage: python invert.py oldppm newppm")
        sys.exit()

    in_image = sys.argv[1]
    out_image = sys.argv[2]

    im = Image(in_image)
    sunset(im)
    im.save(out_image)


if __name__ == "__main__":
    main()
