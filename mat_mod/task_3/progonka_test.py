import math

import numpy as np

from mat_mod.task_3.progonka import method_progonki

N = 10  # grid spacing
mu1 = 0
mu2 = 10


def random_array(length):
    return np.random.rand(length)
    # rez = []
    # for i in range(0, length):
    #     rez.append(random.randint(0, 10))
    # return rez


A = random_array(N - 2)
B = random_array(N - 2)
C = random_array(N - 2)
random_F = random_array(N - 2)
print("random_F = ")
print(random_F)


def get_f(a, b, c, y):
    f = [0] * (N - 2)
    for i in range(0, N - 2):
        f[i] = - (a[i] * y[i + 2] - c[i] * y[i + 1] + b[i] * y[i])
    return f


y = method_progonki(N, A, B, C, random_F, mu1, mu2)

count_F = get_f(A, B, C, y)
print("count_F = ")
print(count_F)


def compare_array(a, b, eps):
    for i in range(0, len(a)):
        if math.fabs(a[i] - b[i]) > eps:
            return False
    return True


def printLine():
    print("-------------------------------------------")


printLine()
if compare_array([1, 1, 1], [1, 1.001, 1], 0.01):
    print("compare_array works correct")
else:
    print("compare_array doesn't work")
printLine()

printLine()
if compare_array(random_F, count_F, 0.0000001):
    print("method_progonki works correct")
else:
    print("method_progonki doesn't work")
printLine()
