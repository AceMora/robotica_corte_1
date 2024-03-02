"""4. Realice un programa para el cálculo de la resistencia de una RTD de platino (PT100) en función de
la temperatura.
"""
#fuente = https://metas.com.mx/guia_metas/archivos/La-Guia-MetAs-09-09-CVD.pdf




# Rt = R0 [1 + A*t + B*t^2 + C*t^3(t - 100)]        formula de resistencia PT100

RO, A, B, C = 100, 3.969e-3, -5.8410e-7, -4.183e-12
t= -15 #temperatura

if t> 0:
    Rt = RO*(1 + A*t + B*t**2 + C*t**3*(t - 100))
    print("la resistencia para una temperatura de ", t, "°C es", Rt, "ohm")

else:
    Rt = RO*(1 + A*t + B*t**2 )
    print("la resistencia para una temperatura de ", t, "°C es", Rt, "ohm")