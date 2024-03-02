"""
3. Realice un programa que convierta coordenadas rectangulares a cilíndricas y esféricas, para lo cual
deben consultar sobre el uso de funciones trigonométricas en Python.
"""

import math as m


x, y, z = 2, 3, 8

#_____________________________________________
#rectangulares a cilindricas


r =m.sqrt(x**2 + y**2)
theta = m.atan2(y, x)       #atan2 = y/x
#convierte rad a grados
gtheta= m.degrees(theta)

#_________rectangulares a esfericas_________

r1 =m.sqrt(x**2 + y**2+ z**2)
phi = m.phi = m.acos(z / r1)
theta2 = m.atan2(y, x)

#convierte rad a grados
gphi= m.degrees(phi)
gtheta2 = m.degrees(theta2)

#________________________________________________

print("x, y, z:",x, y, z )
print("rectangulares a cilindricas:",r, gtheta, z)
print("rectangulares a esfericas:", r1, gphi, gtheta2)

