"""
2. Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos
matrices previamente inicializadas.
"""

import numpy as result

matriz1 = result.array([[1, 2, 3],
                        [1, 2, 3],
                        [1, 2, 3]])

matriz2 = result.array([[10, 2, 35],
                        [2, 1, 4],
                        [7, 5, 4]])


suma=matriz1 +   matriz2
resta= matriz1 - matriz2
prod_punto = result.dot(matriz1, matriz2)
prod_cruz =  result.cross(matriz1, matriz2)
division=  matriz1/matriz2

print("Las matrices son:")

print(matriz1, "\n")
print(matriz2, "\n")


print("suma:", suma,"\n")
print("resta:", resta)
print("producto punto:", prod_punto)
print("producto cruz:", prod_cruz)