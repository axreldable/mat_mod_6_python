from matplotlib import pyplot as plt
from matplotlib.lines import Line2D

from planet_pack.planet import *

step = 0.01
m1 = 1
m2 = 100000
G = 9.987


def get_next_r(r_prev, v_prev):
    return r_prev.add(v_prev.multi(step))


def get_next_v_1(r_1_prev, r_2_prev, v_prev):
    return v_prev.add(get_f(r_1_prev, r_2_prev).multi(step * G * m2))


def get_next_v_2(r_1_prev, r_2_prev, v_prev):
    return v_prev.minus(get_f(r_1_prev, r_2_prev).multi(step * G * m1))


def get_first_space_speed(mass, radius):
    return math.sqrt(G * mass / radius)


rad = 100
r10 = Point(0, rad)
r20 = Point(0, 0)
v10 = Point(get_first_space_speed(m2, rad), 0)  # sputnik
v20 = Point(0, 0)  # Earth

r1_prev = r10
r2_prev = r20
v1_prev = v10
v2_prev = v20
point_mass_1 = []
point_mass_2 = []
point_mass_1.append(r1_prev)
point_mass_2.append(r2_prev)

for i in range(0, 100000):
    r1_next = get_next_r(r1_prev, v1_prev)
    r2_next = get_next_r(r2_prev, v2_prev)

    v1_next = get_next_v_1(r1_prev, r2_prev, v1_prev)
    v2_next = get_next_v_2(r1_prev, r2_prev, v2_prev)

    point_mass_1.append(r1_next)
    point_mass_2.append(r2_next)

    r1_prev = r1_next
    r2_prev = r2_next
    v1_prev = v1_next
    v2_prev = v2_next

x1, y1 = get_coordinates_array(point_mass_1)
x2, y2 = get_coordinates_array(point_mass_2)

print(x1)
print(y1)
# print(x2)
# print(y2)

plt.plot(x1, y1, 'ro', label='telo_1')
plt.plot(x2, y2, 'bs', label='telo_2')
plt.title("two bodies")
plt.legend()
plt.show()


def get_next_array(ar, start):
    rez_array = [ar[start + 1], ar[start + 2], ar[start + 3], ar[start + 4], ar[start + 5]]
    return rez_array


fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_xlim(-420, 400)
ax1.set_ylim(-400, 400)
ax2 = fig.add_subplot(1, 1, 1)
line1 = Line2D([], [], color='red', marker='o', markeredgecolor='r')
ax2.add_line(line1)
for t in range(0, 100000, 5):
    x_1 = get_next_array(x1, t)
    y_1 = get_next_array(y1, t)
    x_2 = get_next_array(x2, t)
    y_2 = get_next_array(y2, t)
    ax1.plot(x_1, y_1)
    ax2.plot(x_2, y_2, 'ro')
    plt.pause(0.0000001)
