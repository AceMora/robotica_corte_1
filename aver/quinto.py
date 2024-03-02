import numpy as np

def rotacion_x(angulo):
    theta = np.radians(angulo)
    return np.array([[1, 0, 0],
                     [0, np.cos(theta), -np.sin(theta)],
                     [0, np.sin(theta), np.cos(theta)]])

def rotacion_y(angulo):
    theta = np.radians(angulo)
    return np.array([[np.cos(theta), 0, np.sin(theta)],
                     [0, 1, 0],
                     [-np.sin(theta), 0, np.cos(theta)]])

def rotacion_z(angulo):
    theta = np.radians(angulo)
    return np.array([[np.cos(theta), -np.sin(theta), 0],
                     [np.sin(theta), np.cos(theta), 0],
                     [0, 0, 1]])

grados = 90

print("El resultado de la rotación de las matrices con un ángulo de", grados, "es:\n")

print("\nROT_X\n", rotacion_x(grados), "\n\nROT_Y\n", rotacion_y(grados), "\n\nROT_Z\n", rotacion_z(grados))
