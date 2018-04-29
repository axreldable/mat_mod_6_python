import matplotlib.pyplot as plt

from mat_mod.task_2.planet import *

step = 0.01
m1 = 1
m2 = 100000
G = 9.987


def get_next_half_r(r_prev, v_prev):
    return r_prev.add(v_prev.multi(step * 0.5))


def get_next_r(r_prev, v_prev_half):
    return r_prev.add(v_prev_half.multi(step))


def get_next_v_half_1(r_1_prev, r_2_prev, v_prev):
    return v_prev.add(get_f(r_1_prev, r_2_prev).multi(step * G * m2 * 0.5))


def get_next_v_1(r_1_prev_half, r_2_prev_half, v_prev):
    return v_prev.add(get_f(r_1_prev_half, r_2_prev_half).multi(step * G * m2))


def get_next_v_half_2(r_1_prev, r_2_prev, v_prev):
    return v_prev.minus(get_f(r_1_prev, r_2_prev).multi(step * G * m1 * 0.5))


def get_next_v_2(r_1_prev_half, r_2_prev_half, v_prev):
    return v_prev.minus(get_f(r_1_prev_half, r_2_prev_half).multi(step * G * m1))


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

for i in range(0, 1000):
    v1_prev_half = get_next_v_half_1(r1_prev, r2_prev, v1_prev)
    v2_prev_half = get_next_v_half_2(r1_prev, r2_prev, v2_prev)

    r1_next = get_next_r(r1_prev, v1_prev_half)
    r2_next = get_next_r(r2_prev, v2_prev_half)

    point_mass_1.append(r1_next)
    point_mass_2.append(r2_next)

    r1_prev_half = get_next_half_r(r1_prev, v1_prev)
    r2_prev_half = get_next_half_r(r2_prev, v2_prev)

    v1_next = get_next_v_1(r1_prev_half, r2_prev_half, v1_prev)
    v2_next = get_next_v_2(r1_prev_half, r2_prev_half, v2_prev)

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
plt.title("Взаимодействие 2-х тел")
plt.legend()
plt.show()
