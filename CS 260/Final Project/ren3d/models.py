# models.py
#   Objects used for constructing scenes


from math import sin, cos, pi, sqrt, tau
from ren3d.math3d import Point, Vector
from ren3d.materials import make_material
import ren3d.matrix as mat
import ren3d.trans3d as trans3d


# Surfaces for Scene Modeling
# ----------------------------------------------------------------------
class Box:

    def __init__(self, pos=(0.0, 0.0, 0.0), size=(1, 1, 1),
                 color=(0, 0, 0), texture=None):
        planes = [(pos[i]-size[i]/2, pos[i]+size[i]/2) for i in range(3)]
        self.planes = planes
        self.color = make_material(color)
        self.texture = texture
                                      
    def iter_polygons(self):
        ijseq = [(0, 0), (1, 0), (1, 1), (0, 1)]
        xs, ys, zs = self.planes
        yield Record(points=[Point((xs[0], ys[i], zs[j])) for i, j in ijseq],
                     normals=[Vector((-1, 0, 0))]*4, color=self.color)
        yield Record(points=[Point((xs[1], ys[i], zs[j])) for i, j in ijseq],
                     normals=[Vector((1, 0, 0))]*4, color=self.color)
        yield Record(points=[Point((xs[i], ys[0], zs[j])) for i, j in ijseq],
                     normals=[Vector((0, -1, 0))]*4, color=self.color)
        yield Record(points=[Point((xs[i], ys[1], zs[j])) for i, j in ijseq],
                     normals=[Vector((0, 1, 0))]*4, color=self.color)
        yield Record(points=[Point((xs[i], ys[j], zs[0])) for i, j in ijseq],
                     normals=[Vector((0, 0, -1))]*4, color=self.color)
        yield Record(points=[Point((xs[i], ys[j], zs[1])) for i, j in ijseq],
                     normals=[Vector((0, 0, 1))]*4, color=self.color)

    def intersect(self, ray, interval, info):
        s, d = ray.start, ray.dir
        planes = self.planes
        hit = False
        for axis in range(3):
            if d[axis] == 0.0:
                continue
            for lh in range(2):
                t = (planes[axis][lh] - s[axis])/d[axis]
                if t not in interval:
                    continue
                p = ray.point_at(t)
                if self._inrect(p, axis):
                    hit = True
                    interval.high = t
                    info.t = t
                    info.object = self
                    info.point = p
                    info.normal = Vector([0]*3)
                    info.normal[axis] = (-1.0, 1.0)[lh]
                    info.color = self.color
                    info.texture = self.texture
                    if self.texture:
                        info.textcoords = self.generic_coords(p)
        return hit

    def generic_coords(self, p):
        uvn = [2*(p[a]-self.planes[a][0])/(self.planes[a][1]-self.planes[a][0]) - 1
               for a in [0, 1, 2]]
        return uvn

    def _inrect(self, p, axis):
        axes = [0, 1, 2]
        axes.remove(axis)
        for a in axes:
            low, high = self.planes[a]
            if not low <= p[a] <= high:
                return False
        return True


class Sphere:
    """ Model of a sphere shape
    """

    def __init__(self, pos=(0, 0, 0), radius=1,
                 color=(0, 1, 0), texture=None, nlat=15, nlong=15):
        """ create a sphere
        """
        self.pos = Point(pos)
        self.radius = radius
        self.color = make_material(color)
        self.nlat = nlat
        self.nlong = nlong
        self._make_bands(nlat, nlong)
        axis = Vector((0, radius, 0))
        self.northpole = self.pos + axis
        self.southpole = self.pos - axis
        self.texture = texture
        cx, cy, cz = pos

    def _make_bands(self, nlat, nlong):
        # helper method that creates a list of "bands" where each band consists
        #  of a list of points encircling the sphere at a latitude. There
        #  are nlat evenly (angularly) spaced bands each with nlong points
        #  evenly spaced around the band.

        def circle2d(c, r, n):
            cx, cy = c
            dt = tau/n
            points = [(r*cos(i*dt)+cx, r*sin(i*dt)+cy) for i in range(n)]
            points.append(points[0])  # complete the loop back to first
            return points

        cx, cy, cz = self.pos
        bands = []
        theta = pi/2
        dtheta = -pi/(nlat+1)
        for i in range(nlat):
            theta += dtheta
            r = self.radius*cos(theta)
            y = self.radius*sin(theta) + cy
            band = [Point((x, y, z))
                    for x, z in circle2d((cx, cz), r, nlong)]
            bands.append(band)
        self.bands = bands

    def iter_polygons(self):
        bands = self.bands
        # arctic
        b = bands[0]
        for i in range(self.nlong):
            points = (self.northpole, b[i], b[i+1])
            yield Record(points=points, color=self.color,
                         normals=[self.normal_at(p) for p in points])
        # inter-latitudes
        for b in range(len(bands)-1):
            b0 = bands[b]
            b1 = bands[b+1]
            for i in range(self.nlong):
                quad = b0[i], b1[i], b1[i+1], b0[i+1]
                yield Record(points=quad, color=self.color,
                             normals=[self.normal_at(p) for p in quad])
        # antarctic
        b = bands[-1]
        for i in range(self.nlong):
            points = (self.southpole, b[i+1], b[i])
            yield Record(points=points, color=self.color,
                         normals=[self.normal_at(p) for p in points])

    def normal_at(self, pt):
        n = (pt-self.pos)
        n.normalize()
        return n

    def generic_coords(self, p):
        return [(p[a]-self.pos[a]+self.radius)/self.radius - 1
                for a in [0, 1, 2]]
       
    def intersect(self, ray, interval, info):
        """ returns a True iff ray intersects the sphere within the

        given time interval. The approriate intersection information
        is recorded into info, which is a Record containing:
          point: the point of intersection
          t: the time of the intersection
          normal: the surface normal at the point
          color: the color at the point.
        """

        dir = ray.dir
        r = self.radius
        s_p = ray.start-self.pos

        a = dir.mag2()
        b = 2 * dir.dot(s_p)
        c = s_p.mag2() - r*r
        discrim = b*b - 4 * a * c
        if discrim <= 0:
            return False

        discrt = sqrt(discrim)
        t = (-b - discrt)/(2*a)
        if t in interval:
            self._setinfo(ray, t, info)
            return True
        elif t < interval.low:
            t = (-b + discrt)/(2*a)
            if t in interval:
                self._setinfo(ray, t, info)
                return True
        return False

    def _setinfo(self, ray, t, info):
        # helper method to fill in the info record
        p = ray.point_at(t)
        info.color = self.color
        info.point = p
        info.t = t
        info.normal = self.normal_at(p)
        info.texture = self.texture
        if self.texture:
            info.textcoords = self.generic_coords(p)

            
