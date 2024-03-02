"""2. Realice un programa que calcule X números aleatorios en un rango determinado por el usuario."""

import random

x = int(input("Digite el valor mínimo del rango: "))
y = int(input("Digite el valor máximo del rango: "))
n_numeros = int(input("Digite la cantidad de números aleatorios que quiere ver: "))

for i in range(n_numeros):
    print(random.randint(x, y))
