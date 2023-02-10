# trans2d.py
#    implementation of 2d transformations in homogeneous coords


from math import radians, sin, cos, tan
import matrix as mat


def scale(sx, sy):
    """ return a matrix that scales by sx, sy.

    >>> scale(2,3)
    [[2.0, 0.0, 0.0], [0.0, 3.0, 0.0], [0.0, 0.0, 1.0]]
    >>> 
    """
    m = mat.unit(3)
    m[0][0] = float(sx)
    m[1][1] = float(sy)
    return m

def translate(dx, dy):
    """return a matrix that translates by (dx, dy)

    >>> translate(-3, 2)
    [[1.0, 0.0, -3.0], [0.0, 1.0, 2.0], [0.0, 0.0, 1.0]]
    """
    m = mat.unit(3)
    m[0][2] = float(dx)
    m[1][2] = float(dy)
    return m

def rotate(angle):
    """returns a matrix that rotates angle degrees counter-clockwise

    >>> print(rotate(30))
    [[0.8660254037844387, -0.49999999999999994, 0.0], [0.49999999999999994, 0.8660254037844387, 0.0], [0.0, 0.0, 1.0]]
    """
    angle = radians(angle)
    m = mat.unit(3)
    m[0][0], m[1][1] = cos(angle), cos(angle)
    m[0][1], m[1][0] = -sin(angle), sin(angle)
    return m

    
def window(box0, box1):
    """returns a transformation that maps box0 to box1

    note: a box is a tuple: (left, bottom, right, top) where
    (left,bottom) is the point at the lower-left corner and
    (right, top) is the point in the upper-right corner.

    >>> window((20, 10, 60,40), (5, 5, 9, 8))
    [[0.1, 0.0, 3.0], [0.0, 0.1, 4.0], [0.0, 0.0, 1.0]]
    >>> m=window((20, 10, 60,40), (5, 5, 9, 8))
    >>> mat.apply(m, (20,10,1))
    [5.0, 5.0, 1.0]
    >>> mat.apply(m, (60,40,1))
    [9.0, 8.0, 1.0]
    >>> mat.apply(m, (40,25,1))
    [7.0, 6.5, 1.0]

    """
    m = translate(-box0[0], -box0[1])
    m = mat.mul(scale((box1[2] - box1[0]) / (box0[2] - box0[0]),
                      (box1[3] - box1[1]) / (box0[3] - box0[1])), m)
    m = mat.mul(translate(box1[0], box1[1]), m)
    return m


if __name__ == '__main__':
    import doctest
    doctest.testmod()
