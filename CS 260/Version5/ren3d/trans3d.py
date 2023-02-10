# trans3d.py
"""matrices for performing 3D transformations in homogeneous coordinates"""

from math import radians, sin, cos, tan
from ren3d.math3d import Point, Vector
import ren3d.matrix as mat


def translate(dx=0., dy=0., dz=0.):
    """ returns matrix that translates by dx, dy, dz

    >>> translate(2,1,3)
    [[1.0, 0.0, 0.0, 2.0], [0.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 3.0], [0.0, 0.0, 0.0, 1.0]]
    """
    m = mat.unit(4)
    m[0][3] = float(dx)
    m[1][3] = float(dy)
    m[2][3] = float(dz)
    return m


def scale(sx=1., sy=1., sz=1.):
    """ returns matrix that scales by sx, sy, sz

    >>> scale(2,3,4)
    [[2.0, 0.0, 0.0, 0.0], [0.0, 3.0, 0.0, 0.0], [0.0, 0.0, 4.0, 0.0], [0.0, 0.0, 0.0, 1.0]]
    >>>
    """
    m = mat.unit(4)
    m[0][0] = float(sx)
    m[1][1] = float(sy)
    m[2][2] = float(sz)
    return m

def rotate_x(angle):
    """ returns matrix that rotates angle degrees about X axis

    >>> rotate_x(30)
    [[1.0, 0.0, 0.0, 0.0], [0.0, 0.8660254037844387, -0.49999999999999994, 0.0], [0.0, 0.49999999999999994, 0.8660254037844387, 0.0], [0.0, 0.0, 0.0, 1.0]]
    """
    m = mat.unit(4)
    angle = radians(angle)
    m[1][1], m[1][2] = cos(angle), -sin(angle)
    m[2][1], m[2][2] = sin(angle), cos(angle)
    return m

def rotate_y(angle):
    """ returns matrix that rotates by angle degrees around the Y axis

    >>> rotate_y(30)
    [[0.8660254037844387, 0.0, 0.49999999999999994, 0.0], [0.0, 1.0, 0.0, 0.0], [-0.49999999999999994, 0.0, 0.8660254037844387, 0.0], [0.0, 0.0, 0.0, 1.0]]
    """
    m = mat.unit(4)
    angle = radians(angle)
    m[0][0], m[0][2] = cos(angle), sin(angle)
    m[2][0], m[2][2] = -sin(angle), cos(angle)
    return m

def rotate_z(angle):
    """returns a matrix that rotates by angle degrees around Z axis

    >>> rotate_z(30)
    [[0.8660254037844387, -0.49999999999999994, 0.0, 0.0], [0.49999999999999994, 0.8660254037844387, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]
    """
    m = mat.unit(4)
    angle = radians(angle)
    m[0][0], m[0][1] = cos(angle), -sin(angle)
    m[1][0], m[1][1] = sin(angle), cos(angle)
    return m

def to_uvn(u, v, n, eye):
    """returns a matrix that transforms a point to UVN coordinates

    >>> to_uvn(Vector([1.0, 2.0, 3.0]), Vector([4.0, 5.0, 6.0]), Vector([7.0, 8.0, 9.0]), Vector([10.0, 11.0, 12.0]))
    [[1.0, 2.0, 3.0, -68.0], [4.0, 5.0, 6.0, -167.0], [7.0, 8.0, 9.0, -266.0], [0.0, 0.0, 0.0, 1.0]]
    """
    m = mat.unit(4)

    m[0][0], m[0][1], m[0][2] = u[0], u[1], u[2]
    m[1][0], m[1][1], m[1][2] = v[0], v[1], v[2]
    m[2][0], m[2][1], m[2][2] = n[0], n[1], n[2]

    m[0][3] = -u.dot(eye)
    m[1][3] = -v.dot(eye)
    m[2][3] = -n.dot(eye)

    return m

if __name__ == '__main__':
    import doctest
    doctest.testmod()
