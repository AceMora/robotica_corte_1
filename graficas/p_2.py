"""2. Realice un programa que le permita al usuario ingresar los coeficientes de una función de
transferencia de segundo orden y graficar su comportamiento, además se debe mostrar que tipo
de sistema es: subamortiguado, criticamente amortiguado y sobreamortiguado."""

import numpy as np
import matplotlib.pyplot as plt
import control

def determinar_tipo_amortiguamiento(zeta):
    if np.all(zeta < 1):
        return "subamortiguado"
    elif np.all(zeta == 1):
        return "críticamente amortiguado"
    else:
        return "sobreamortiguado"


def graficar_respuesta(tiempo, respuesta):
    plt.plot(tiempo, respuesta)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Respuesta')
    plt.title('Respuesta del sistema')
    plt.grid(True)
    plt.show()

def main():
    # Solicitar al usuario que ingrese los coeficientes
    Kp = float(input("Ingrese el coeficiente Kp: "))
    zeta = float(input("Ingrese el coeficiente de amortiguamiento (zeta): "))
    omega = float(input("Ingrese la frecuencia natural (omega): "))

    # Crear la función de transferencia
    sys = control.TransferFunction([Kp * omega**2], [1, 2 * zeta * omega, omega**2])
    
    # Obtener parámetros del sistema de segundo orden
    zeta, wn, poles = control.damp(sys)

    # Determinar el tipo de amortiguamiento
    tipo_amortiguamiento = determinar_tipo_amortiguamiento(zeta)
    print("El sistema es", tipo_amortiguamiento)

    # Simular la respuesta del sistema
    tiempo, respuesta = control.step_response(sys)

    # Graficar la respuesta del sistema
    graficar_respuesta(tiempo, respuesta)

if __name__ == "__main__":
    main()
