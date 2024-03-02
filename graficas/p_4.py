"""4. Consulte y elabore un sistema coordenado X, Y y Z donde se dibuje un vector con coordenadas
ingresadas por el usuario."""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Coordenadas del vector
x = float(input("Ingrese la coordenada X del vector: "))
y = float(input("Ingrese la coordenada Y del vector: "))
z = float(input("Ingrese la coordenada Z del vector: "))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.quiver(0, 0, 0, x, y, z)


max_range = max(x, y, z)
ax.set_xlim([-max_range, max_range])
ax.set_ylim([-max_range, max_range])
ax.set_zlim([-max_range, max_range])


plt.show()
