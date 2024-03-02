"""5. Dibuje el nombre de cada uno de los integrantes del grupo en un plot en 2D, teniendo en cuenta
líneas rectas y/o curvas."""

import matplotlib.pyplot as plt



plt.plot([0, 1, 2], [0, 3, 0], color='blue')  #  A
plt.plot([2.5, 2.5, 2.5, 3.5], [0, 3, 0, 0], color='blue')  #  L
plt.plot([4, 5, 4, 4, 5, 4, 4, 5], [0, 0, 0, 1.5, 1.5, 1.5, 3, 3], color='blue')  
plt.plot([5.5, 6, 6.5, 6, 5.5, 6.5], [0, 1.5, 3, 1.5, 3, 0], color='blue') 


plt.title('Nombre: ALEX')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.grid(True)

plt.show()
