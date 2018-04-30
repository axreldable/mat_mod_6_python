import numpy as np
import math
from matplotlib import pyplot as plt

n = 200
l = 2.0
t = 0.03

step = l / n

x = np.arange(0.0, l, step)

y = []


def phi(x):
    return math.sin((5 * math.pi / 2) * x)


for i in x:
    y.append(phi(i))


def answer(x, t):
    return math.sin((5 * math.pi / 2) * x) * math.exp(-((5 * math.pi / 2) ** 2) * t)


y1 = []

for i in x:
    y1.append(answer(i, t))


plt.plot(x, y, 'ro', label='func_min')
plt.plot(x, y1)

plt.title("Newspaper task decision")
plt.legend()
plt.show()
print("done")






