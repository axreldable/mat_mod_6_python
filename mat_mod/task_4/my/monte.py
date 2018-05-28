import math

from mat_mod.task_2.planet import Point, distance
import matplotlib.pyplot as plt

point1 = Point(1, 2)
point2 = Point(2, 2)

print(point1.add(point2))
print(distance(point1, point2))

dx0 = 1 / 14
dy0 = math.sqrt(3) / 2 * dx0

points = []
for i in range(0, int(1 / dx0)):
    for j in range(0, int(1 / dy0)):
        points.append(Point(i * dx0, j * dy0))


def get_x_y(points):
    x = []
    y = []
    for i in range(0, len(points)):
        x.append(points[i].x)
        y.append(points[i].y)
    return x, y


(x, y) = get_x_y(points)
fig, ax = plt.subplots()
ax.plot(x, y, 'o')
ax.set_title('Using hyphen instead of Unicode minus')
plt.show()
