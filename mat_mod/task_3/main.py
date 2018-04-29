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


A = random_array(N-2)
B = random_array(N-2)
C = random_array(N-2)
F = random_array(N-2)
# print(A)
# print(B)
# print(C)
# print(F)

y = method_progonki(N, A, B, C, F, mu1, mu2)
print(y)
