# models.py
#   Objects used for constructing scenes

from math import sin, cos, pi, sqrt, tau
from ren3d.math3d import Point, Vector
from ren3d.rgb import RGB

# Surfaces for Scene Modeling
# ----------------------------------------------------------------------


class Sphere:
    """ Model of a sphere shape
    """

    def __init__(self, pos=(0, 0, 0), radius=1,
                 color=(0, 1, 0), nlat=7, nlong=15):
        """ create a sphere
        """
        self.pos = Point(pos)
        self.radius = radius
        self.color = RGB(color)
        self.nlat = nlat
        self.nlong = nlong
        self._make_bands(nlat, nlong)
        axis = Vector((0, radius, 0))
        self.northpole = self.pos + axis
        self.southpole = self.pos - axis

    def _make_bands(self, nlat, nlong):
        """helper method that creates a list of "bands"

        each band consists of a list of points encircling the sphere
        at a latitude. There are nlat evenly (angularly) spaced
        bands each with nlong points evenly spaced around the band.

        """
        
    def iter_triangles(self):
        """produces a sequence of triangles on the skin of the sphere.

        Each triangle is a Record with fields "points" (a list of three points)
        and color (the color of the triangle).
        """
        
    def intersect(self, ray, interval, info):
        """ returns a True iff ray intersects the sphere within the

        given time interval. The approriate intersection information
        is recorded into info, which is a Record containing:
          point: the point of intersection
          t: the time of the intersection
          normal: the surface normal at the point
          color: the color at the point.
        """

    def _setinfo(self, ray, t, info):
        """ helper method to fill in the info record """


class Group:
    """ Model comprised of a group of other models.
    The contained models may be primitives (such as Sphere) or other groups.
    """

    def __init__(self):
        self.objects = []

    def add(self, model):
        """ Add model to the group
        """

    def iter_triangles(self):
        """ Produce all triangles in the group
        """

    def intersect(self, ray, interval, info):
        """Returns True iff ray intersects some object in the group

        If so, info is the record of the first (in time) object hit, and
        interval.max is set to the time of the first hit.
        """


# ----------------------------------------------------------------------
class Record(object):
    """ conveience for bundling a bunch of info together. Basically
    a dictionary that can use dot notatation

    >>> info = Record()
    >>> info.point = Point([1,2,3])
    >>> info
    Record(point=Point([1.0, 2.0, 3.0]))
    >>> info.t = 3.245
    >>> info
    Record(point=Point([1.0, 2.0, 3.0]), t=3.245)
    >>> info.update(point=Point([-1,0,0]), t=5)
    >>> info.t
    5
    >>> info
    Record(point=Point([-1.0, 0.0, 0.0]), t=5)
    >>> info2 = Record(whatever=53, whereever="Iowa")
    >>> info2.whereever
    'Iowa'
    >>> 
    """

    def __init__(self, **items):
        self.__dict__.update(items)

    def update(self, **items):
        self.__dict__.update(**items)

    def __repr__(self):
        d = self.__dict__
        fields = [k+"="+str(d[k]) for k in sorted(d)]
        return "Record({})".format(", ".join(fields))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
