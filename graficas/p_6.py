"""6. Obtenga las coordenadas X y Y de los contornos de dos logos de automóviles (Chevrolet, Hyundai,
Mazda, etc.), a través de Python."""

import cv2
import numpy as np

# Leer la imagen del logo del automóvil
image = cv2.imread('logo_chevrolet.png')

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización adaptativa para mejorar la detección de contornos
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)


contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Crear una imagen en blanco del mismo tamaño que la original
contour_image = np.zeros_like(image)

# Dibujar los contornos encontrados en la imagen en blanco
cv2.drawContours(contour_image, contours, -1, (255, 255, 255), 2)


height, width, _ = contour_image.shape
max_height = 500
max_width = 800
scale = min(max_height/height, max_width/width)
resized_image = cv2.resize(contour_image, None, fx=scale, fy=scale)


cv2.imshow('Contornos', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