class Transformable:

    def __init__(self, surface):
        self.surface = surface
        self.trans = mat.unit(4)
        self.itrans = mat.unit(4)
        self.ntrans = mat.unit(4)
 
    def _update(self, trans, itrans):
        self.trans = mat.mul(trans, self.trans)
        self.itrans = mat.mul(self.itrans, itrans)
        self.ntrans = mat.transpose(self.itrans)

    def scale(self, sx, sy, sz):
        trans = trans3d.scale(sx, sy, sz)
        itrans = trans3d.scale(1/sx, 1/sy, 1/sz)
        self._update(trans, itrans)
        return self

    def translate(self, dx, dy, dz):
        trans = trans3d.translate(dx, dy, dz)
        itrans = trans3d.translate(-dx, -dy, -dz)
        self._update(trans, itrans)
        return self

    def rotate_x(self, angle):
        trans = trans3d.rotate_x(angle)
        itrans = trans3d.rotate_x(-angle)
        self._update(trans, itrans)
        return self
       
    def rotate_y(self, angle):
        trans = trans3d.rotate_y(angle)
        itrans = trans3d.rotate_y(-angle)
        self._update(trans, itrans)
        return self

    def rotate_z(self, angle):
        trans = trans3d.rotate_z(angle)
        itrans = trans3d.rotate_z(-angle)
        self._update(trans, itrans)
        return self

    def iter_polygons(self):
        for poly in self.surface.iter_polygons():
            transpoints = [p.transform(self.trans) for p in poly.points]
            poly.points = transpoints
            normals = [n.transform(self.ntrans) for n in poly.normals]
            poly.normals = normals
            yield poly

    def intersect(self, ray, interval, info):
        iray = ray.transform(self.itrans)
        hit = self.surface.intersect(iray, interval, info)
        if hit:
            info.point = info.point.transform(self.trans)
            info.normal = info.normal.transform(self.ntrans)
            info.normal.normalize()
        return hit


class Square:

    def __init__(self, color=(.8, .2, .2), texture=None):
        self.color = make_material(color)
        self.points = [Point([-.5, 0., -.5]), Point([-.5, 0., .5]),
                       Point([.5, 0., .5]), Point([.5, 0., -.5])]
        self.normal = Vector([0., 1., 0.])
        self.texture = texture

    def iter_polygons(self):
        r = Record()
        r.points = list(self.points)
        r.normals = [self.normal] * 4
        r.color = self.color
        yield r

    def intersect(self, ray, interval, info):
        dy = ray.dir.y
        if dy == 0.:
            return False
        t = -ray.start.y/dy
        if t not in interval:
            return False
        p = ray.point_at(t)
        hit = (-.5 <= p.x <= .5) and (-.5 <= p.z <= .5)
        if hit:
            info.t = t
            info.point = p
            info.color = self.color
            info.normal = self.normal
            info.texture = self.texture
            info.textcoords = (2*p.x, 0, 2*p.z)
        return hit


class Group:
    """ Model comprised of a group of other models.
    The contained models may be primitives (such as Sphere) or other groups.
    """

    def __init__(self):
        self.objects = []

    def add(self, model):
        """Add model to the group
        """
        self.objects.append(model)

    def iter_polygons(self):
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
                interval.high = info.t
                hit = True
        return hit


# ----------------------------------------------------------------------
class Record:
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
