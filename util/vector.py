import math


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def coords(self):
        return self.x, self.y

    @property
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @property
    def direction(self):
        length = self.length
        return self.x/length, self.y/length

    def normalize(self):
        self.x, self.y = self.direction

    def __add__(self, other):
        assert isinstance(other, type(self)) or isinstance(other, int) or isinstance(other, float)
        if isinstance(other, type(self)):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x + other, self.y + other)

    def __sub__(self, other):
        return self + -1 * other

    def __mul__(self, other):
        assert isinstance(other, type(self)) or isinstance(other, int) or isinstance(other, float)
        if isinstance(other, type(self)):
            return Vector(self.x * other.x, self.y * other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other)

    def __truediv__(self, other):
        return self * Vector(1/other.x, 1/other.y)

    def __floordiv__(self, other):
        return self * Vector(1//other, 1//other.y)

    def __eq__(self, other):
        assert isinstance(other, type(self))
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other