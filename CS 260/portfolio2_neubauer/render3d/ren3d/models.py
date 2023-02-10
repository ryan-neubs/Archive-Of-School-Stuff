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
        def circle2d(c, r, n):
            cx, cy = c
            dt = tau/n
            points = [(r * cos(i * dt) + cx, r * sin(i * dt) + cy) for i in range(n)]
            return points
        cx, cy, cz = self.pos
        bands = []
        theta = pi/2
        dtheta = pi/(nlat+1)
        for i in range(nlat):
            theta += dtheta
            r = self.radius * cos(theta)
            y = self.radius * sin(theta) + cy
            band = [Point((x,y,z)) for x,z in circle2d((cx, cz), r, nlong)] 
            bands.append(band)
        self.bands = bands

    def iter_polygons(self):
        """produces a sequence of polygons on the skin of the sphere.

        Each polygon is a Record with fields "points" (a list of three points)
        and color (the color of the polygon).
        """
        bands = self.bands
        # Northpole Triangles
        b0 = bands[0]
        for i in range(len(b0)-1):
            points = [self.northpole, b0[i], b0[i + 1]]
            yield Record(points = points, color = self.color)
        # Quadrilaterals
        for i in range(len(bands) - 1):
            b0 = bands[i]
            b1 = bands[i + 1]
            for j in range(len(b0)-1):
                points = [b0[j], b1[j], b1[j+1], b0[j + 1]]
                yield Record(points = points, color = self.color)
        # Southpole Triangles
        b1 = bands[-1]
        for i in range(len(b1)-1):
            b1 = bands[-1]
            points = [self.southpole, b1[i], b1[i+1]]
            yield Record(points = points, color = self.color)
        
    def intersect(self, ray, interval, info):
        """ returns a True iff ray intersects the sphere within the

        given time interval. The approriate intersection information
        is recorded into info, which is a Record containing:
          point: the point of intersection
          t: the time of the intersection
          normal: the surface normal at the point
          color: the color at the point.
        """
        a = ray.dir.mag2()
        b = (2 * ray.dir).dot(ray.start - self.pos)
        c = (ray.start - self.pos).mag2() - self.radius ** 2
        if (b**2 - (4 * a * c)) < 0:
            return False
        t = (-b - sqrt(b**2 - 4 * a * c))/(2*a)
        if t in interval:
            self._setinfo(ray, t, info)
            return True


    def _setinfo(self, ray, t, info):
        """ helper method to fill in the info record """
        info.point = ray.point_at(t)
        info.t = t
        info.normal = (info.point - self.pos).normalized()
        info.color = self.color

class Box:

    def __init__(self, size, pos, color):
        self.pos = Point(pos)
        self.size = size
        self.color = RGB(color)
        xlow, xhigh = self.pos[0] - self.size[0]/2, self.pos[0] + self.size[0]/2
        ylow, yhigh = self.pos[1] - self.size[1]/2, self.pos[1] + self.size[1]/2
        zlow, zhigh = self.pos[2] - self.size[2]/2, self.pos[2] + self.size[2]/2
        self.planes = [(xlow, xhigh), (ylow, yhigh), (zlow, zhigh)]

    def iter_polygons(self):
        xs, ys, zs = self.planes
        #left
        yield Record(points=[Point((xs[0], ys[0], zs[0])), Point((xs[0], ys[0], zs[1])), Point((xs[0], ys[1], zs[1])), Point((xs[0], ys[1], zs[0]))], color = self.color)
        #top
        yield Record(points=[Point((xs[0], ys[1], zs[0])), Point((xs[0], ys[1], zs[1])), Point((xs[1], ys[1], zs[1])), Point((xs[1], ys[1], zs[0]))], color = self.color)
        #right
        yield Record(points=[Point((xs[1], ys[1], zs[0])), Point((xs[1], ys[1], zs[1])), Point((xs[1], ys[0], zs[1])), Point((xs[1], ys[0], zs[0]))], color = self.color)
        #bottom
        yield Record(points=[Point((xs[1], ys[0], zs[0])), Point((xs[0], ys[0], zs[0])), Point((xs[0], ys[0], zs[1])), Point((xs[1], ys[0], zs[1]))], color = self.color)
        #front
        yield Record(points=[Point((xs[0], ys[1], zs[0])), Point((xs[1], ys[1], zs[0])), Point((xs[1], ys[0], zs[0])), Point((xs[0], ys[0], zs[0]))], color = self.color)
        #back
        yield Record(points=[Point((xs[1], ys[0], zs[1])), Point((xs[1], ys[1], zs[1])), Point((xs[0], ys[1], zs[1])), Point((xs[0], ys[0], zs[1]))], color = self.color)

    def intersect(self, ray, interval, info):
        def _inrect(p, axis):
            for a in range(3):
                if a == axis:
                    continue
                low, high = self.planes[a]
                if not low <= p[a] <= high:
                    return False
            return True
        s = ray.start
        d = ray.dir
        planes = self.planes
        hit = False
        for a in range(3):
            if d[a] == 0.0:
                continue
            for lh in range(2):
                t = (planes[a][lh] - s[a])/d[a]
                if t not in interval:
                    continue
                p = ray.point_at(t)
                if _inrect(p, a):
                    hit = True
                    interval.high = t
                    info.t = t
                    info.normal = Vector((0, 0, 0))
                    info.normal[a] = (-1.0, 1.0)[lh]
                    info.color = self.color
        return hit
    

    def _setinfo(self, ray, t, info):
        info.point = ray.point_at(t)
        info.t = t
        info.normal = (info.point - self.pos).normalized()
        info.color = self.color

class Group:
    """ Model comprised of a group of other models.
    The contained models may be primitives (such as Sphere) or other groups.
    """

    def __init__(self):
        self.objects = []

    def add(self, model):
        """ Add model to the group
        """
        self.objects.append(model)

    def iter_polygons(self):
        """ Produce all polygons in the group
        """
        for obj in self.objects:
            for poly in obj.iter_polygons():
                yield poly

    def intersect(self, ray, interval, info):
        """Returns True iff ray intersects some object in the group

        If so, info is the record of the first (in time) object hit, and
        interval.max is set to the time of the first hit.
        """
        hit = False
        for obj in self.objects:
            if obj.intersect(ray, interval, info):
                hit = True
                interval.high = info.t
        return hit


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
