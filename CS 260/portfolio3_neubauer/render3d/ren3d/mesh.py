# mesh.py
#    tools for handling meshes from OFF files.
#    The main "export" is Mesh

from ren3d.math3d import Point, Vector
from ren3d.bbox import BoundingBox
from ren3d.materials import make_material
from ren3d.models import Group, Record


class Triangle:
    """Model for a triangle """

    def __init__(self, points, color=(0, 1, 0), normals=[]):
        self.points = [Point(p) for p in points]
        self.color = make_material(color)
        if not normals:
            normals = [Vector((0,0,1)) for i in range(3)]
        self.normals = [Vector(n).normalized() for n in normals]
        self.bbox = BoundingBox()
        self.bbox.include_points(points)

    def __repr__(self):
        return "Triangle({}, {})".format(self.points, self.normals)

    def iter_polygons(self):
        yield Record(points=self.points, color=self.color, normals=self.normals)

    def intersect(self, ray, interval, info):
        p0,p1,p2 = self.points
        a,b,c = p0-p1
        d,e,f = p0-p2
        g,h,i = ray.dir
        ei_hf = e*i-h*f
        gf_di = g*f-d*i
        dh_eg = d*h-e*g
        den = a*ei_hf + b*gf_di + c*dh_eg
        if den == 0.0:
            return False
        j,k,l = p0-ray.start
        t = -(d*(b*l-k*c) + e*(j*c-a*l) + f * (a * k-j*b))/den
        if t not in interval:
            return False
        beta = (j*ei_hf + k*gf_di + l*dh_eg)/den
        if beta < 0 or beta > 1:
            return False
        gamma = (g*(b*l-k*c) + h*(j*c-a*l) + i*(a*k-j*b))/den
        if gamma < 0 or (beta + gamma) > 1:
            return False
        alpha = 1-beta-gamma
        info.t = t
        info.point = ray.point_at(t)
        info.normal = (alpha*self.normals[0] + beta*self.normals[1] + gamma*self.normals[2]).normalized()
        info.color = self.color
        return True


class Mesh:
    """model to implement polygonal mesh from OFF file

    Mesh is modeled as a group of triangles with a bounding box.
    """

    def __init__(self, fname, color, recenter=False, smooth=False):
        self.meshdata = OFFData(fname)
        if recenter:
            self.meshdata.recenter()
        self.group = Group()
        self.bbox = self.meshdata.bbox
        self._make_tris(self.meshdata, smooth)

    def _make_tris(self, smooth, color):
        for i in self.meshdata.face_indexes:
            points = [self.meshdata.points[j] for j in self.meshdata.faces[i]]
            normals = self.meshdata.get_vertex_normals(i) if smooth else self.meshdata.get_face_normal(i)
            for tri in _make_triangles(points, normals, color):
                self.group.add(tri)

    def iter_polygons(self):
        return self.objects.iter_polygons()

    def intersect(self, ray, interval, info):
        return False if not self.bbox.hit(ray, interval) else self.group.intersect(ray, interval, info)
   
def _make_triangles(facepoints, facenormals, color):
    """helper function to turn a face into tiangles

    facepoints is list of points and facenormals is a corresponding
    list of normals. color is a material
    """
    tris = []
    if type(facenormals) != list:
        facenormals = [Vector(facenormals) for _ in range(len(facepoints))]

    for i in range(len(facepoints)-1):
        tris.append(Triangle([facepoints[0], facepoints[i], facepoints[i+1]],
        color,
        [facenormals[0], facenormals[i], facenormals[i+1]]))

    return tris

class OFFData:
    """Class for reading OFF files and supplying face information"""

    def __init__(self, fname):
        points, faces = self._readOFF("meshes/"+fname)
        self.points = points # List of points from the file
        self.faces = faces # List of faces from the file
        self.face_indexes = range(len(faces)) # 
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
                verts.append(Point(float(s) for s in line.split()[:3]))  # ignore rgb
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
        norm = (b-a).cross(c-a) # Crossing these will give the surface normal (vector pointing the way the surface is pointing)
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
        """returns a list of points for face; face is an index"""
        return [self.points[i] for i in self.faces[face]]

    def get_face_normal(self, face):
        """return normal for face; face is an index."""
        return self._f_norms[face]

    def get_vertex_normals(self, face):
        """return list of normals for a face; face is an index"""
        return [self._v_norms[i] for i in self.faces[face]]
       
    def recenter(self):
        """move points to put midpoint at (0, 0, 0)"""
        
        dist = Vector(self.bbox.midpoint)
        self.points = [vert-dist for vert in self.points]
        # rebuild the bounding box
        self.bbox = self._make_bbox()

