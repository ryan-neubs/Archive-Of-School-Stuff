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
        pass

    def __repr__(self):
        pass

    def iter_polygons(self):
        pass

    def intersect(self, ray, interval, info):
        pass


class Mesh:
    """model to implement polygonal mesh from OFF file

    Mesh is modeled as a group of triangles with a bounding box.
    """

    def __init__(self, fname, color, recenter=False, smooth=False):
        pass

    def iter_polygons(self):
        pass

    def intersect(self, ray, interval, info):
        pass
   
def _make_triangles(facepoints, facenormals, color):
    """helper function to turn a face into tiangles

    facepoints is list of points and facenormals is a corresponding
    list of normals. color is a material
    """

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

