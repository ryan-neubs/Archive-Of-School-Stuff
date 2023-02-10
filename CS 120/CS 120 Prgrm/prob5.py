# Problem 5
# Ryan Neubauer

class Cube:

    def __init__(self, length):
        self.sidelength = length

    def set_side_length(self, length):
        self.sidelength = length

    def area(self):
        cubeArea = (self.sidelength ** 2) * 6
        return cubeArea

    def vol(self):
        cubeVol = self.sidelength ** 3
        return cubeVol
