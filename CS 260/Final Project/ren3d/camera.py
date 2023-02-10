# camera.py
#    Implementation of simple camera for describing views

from math import tan, radians
from ren3d.math3d import Point, Vector
from ren3d.ray3d import Ray
from ren3d.trans3d import to_uvn
import ren3d.matrix as mat


class Camera:
    """Camera is used to specify the view of the scene.
    """

    def __init__(self):
        self.eye = Point([0, 0, 0])
        self.window = -10.0, -10.0, 10.0, 10.0
        self.distance = 10
        self.u = Vector([1, 0, 0])
        self.v = Vector([0, 1, 0])
        self.n = Vector([0, 0, 1])
        self.trans = mat.unit(4)

    def set_view(self, eye, lookat, up=(0, 1, 0)):
        self.eye = eye = Point(eye)
        n = self.n = (eye-Point(lookat)).normalized()
        u = self.u = (Vector(up).cross(self.n)).normalized()
        v = self.v = self.n.cross(u).normalized()
        self.trans = to_uvn(u, v, n, eye)

    def set_perspective(self, hfov, aspect, distance):
        """ Set up perspective view
        hfov is horizontal field of view (in degrees)
        aspect is the aspect ratio horizontal/vertical
        distance is distance from eye to focal plane.

        >>> c = Camera()
        >>> c.set_perspective(60, 1.333, 20)
        >>> c.eye
        Point([0.0, 0.0, 0.0])
        >>> c.distance
        20
        >>> c.window
        (-11.547005383792515, -8.662419642755076, 11.547005383792515, 8.662419642755076)
        """
        self.distance = distance
        hwidth = distance * tan(radians(hfov)/2)
        top = hwidth/aspect
        self.window = (-hwidth, -top, hwidth, top)

    # ------------------------------------------------------------
    # These methods used for ray tracing

    def set_resolution(self, width, height):
        """ Set resolution of pixel sampling across the window.
        """
        l, b, r, t = self.window
        self.dx = (r-l)/width
        self.dy = (t-b)/height

    def ij_ray(self, i, j):
        """ return the ray from the eye through the ijth pixel.

        >>> c = Camera()
        >>> c.set_resolution(400, 300)
        >>> c.ij_ray(-0.5, -0.5)
        Ray(Point([0.0, 0.0, 0.0]), Vector([-10.0, -10.0, -10.0]))
        >>> c.ij_ray(399.5, 299.5)
        Ray(Point([0.0, 0.0, 0.0]), Vector([10.0, 10.0, -10.0]))
        >>> c.ij_ray(0, 0)
        Ray(Point([0.0, 0.0, 0.0]), Vector([-9.975, -9.966666666666667, -10.0]))
        >>> c.ij_ray(399/2, 299/2)
        Ray(Point([0.0, 0.0, 0.0]), Vector([0.0, 0.0, -10.0]))
        >>>

        """
        l, b, r, t = self.window
        x = l + (i+0.5)*self.dx
        y = b + (j+0.5)*self.dy
        z = -self.distance
        raydir = x*self.u + y*self.v + z*self.n
        return Ray(self.eye, raydir)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
