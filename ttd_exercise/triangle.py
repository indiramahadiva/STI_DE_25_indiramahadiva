import numbers


class Triangle:
    # x and y optional
    def __init__(self, base, height, height_2):
        self.base = base
        self.height = height
        self.height_2 = height_2

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        if not isinstance(value, numbers.Number):
            raise TypeError("must be a number")

        if value <= 0:
            raise ValueError("base must be larger than zero")
        self._base = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, numbers.Number):
            raise TypeError("must be a number")
        self._height = value

    @property
    def height_2(self):
        return self._height_2

    @height.setter
    def height_2(self, value):
        if not isinstance(value, numbers.Number):
            raise TypeError("must be a number")
        self._height_2 = value

    @property
    def area(self):
        return 0.5 * self._base * self._height

    # @property
    # def perimeter(self):
    #     pass


def __eq__(self, other):
    """Checks if two triangles are equal based on their area."""
    if not isinstance(other, Triangle):
        return NotImplemented
    return self.area == other.area


def __lt__(self, other):
    """Checks if this triangle is smaller than another based on area."""
    if not isinstance(other, Triangle):
        return NotImplemented
    return self.area < other.area


def __gt__(self, other):
    """Checks if this triangle is larger than another based on area."""
    if not isinstance(other, Triangle):
        return NotImplemented
    return self.area > other.area


def equilateral(self, b):
    return "equilateral"


def __repr__(self):
    return f"Triangle(base={self.base}, height={self.height})"
