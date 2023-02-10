# sphere.py
# by Ryan Neubauer

from math import *

class sphere:

    def __init__(self, radius):
        self.radius = radius
        self.sa = (pi * radius ** 2)
        self.v = ((4/3) * pi * radius ** 3)

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        return self.sa

    def volume(self):
        return self.v
        

