# rgb.py
#    Calculations on color values

# ----------------------------------------------------------------------


class RGB:

    def __init__(self, rgb):
        """ representaiton of color using 3 floating point values

        >>> c = RGB((.3, .3, .75))
        >>> c.values
        (0.3, 0.3, 0.75)
        >>> c = RGB((1, 0, 1))
        >>> c.values
        (1.0, 0.0, 1.0)
        >>>
        """
        self.values = (float(rgb[0]), float(rgb[1]), float(rgb[2]))

    def __repr__(self):
        """
        >>> RGB((.5, .5, 1))
        RGB((0.5, 0.5, 1.0))
        """
        return f"RGB(({self.values[0]}, {self.values[1]}, {self.values[2]}))"

    def __iter__(self):
        """ iterate through components in r,g,b order
        >>> c = RGB((1, 2, 3))
        >>> list(c)
        [1.0, 2.0, 3.0]
        """
        return iter(self.values)

    def quantize(self, top):
        """ return a tuple of ints all in range(top+1)
        >>> RGB((.3, .3, .75)).quantize(255)
        (76, 76, 191)
        >>> RGB((.5, .8, 1.1)).quantize(255)
        (128, 204, 255)
        """
        vals = []
        for val in self.values:
            if val > 1: vals.append(top)
            else: vals.append(round(val * top))
        return tuple(vals)

    
    def __add__(self, other):
        """
        >>> RGB((0.3, 0.5, 0.23)).__add__(RGB((0.1, 0.2, 0.31)))
        RGB((0.4, 0.7, 0.54))
        """
        return RGB(tuple([a+b for a,b in zip(self, other)]))

    def __mul__(self, i):
        """ return a new RGB that is scaled by i

        >>> .25*RGB((.8, .5, .4))
        RGB((0.2, 0.125, 0.1))
        """
        return RGB(tuple([v * i for v in self.values]))

    def __rmul__(self, i):
        """ return a new RGB that is scaled by i

        >>> RGB((.8, .5, .4))*(.25)
        RGB((0.2, 0.125, 0.1))
        """
        return RGB(tuple([v * i for v in self.values]))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
