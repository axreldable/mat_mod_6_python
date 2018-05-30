import math
import random
from tkinter import *

import matplotlib

matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


def initlattice(x, y, dist):
    dx = float(dist)
    dy = math.sin(math.pi / 3) * dist
    result = []
    iid = 0
    for j in range(y):
        if (j % 2 == 0):
            shift = 0
        else:
            shift = dx / 2.
        for i in range(x):
            result.append(Point(iid, shift + i * dx, j * dy))
            iid += 1
    return result


def Distance(a, b):
    res = []
    res.append(math.sqrt((a.x - (b.x + ax * -1)) ** 2 + (a.y - (b.y + ay * -1)) ** 2))
    res.append(math.sqrt((a.x - (b.x + ax * 0)) ** 2 + (a.y - (b.y + ay * -1)) ** 2))
    res.append(math.sqrt((a.x - (b.x + ax * 1)) ** 2 + (a.y - (b.y + ay * -1)) ** 2))
    res.append(math.sqrt((a.x - (b.x + ax * -1)) ** 2 + (a.y - (b.y + ay * 1)) ** 2))
    res.append(math.sqrt((a.x - (b.x + ax * 0)) ** 2 + (a.y - (b.y + ay * 1)) ** 2))
    res.append(math.sqrt((a.x - (b.x + ax * 1)) ** 2 + (a.y - (b.y + ay * 1)) ** 2))
    res.append(math.sqrt((a.x - (b.x + ax * -1)) ** 2 + (a.y - (b.y + ay * 0)) ** 2))
    res.append(math.sqrt((a.x - (b.x + ax * 0)) ** 2 + (a.y - (b.y + ay * 0)) ** 2))
    res.append(math.sqrt((a.x - (b.x + ax * 1)) ** 2 + (a.y - (b.y + ay * 0)) ** 2))
    return min(res)


def DistanceManhattan(a, b):
    res = []
    res.append(abs(a.x - b.x + ax * 0) + abs(a.y - b.y + ay * 0))
    res.append(abs(a.x - b.x + ax * 1) + abs(a.y - b.y + ay * 0))
    res.append(abs(a.x - b.x + ax * -1) + abs(a.y - b.y + ay * 0))
    res.append(abs(a.x - b.x + ax * 0) + abs(a.y - b.y + ay * 1))
    res.append(abs(a.x - b.x + ax * 1) + abs(a.y - b.y + ay * 1))
    res.append(abs(a.x - b.x + ax * -1) + abs(a.y - b.y + ay * 1))
    res.append(abs(a.x - b.x + ax * 0) + abs(a.y - b.y + ay * -1))
    res.append(abs(a.x - b.x + ax * 1) + abs(a.y - b.y + ay * -1))
    res.append(abs(a.x - b.x + ax * -1) + abs(a.y - b.y + ay * -1))
    return min(res)


def MinDistance(point, points):
    res = [d0 + 0.1]
    for apoint in points:
        if (apoint.id != point.id) and (DistanceManhattan(point, apoint) < d0 * 2):
            res.append(Distance(point, apoint))
    return min(res)


def V(distance):
    return 1. / distance


# Lennard-Jones equation
# distance *= 6
# return -1/distance**6 + 1/distance**12

def CalcEnergy(points):
    energy = 0
    #	for pointa in points:
    #		for pointb in points:
    #			if (pointa.id != pointb.id):
    #				energy += V(Distance(pointa, pointb))
    #	return energy / 2
    for x in range(len(points)):
        for y in range(x, len(points)):
            if (points[x].id != points[y].id):
                energy += V(Distance(points[x], points[y]))
    return energy


class Point(object):
    """docstring for Point"""

    def __init__(self, id, x, y):
        super(Point, self).__init__()
        self.id = id
        self.x = x
        self.y = y


def InitShapes(bodies):
    for body in bodies:
        body.shape = canvas.create_oval(0, 0, 5, 5, fill="black")


def Draw(points):
    diam = d0
    xpoint = window_w / float(ax)
    ypoint = window_h / float(ay)
    for point in points:
        canvas.coords(point.shape, (point.x - 0.5 * diam) * xpoint, (point.y - 0.5 * diam) * ypoint,
                      (point.x + 0.5 * diam) * xpoint, (point.y + 0.5 * diam) * ypoint)
    tk.update()


def MovePoint(point, alpha):
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


def DoLoop(points):
    oldenergy = CalcEnergy(points)
    for point in points:
        oldx = point.x
        oldy = point.y
        tmp = MovePoint(point, alpha)
        if (MinDistance(tmp, points) > d0):
            point.x = tmp.x
            point.y = tmp.y
            newenergy = CalcEnergy(points)
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
        Draw(points)
        DoPlot()


def DoPlot():
    #	while True:
    plt.plot(energy)
    plt.pause(0.00000000000000001)


#		time.sleep(1)


# points = initlattice(14, 16, 1/14)
points = initlattice(4, 6, 1 / 4)

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
# Boltzman's constant
# k=1.3806485279 * 10**-23
k = 1
d = 1. / 14
d0 = d * (1 - 2 ** (v - 8))
alpha = d - d0
# alpha=1./6-d0

ax = 1
ay = 1

###
InitShapes(points)
# _thread.start_new_thread( DoPlot, () )
while True:
    DoLoop(points)
time.sleep(5)
