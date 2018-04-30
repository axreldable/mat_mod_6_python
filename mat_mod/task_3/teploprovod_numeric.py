import math

import matplotlib.pyplot as plt
import numpy as np

# сетка по x
from mat_mod.task_3.progonka import method_progonki

n = 200
l = 2.0
step_h = l / n
x = np.arange(0.0, l, step_h)

# сетка по времени
T = 0.03
step_t = 0.001


# граничные условия
mu_1 = 0
mu_2 = 0


A = [step_t / (step_h ** 2)] * (n - 2)
B = [step_t / (step_h ** 2)] * (n - 2)
C = [(2 * step_t / (step_h ** 2)) + 1] * (n - 2)


def phi(x):
    return math.sin((5 * math.pi / 2) * x)


y_start = []
for i in x:
    y_start.append(phi(i))


def get_f_from_y(y):
    return y[1:-1]


y_next = y_start
y_for_anim = [y_next]

for i in range(0, int(T / step_t)):
    F = get_f_from_y(y_next)
    y_next = method_progonki(n=n, a=A, b=B, c=C, f=F, mu1_local=mu_1, mu2_local=mu_2)
    y_for_anim.append(y_next)


plt.plot(x, y_start, 'ro', label='func_min')
plt.plot(x, y_next)

plt.title("Newspaper task decision")
plt.legend()
plt.show()
print("done")


# Animation

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_xlim(-1, 3)
ax1.set_ylim(-1, 1)
for i in range(0, int(T / step_t)):
    ax1.plot(x, y_for_anim[i])
    plt.pause(0.001)


while True:
    pass
