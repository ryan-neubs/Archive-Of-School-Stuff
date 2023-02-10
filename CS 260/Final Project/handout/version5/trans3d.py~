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

    return [[1., 0., 0., float(dx)],
            [0., 1., 0., float(dy)],
            [0., 0., 1., float(dz)],
            [0., 0., 0., 1.]]


def scale(sx=1., sy=1., sz=1.):
    """ returns matrix that scales by 

    >>> scale(2,3,4)
    [[2.0, 0.0, 0.0, 0.0], [0.0, 3.0, 0.0, 0.0], [0.0, 0.0, 4.0, 0.0], [0.0, 0.0, 0.0, 1.0]]
    >>> 
    """
    return [[float(sx), 0., 0., 0.],
            [0., float(sy), 0., 0.],
            [0., 0., float(sz), 0.],
            [0., 0., 0., 1.]
            ]


def rotate_x(angle):
    """ returns matrix that rotates angle degrees about X axis

    >>> rotate_x(30)
    [[1.0, 0.0, 0.0, 0.0], [0.0, 0.8660254037844387, -0.49999999999999994, 0.0], [0.0, 0.49999999999999994, 0.8660254037844387, 0.0], [0.0, 0.0, 0.0, 1.0]]
    """

    m = mat.unit(4)
    theta = radians(angle)
    m[1][1] = cos(theta)
    m[1][2] = -sin(theta)
    m[2][1] = sin(theta)
    m[2][2] = cos(theta)
    return m


def rotate_y(angle):
    """ returns matrix that rotates by angle degrees around the Y axis

    >>> rotate_y(30)
    [[0.8660254037844387, 0.0, 0.49999999999999994, 0.0], [0.0, 1.0, 0.0, 0.0], [-0.49999999999999994, 0.0, 0.8660254037844387, 0.0], [0.0, 0.0, 0.0, 1.0]]
    """

    m = mat.unit(4)
    theta = radians(angle)
    m[0][0] = cos(theta)
    m[0][2] = sin(theta)
    m[2][0] = -sin(theta)
    m[2][2] = cos(theta)
    return m


def rotate_z(angle):
    """returns a matrix that rotates by angle degrees around Z axis

    >>> rotate_z(30)
    [[0.8660254037844387, -0.49999999999999994, 0.0, 0.0], [0.49999999999999994, 0.8660254037844387, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]
    """
    m = mat.unit(4)
    theta = radians(angle)
    m[0][0] = cos(theta)
    m[0][1] = -sin(theta)
    m[1][0] = sin(theta)
    m[1][1] = cos(theta)
    return m


def to_uvn(u, v, n, eye):
    """returns a matrix that transforms a point to UVN coordinates

    >>> to_uvn(Vector([1.0, 2.0, 3.0]), Vector([4.0, 5.0, 6.0]), Vector([7.0, 8.0, 9.0]), Vector([10.0, 11.0, 12.0]))
    [[1.0, 2.0, 3.0, -68.0], [4.0, 5.0, 6.0, -167.0], [7.0, 8.0, 9.0, -266.0], [0, 0, 0, 1]]
    """
    evec = Point((0, 0, 0))-eye
    return [list(u)+[u.dot(evec)],
            list(v)+[v.dot(evec)],
            list(n)+[n.dot(evec)],
            [0, 0, 0, 1]]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
