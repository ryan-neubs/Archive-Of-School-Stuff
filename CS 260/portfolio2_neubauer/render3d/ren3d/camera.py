# camera.py
#    Implementation of simple camera for describing views

from math import tan, radians
from ren3d.math3d import Point
from ren3d.ray3d import Ray


class Camera:
    """Camera is used to specify the view of the scene.
    """

    def __init__(self):
        self.eye = Point([0, 0, 0])
        self.window = -10.0, -10.0, 10.0, 10.0
        self.distance = 10
        self.dx = 0
        self.dy = 0

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
        w2 = tan(radians(hfov/2)) * distance
        h2 = w2/aspect
        self.window = (-w2, -h2, w2, h2)

        


    # ------------------------------------------------------------
    # These methods used for ray tracing

    def set_resolution(self, width, height):
        """ Set resolution of pixel sampling across the window.
        """
        self.dx = (self.window[2] - self.window[0])/width
        self.dy = (self.window[3] - self.window[1])/height

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
        l,b,r,t = self.window
        z = -self.distance
        x = l + self.dx * (i + 0.5)
        y = b + self.dy * (j + 0.5)
        return Ray(self.eye, Point((x,y,z)) - self.eye)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
