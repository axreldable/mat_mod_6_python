import math
import random

from mat_mod.task_2.planet import Point, distance
import matplotlib.pyplot as plt


def get_distance(a, b):
    res = [math.sqrt((a.x - (b.x + a_x * -1)) ** 2 + (a.y - (b.y + a_y * -1)) ** 2),
           math.sqrt((a.x - (b.x + a_x * 0)) ** 2 + (a.y - (b.y + a_y * -1)) ** 2),
           math.sqrt((a.x - (b.x + a_x * 1)) ** 2 + (a.y - (b.y + a_y * -1)) ** 2),
           math.sqrt((a.x - (b.x + a_x * -1)) ** 2 + (a.y - (b.y + a_y * 1)) ** 2),
           math.sqrt((a.x - (b.x + a_x * 0)) ** 2 + (a.y - (b.y + a_y * 1)) ** 2),
           math.sqrt((a.x - (b.x + a_x * 1)) ** 2 + (a.y - (b.y + a_y * 1)) ** 2),
           math.sqrt((a.x - (b.x + a_x * -1)) ** 2 + (a.y - (b.y + a_y * 0)) ** 2),
           math.sqrt((a.x - (b.x + a_x * 0)) ** 2 + (a.y - (b.y + a_y * 0)) ** 2),
           math.sqrt((a.x - (b.x + a_x * 1)) ** 2 + (a.y - (b.y + a_y * 0)) ** 2)]
    return min(res)


def distance_abs(a, b):
    res = [abs(a.x - b.x + a_x * 0) + abs(a.y - b.y + a_y * 0), abs(a.x - b.x + a_x * 1) + abs(a.y - b.y + a_y * 0),
           abs(a.x - b.x + a_x * -1) + abs(a.y - b.y + a_y * 0), abs(a.x - b.x + a_x * 0) + abs(a.y - b.y + a_y * 1),
           abs(a.x - b.x + a_x * 1) + abs(a.y - b.y + a_y * 1), abs(a.x - b.x + a_x * -1) + abs(a.y - b.y + a_y * 1),
           abs(a.x - b.x + a_x * 0) + abs(a.y - b.y + a_y * -1), abs(a.x - b.x + a_x * 1) + abs(a.y - b.y + a_y * -1),
           abs(a.x - b.x + a_x * -1) + abs(a.y - b.y + a_y * -1)]
    return min(res)


def min_distance(point, points):
    res = [d0 + 0.1]
    for apoint in points:
        if (apoint.id != point.id) and (distance_abs(point, apoint) < d0 * 2):
            res.append(get_distance(point, apoint))
    return min(res)


def get_start_points(dx, dy):
    rez = []
    id = 0
    for i in range(0, int(1 / dx)):
        for j in range(0, int(1 / dy)):
            rez.append(Point(id, i * dx, j * dy))
            id += 1
    return rez


def get_x_y(points):
    x = []
    y = []
    for i in range(0, len(points)):
        x.append(points[i].x)
        y.append(points[i].y)
    return x, y


def V(distance):
    return 1. / distance


def get_energy(points):
    rez = 0
    for i in range(0, len(points)):
        for j in range(0, len(points)):
            if i != j:
                rez += V(get_distance(points[i], points[j]))
    return rez / 2


def move_point(point):
    ksi1 = random.uniform(-1, 1)
    ksi2 = random.uniform(-1, 1)
    x = point.x + ksi1 * alpha
    y = point.y + ksi2 * alpha
    if x < 0:
        x += a_x
    elif x > a_x:
        x -= a_x
    if y < 0:
        y += a_y
    elif y > a_y:
        y -= a_y
    return Point(point.id, x, y)


def next_step(points):
    old_energy = get_energy(points)
    for point in points:
        x = point.x
        y = point.y
        tmp = move_point(point)

        if min_distance(tmp, points) > d0:
            point.x = tmp.x
            point.y = tmp.y

            new_energy = get_energy(points)
            dE = new_energy - old_energy
            if dE > 0:
                ksi3 = random.uniform(0, 1)
                if ksi3 < math.e ** (-dE / K * T):
                    old_energy = new_energy
                else:
                    point.x = x
                    point.y = y
            else:
                old_energy = new_energy
        energy.append(old_energy)
        # Draw(points)
        plot_energy()


def plot_energy():
    plt.plot(energy)
    plt.pause(0.00000000000000001)

################################


v = 7
T = 6
K = 1.5

dx = 1 / 14
dy = math.sqrt(3) / 2 * dx
d0 = dx * (1 - 2 ** (v - 8))
alpha = dx - d0

# Размер сетки
a_x = 1
a_y = 1

points = get_start_points(dx, dy)
energy = []
while True:
    next_step(points)


# (x, y) = get_x_y(points)
# fig, ax = plt.subplots()
# ax.plot(x, y, 'o')
# plt.show()




























