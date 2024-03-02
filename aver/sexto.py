
"""Realice un programa que calcule la fuerza de avance y retroceso de un cilindro neumático de doble
efecto. Debe establecer previamente los valores de presión, así como las dimensiones físicas del
cilindro para realizar el cálculo.
"""


import math as m

diametro_cilin, diametro_vastago = 0.1, 0.02
P = 40000


area_avance = m.pi * ((diametro_cilin**2)/4)

area_retro = m.pi * ((diametro_cilin**2- diametro_vastago**2)/4)


f_avance= area_avance*P
f_retro= area_retro*P

print("el cilindro trabaja con una presion nominal de ", P, "Pa")
print("la fuerza de avance del cilindro es de:", f_avance, "N")
print("la fuerza de retroceso del cilindro es de:", f_retro, "N")
