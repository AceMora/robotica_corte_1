"""3. Implemente la ecuación de carga y descarga para un circuito RC. El usuario ingresa por teclado el
valor de voltaje (V), capacitancia (μF) y resistencia (Ω). Posteriormente realice en Python la
gráfica."""

import numpy as np
import matplotlib.pyplot as plt

V = float(input("Ingrese el voltaje (V): "))
C = float(input("Ingrese la capacitancia (uF): ")) * 1e-6
R = float(input("Ingrese la resistencia (ohm): "))

t = np.linspace(0, 5 * R * C, 1000)  

V_max = V
carga = V_max * (1 - np.exp(-t / (R * C)))
descarga = V_max * np.exp(-t / (R * C))

plt.plot(t, carga, label='Carga')
plt.plot(t, descarga, label='Descarga')
plt.title('Carga y descarga de un capacitor en un circuito RC')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.legend()
plt.grid(True)

# Ajustar límites del eje y para mostrar todos los valores de voltaje
plt.ylim(0, V_max)

plt.show()
