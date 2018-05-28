import math


class Point:
    def __init__(self, x_v, y_v):
        self.x = x_v
        self.y = y_v

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def minus(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def multi(self, a):
        return Point(a * self.x, a * self.y)

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


def distance(point_1, point_2):
    return math.pow(math.sqrt(math.pow(point_2.x - point_1.x, 2) + math.pow(point_2.y - point_1.y, 2)), 3)


def get_f(point_1, point_2):
    mnoz = 1 / distance(point_1, point_2)
    return point_2.minus(point_1).multi(mnoz)


def get_coordinates_array(point_mass):
    x = []
    y = []
    for point in point_mass:
        x.append(point.x)
        y.append(point.y)
    return x, y

