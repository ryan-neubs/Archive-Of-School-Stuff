# scenedef.py
#    A scene is a collection of modeling elements.
#    This file is the basic "header" needed to define scenes
# by: John Zelle


from ren3d.rgb import RGB
from ren3d.models import Box, Sphere, Group, Record
from ren3d.camera import Camera
from ren3d.math3d import Point
from ren3d.textures import *
from ren3d.materials import Material
from ren3d.mesh import Mesh
import ren3d.matrix as mat
import ren3d.trans3d as trans3d


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
        self.textures = False

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

class Transformable:
    """
        >>> s = Transformable(Sphere(color=(0, 0, 0)))
        >>> x = s.scale(2, 3, 4).rotate_y(30).translate(5, -3, 8)
        >>> s.trans[0]
        [1.7320508075688774, 0.0, 1.9999999999999998, 5.0]
        >>> s.trans[1]
        [0.0, 3.0, 0.0, -3.0]
        >>> s.trans[2]
        [-0.9999999999999999, 0.0, 3.464101615137755, 8.0]
        >>> s.trans[3]
        [0.0, 0.0, 0.0, 1.0]
        >>> s.itrans[0]
        [0.43301270189221935, 0.0, -0.24999999999999997, -0.16506350946109705]
        >>> s.itrans[1]
        [0.0, 0.3333333333333333, 0.0, 1.0]
        >>> s.itrans[2]
        [0.12499999999999999, 0.0, 0.21650635094610968, -2.357050807568877]
        >>> s.itrans[3]
        [0.0, 0.0, 0.0, 1.0]
        >>> s.ntrans[0]
        [0.43301270189221935, 0.0, 0.12499999999999999, 0.0]
        >>> s.ntrans[1]
        [0.0, 0.3333333333333333, 0.0, 0.0]
        >>> s.ntrans[2]
        [-0.24999999999999997, 0.0, 0.21650635094610968, 0.0]
        >>> s.ntrans[3]
        [-0.16506350946109705, 1.0, -2.357050807568877, 1.0]
        >>>
    """

    def __init__(self, obj):
        self.object = obj
        self.trans = mat.unit(4)
        self.itrans = mat.unit(4)

    def intersect(self, ray, interval, info):
        transRay = ray.trans(self.itrans)
        hit = False
        if self.object.intersect(transRay, interval, info):
            info.point = info.point.trans(self.trans)
            info.normal = info.normal.trans(self.ntrans).normalized()
            hit = True
        return hit

    def scale(self, sx, sy, sz):
        trans = trans3d.scale(sx, sy, sz)
        self.trans = mat.mul(trans, self.trans)
        itrans = trans3d.scale(1/sx, 1/sy, 1/sz)
        self.itrans = mat.mul(self.itrans, itrans)
        self.ntrans = mat.transpose(self.itrans)
        return self

    def translate(self, dx, dy, dz):
        trans = trans3d.translate(dx, dy, dz)
        self.trans = mat.mul(trans, self.trans)
        itrans = trans3d.translate(-dx, -dy, -dz)
        self.itrans = mat.mul(self.itrans, itrans)
        self.ntrans = mat.transpose(self.itrans)
        return self

    def rotate_x(self, angle):
        trans = trans3d.rotate_x(angle)
        self.trans = mat.mul(trans, self.trans)
        itrans = trans3d.rotate_x(-angle)
        self.itrans = mat.mul(self.itrans, itrans)
        self.ntrans = mat.transpose(self.itrans)
        return self

    def rotate_y(self, angle):
        trans = trans3d.rotate_y(angle)
        self.trans = mat.mul(trans, self.trans)
        itrans = trans3d.rotate_y(-angle)
        self.itrans = mat.mul(self.itrans, itrans)
        self.ntrans = mat.transpose(self.itrans)
        return self

    def rotate_z(self, angle):
        trans = trans3d.rotate_z(angle)
        self.trans = mat.mul(trans, self.trans)
        itrans = trans3d.rotate_z(-angle)
        self.itrans = mat.mul(self.itrans, itrans)
        self.ntrans = mat.transpose(self.itrans)
        return self

    def iter_polygons(self):
        for poly in self.object.iter_polygons():
            polygon = Record(points = [], color = poly.color)
            for p in poly.points:
                polygon.points.append(p.trans(self.trans))
            yield polygon

if __name__ == "__main__":
    import doctest
    doctest.testmod()