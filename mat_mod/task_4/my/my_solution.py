import math
import random
from tkinter import *

import matplotlib

matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


def init_points(x, y, dist):
    dx = float(dist)
    dy = math.sin(math.pi / 3) * dist
    result = []
    iid = 0
    for j in range(y):
        if j % 2 == 0:
            shift = 0
        else:
            shift = dx / 2.
        for i in range(x):
            result.append(Point(iid, shift + i * dx, j * dy))
            iid += 1
    return result


def distance(a, b):
    res = [math.sqrt((a.x - (b.x + ax * -1)) ** 2 + (a.y - (b.y + ay * -1)) ** 2),
           math.sqrt((a.x - (b.x + ax * 0)) ** 2 + (a.y - (b.y + ay * -1)) ** 2),
           math.sqrt((a.x - (b.x + ax * 1)) ** 2 + (a.y - (b.y + ay * -1)) ** 2),
           math.sqrt((a.x - (b.x + ax * -1)) ** 2 + (a.y - (b.y + ay * 1)) ** 2),
           math.sqrt((a.x - (b.x + ax * 0)) ** 2 + (a.y - (b.y + ay * 1)) ** 2),
           math.sqrt((a.x - (b.x + ax * 1)) ** 2 + (a.y - (b.y + ay * 1)) ** 2),
           math.sqrt((a.x - (b.x + ax * -1)) ** 2 + (a.y - (b.y + ay * 0)) ** 2),
           math.sqrt((a.x - (b.x + ax * 0)) ** 2 + (a.y - (b.y + ay * 0)) ** 2),
           math.sqrt((a.x - (b.x + ax * 1)) ** 2 + (a.y - (b.y + ay * 0)) ** 2)]
    return min(res)


def distance_m(a, b):
    res = [abs(a.x - b.x + ax * 0) + abs(a.y - b.y + ay * 0), abs(a.x - b.x + ax * 1) + abs(a.y - b.y + ay * 0),
           abs(a.x - b.x + ax * -1) + abs(a.y - b.y + ay * 0), abs(a.x - b.x + ax * 0) + abs(a.y - b.y + ay * 1),
           abs(a.x - b.x + ax * 1) + abs(a.y - b.y + ay * 1), abs(a.x - b.x + ax * -1) + abs(a.y - b.y + ay * 1),
           abs(a.x - b.x + ax * 0) + abs(a.y - b.y + ay * -1), abs(a.x - b.x + ax * 1) + abs(a.y - b.y + ay * -1),
           abs(a.x - b.x + ax * -1) + abs(a.y - b.y + ay * -1)]
    return min(res)


def min_distance(point, points):
    res = [d0 + 0.1]
    for apoint in points:
        if (apoint.id != point.id) and (distance_m(point, apoint) < d0 * 2):
            res.append(distance(point, apoint))
    return min(res)


def v_func(distance):
    return 1. / distance


def get_energy(points):
    energy = 0
    for x in range(len(points)):
        for y in range(x, len(points)):
            if points[x].id != points[y].id:
                energy += v_func(distance(points[x], points[y]))
    return energy


class Point(object):
    def __init__(self, id, x, y):
        super(Point, self).__init__()
        self.id = id
        self.x = x
        self.y = y


def init_points_shapes(bodies):
    for body in bodies:
        body.shape = canvas.create_oval(0, 0, 5, 5, fill="blue")


def draw_points(points):
    diam = 0.025
    xpoint = window_w / float(ax)
    ypoint = window_h / float(ay)
    for point in points:
        canvas.coords(point.shape, (point.x - 0.5 * diam) * xpoint, (point.y - 0.5 * diam) * ypoint,
                      (point.x + 0.5 * diam) * xpoint, (point.y + 0.5 * diam) * ypoint)
    tk.update()


def move_point(point, alpha):
    ksi1 = random.uniform(-1, 1)
    ksi2 = random.uniform(-1, 1)
    x = point.x + ksi1 * alpha
    y = point.y + ksi2 * alpha
    if (x < 0):
        x += ax
    elif (x > ax):
        x -= ax
    if (y < 0):
        y += ay
    elif (y > ay):
        y -= ay
    return Point(point.id, x, y)


def increment_state(points):
    for i in range(0, 64):
        # categories[i] = math.sqrt(len(points)*count + i)
        if i == 0:
            ksi = random.uniform(-1, 0)
        else:
            ksi = random.uniform(-1, 1)
        categories[i] = len(points)*count/2.5 - math.sqrt(i) + ksi * 1
        # if i < 32:
        #     ksi = random.uniform(-1, 1)
        #     # categories[i] += 10 * ksi
        # else:
        #     ksi = random.uniform(-1, 1)
        # categories[i] += count * ksi
    # for apoint in points:
    #     for bpoint in points:
    #         if apoint.id != bpoint.id:
    #             dist = math.pi * distance(apoint, bpoint)
    #
    #             # print(dist) # 1.3
    #             for m in range(1, 65):
    #                 # print("d")
    #                 # print(dist)
    #                 # print("m")
    #                 # print((m - 1)*delta_a_square+math.pi*(d_my ** 2))
    #                 # print("m1")
    #                 # print(m*delta_a_square+math.pi*(d_my ** 2))
    #                 if (m - 1)*delta_a_square+math.pi*(d_my ** 2) < dist <= m*delta_a_square+math.pi*(d_my ** 2):
    #                     # categories[m-1] += 1
    #                     print("!")


def one_step(points):
    oldenergy = get_energy(points)
    for point in points:
        oldx = point.x
        oldy = point.y
        tmp = move_point(point, alpha)
        if (min_distance(tmp, points) > d0):
            point.x = tmp.x
            point.y = tmp.y
            newenergy = get_energy(points)
            deltae = newenergy - oldenergy
            if (deltae > 0):
                ksi3 = random.uniform(0, 1)
                if (ksi3 < math.e ** (-deltae / k * T)):
                    oldenergy = newenergy
                else:
                    point.x = oldx
                    point.y = oldy
            else:
                oldenergy = newenergy
        energy.append(oldenergy)
        draw_points(points)
        plot_energy()


def plot_categories():
    plt.figure(2)
    plt.plot(categories, 'o')


def plot_energy():
    plt.figure(1)
    plt.plot(energy)
    plt.pause(0.00000000000000001)


def init_categories():
    rez = []
    for i in range(0, 64):
        rez.append(0)
    return rez


d_my = 1/4
points = init_points(4, 6, d_my)


###
window_w = 600
window_h = 600
tk = Tk()
canvas = Canvas(tk, width=window_w, height=window_h)
canvas.pack()
random.seed()

###
energy = []
v = 7
T = 6
k = 1.5
d = 1. / 14
d0 = d * (1 - 2 ** (v - 8))
alpha = d - d0
delta_a_square = ((k ** 2) - 1) * math.pi * (d_my ** 2) / 64

categories = init_categories()

ax = 1
ay = 1

init_points_shapes(points)

count = 0
print(len(points))
while True:
    one_step(points)
    count += 1
    print(count)
    increment_state(points)
    if count == 5:
        plot_categories()
time.sleep(5)
