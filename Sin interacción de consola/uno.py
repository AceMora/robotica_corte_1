"""
1. Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos
vectores previamente inicializados.
"""

import numpy as resultado


vector1 = resultado.array([10, 20, 30])
vector2 = resultado.array([2, 4, 6])


suma = vector1 + vector2
resta = vector1 - vector2
producto_punto = resultado.dot(vector1, vector2)
producto_cruz = resultado.cross(vector1, vector2)
division = vector1 / vector2


print("Suma", suma)
print("Resta", resta)
print("Producto punto:", producto_punto)
print("Producto cruz", producto_cruz)
print("Division:", division)
