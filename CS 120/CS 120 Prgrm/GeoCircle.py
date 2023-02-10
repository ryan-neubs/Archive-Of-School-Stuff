# circle.py

from math import *

class GeomCircle:

    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        

    def get_circumference(self):
        diameter = self.radius * 2
        return pi * diameter

    def get_area(self):
        return pi * self.radius ** 2

    def move(self, dx, dy):
        self.center_x = self.center_x + dx
        self.center_y = self.center_y + dy

    def is_inside(self, px, py):
        dx = self.center_x - px
        dy = self.center_y = py
        return dx * dx + dy * dy <= self.radius * self.radius
