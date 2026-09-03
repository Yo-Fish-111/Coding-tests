from math import sqrt

class Vector:
    x: float
    y: float

class Vector:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __sub__(self, other):
        return self + -other

    def __truediv__(self, other):
        return Vector(self.x/other, self.y/other)

    def __mul__(self, other):
        return Vector(self.x*other, self.y*other)

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        return f"({self.x}, {self.y})"

    def length(self):
        return sqrt(self.x**2 + self.y**2)

    def setMag(self, newMagnitude):
        self.x*= newMagnitude / self.length()
        self.y*= newMagnitude / self.length()

