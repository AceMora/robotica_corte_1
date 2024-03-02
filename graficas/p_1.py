
"""1. Realice un programa que grafique el comportamiento de un sensor PT100 desde -200°C a 200°C."""

import matplotlib.pyplot as plt

# Coeficientes de la ecuación de resistencia PT100
R0, A, B, C = 100, 3.969e-3, -5.8410e-7, -4.183e-12

# Rango de temperaturas
temperaturas_positivas = range(1, 201)  # Temperaturas mayores que cero
temperaturas_negativas = range(-200, 1)  # Temperaturas menores o iguales a cero

# Calcula la resistencia para cada temperatura
resistencias_positivas = [R0 * (1 + A * t + B * t**2 + C * t**3 * (t - 100)) for t in temperaturas_positivas]
resistencias_negativas = [R0 * (1 + A * t + B * t**2) for t in temperaturas_negativas]

# Graficar
plt.plot(temperaturas_positivas, resistencias_positivas, label='Temperatura > 0°C')
plt.plot(temperaturas_negativas, resistencias_negativas, label='Temperatura <= 0°C')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (ohm)')
plt.title('Comportamiento del sensor PT100')
plt.grid(True)
plt.legend()
plt.show()
