# mesh.py
#    tools for handling meshes from OFF files.

from ren3d.math3d import Point, Vector
from ren3d.bbox import BoundingBox
from ren3d.materials import make_material
from ren3d.models import Group, Record

class Triangle:

    def __init__(self, points, color=(0, 1, 0), normals=[]):
        self.points = [Point(p) for p in points]
        self.color = make_material(color)
        if normals:
            self.normals = [Vector(n).normalized() for n in normals]
        else:
            a, b, c = self.points
            normal = (b-a).cross(c-a)
            normal.normalize()
            self.normals = [Vector(normal)] * 3
        self.bbox = BoundingBox()
        self.bbox.include_points(self.points)

    def __repr__(self):
        return "Triangle({}, {})".format(self.points, self.normals)

    def iter_polygons(self):
        yield Record(points=self.points,
                     color=self.color, normals=self.normals)

    def intersect(self, ray, interval, info):
        if not self.bbox.hit(ray, interval):
            return False
        p0, p1, p2 = self.points
        a, b, c = p0 - p1
        d, e, f = p0 - p2
        g, h, i = ray.dir

        ei_hf = e*i - h*f
        gf_di = g*f - d*i
        dh_eg = d*h - e*g

        den = a*ei_hf + b*gf_di + c*dh_eg
        if den == 0:
            return False

        j, k, l = p0 - ray.start
        bl_kc = b*l - k*c
        jc_al = j*c - a*l
        ak_jb = a*k - j*b

        t = -(d*bl_kc + e*jc_al + f*ak_jb) / den
        if t not in interval:
            return False

        beta = (j*ei_hf + k*gf_di + l*dh_eg) / den
        if beta < 0 or beta > 1:
            return False

        gamma = (g*bl_kc + h*jc_al + i*ak_jb) / den
        if gamma < 0 or gamma + beta > 1:
            return False

        info.t = t
        info.point = ray.point_at(t)
        info.color = self.color
        n0, n1, n2 = self.normals
        info.normal = (1 - beta - gamma)*n0 + beta*n1 + gamma*n2
        info.normal.normalize()

        return True


class Mesh:

    def __init__(self, fname, color, recenter=False, smooth=False):
        meshdata = OFFData(fname)
        if recenter:
            meshdata.recenter()

        group = Group()
        for tri in _make_mesh_triangles(meshdata, color, smooth):
            group.add(tri)
        self.group = group
        self.bbox = meshdata.bbox

    def iter_polygons(self):
        return self.group.iter_polygons()

    def intersect(self, ray, interval, info):
        if not self.bbox.hit(ray, interval):
            return False
        return self.group.intersect(ray, interval, info)


def _make_mesh_triangles(data, color, smooth):
    """ yield Triangle objects for all faces of mesh in data"""
    color = make_material(color)
    for face in data.face_indexes:
        points = data.get_points(face)
        if smooth:
            normals = data.get_vertex_normals(face)
        else:
            normals = [data.get_face_normal(face)]*len(points)
        for i in range(len(points)-1):
            tri = Triangle([points[0], points[i], points[i+1]],
                           color,
                           [normals[0], normals[i], normals[i+1]])
            yield tri


class OFFData:
    """Class for reading OFF files and supplying face information"""

    def __init__(self, fname):
        points, faces = self._readOFF("meshes/"+fname)
        self.points = points
        self.faces = faces
        self.face_indexes = range(len(faces))
        self.bbox = self._make_bbox()
        self._f_norms = [self._compute_face_normal(f) for f in faces]
        self._v_norms = [self._compute_vertex_normal(i)
                         for i in range(len(self.points))]

    def _readOFF(self, fname):
        # Read data from OFF file, return vertices and facelists
        with open(fname) as infile:
            heading = infile.readline()
            if heading[:3] != "OFF":
                raise ValueError("File does not appear to be an OFF")
            nVerts, nFaces, nEdges = [int(v) for v in infile.readline().split()]

            verts = []
            for i in range(nVerts):
                line = infile.readline()
                verts.append(Point(float(s) for s in line.split()[:3]))  # ignore rgba
                faces = []
            for i in range(nFaces):
                indexStrings = infile.readline().split()[1:]
                faces.append(tuple(int(s) for s in indexStrings))
        return verts, faces

    def _make_bbox(self):
        box = BoundingBox()
        box.include_points(self.points)
        return box

    def _compute_face_normal(self, f):
        a, b, c = [self.points[i] for i in f[:3]]
        norm = (b-a).cross(c-a)
        norm.normalize()
        return norm

    def _compute_vertex_normal(self, vert_i):
        n = Vector([0, 0, 0])
        for face_i, face in enumerate(self.faces):
            if vert_i in face:
                n += self._f_norms[face_i]
        try:
            n.normalize()
        except ZeroDivisionError:
            pass
        return n

    def get_points(self, face):
        return [self.points[i] for i in self.faces[face]]

    def get_face_normal(self, face):
        return self._f_norms[face]

    def get_vertex_normals(self, face):
        return [self._v_norms[i] for i in self.faces[face]]

    def recenter(self):
        dist = Vector(self.bbox.midpoint)
        self.points = [vert-dist for vert in self.points]
        self.bbox = self._make_bbox()
