# scenedef.py
#    A scene is a collection of modeling elements.
#    This file is the basic "header" needed to define scenes
# by: John Zelle


from ren3d.rgb import RGB
from ren3d.models import Box, Sphere, Group
from ren3d.camera import Camera
from ren3d.math3d import Point


# ----------------------------------------------------------------------
class Scene:

    def __init__(self):
        self.camera = Camera()
        self.objects = Group()
        self.background = (0, 0, 0)
        self.ambient = (.1, .1, .1)
        self.intersect = self.objects.intersect
        self.lights = [(Point((0, 0, 0)), RGB((1, 1, 1)))]
        self.shadows = False

    def add(self, object):
        self.objects.add(object)

    def set_light(self, pos, color):
        self.lights[0] = (Point(pos), RGB(color))

    def add_light(self, pos=(0,0,0), color=(1,1,1)):
        self.lights.append((Point(pos), RGB(color)))

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, color):
        self._background = RGB(color)

    @property
    def ambient(self):
        return self._ambient

    @ambient.setter
    def ambient(self, color):
        if type(color) == float:
            color = [color] * 3
        self._ambient = RGB(color)

# ----------------------------------------------------------------------
# global scene
#   for files that define a scene use: from scenedef import *


scene = Scene()
camera = scene.camera

# ----------------------------------------------------------------------
# use this function to load scene modules for rendering


def load_scene(modname):
    if modname.endswith(".py"):
        modname = modname[:-3]
    scene = __import__(modname).scene
    return scene, modname
