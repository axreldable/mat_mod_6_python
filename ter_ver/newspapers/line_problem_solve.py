from matplotlib import pyplot as plt

from ter_ver.newspapers.NewspaperTask import NewspaperTask

mass_i = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
dispersion = 4

a = 5
b = 10

task = NewspaperTask(mass_i, dispersion, a, b)
print(task)

k_array = range(0, 25)
min_func_array = []
for k in k_array:
    line_prog = task.get_line_prog(k)
    min_func_array.append(line_prog.fun)

plt.plot(k_array, min_func_array, 'ro', label='func_min')
plt.title("Newspaper task decision")
plt.legend()
plt.show()
print("done")
