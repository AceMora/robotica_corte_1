"""Realice un programa para el cálculo de volúmenes (Prisma, Pirámide, Cono truncado, Cilindro)
donde el usuario pueda seleccionar el sólido y los parámetros de cada volumen."""

import math

print("1. Prisma")
print("2. Pirámide")
print("3. Cono truncado")
print("4. Cilindro")
print("0. Opcion salir")

menu=10

#____________________________________________________
while menu != 0:


    menu = int(input("Seleccione el volumen a calcular: "))

    if menu ==1:
        base = float(input("Ingrese la base del prisma mm: "))
        altura = float(input("Ingrese la altura del prisma mm: "))

        volumen= base* altura

    elif menu == 2:
        base = float(input("Ingrese la base de la pirámide mm: "))
        altura = float(input("Ingrese la altura de la pirámide mm: "))
        volumen = (1/3) * base * altura
        

    elif menu == 3:
        radio_inferior = float(input("Ingrese el radio inferior del cono truncado mm: "))
        radio_superior = float(input("Ingrese el radio superior del cono truncado mm: "))
        altura = float(input("Ingrese la altura del cono truncado mm: "))
        volumen = math.pi * altura *  (radio_inferior**2 + radio_inferior * radio_superior + radio_superior**2) / 3

    elif menu == 4:
            
        radio = float(input("Ingrese el radio del cilindro mm: "))
        altura = float(input("Ingrese la altura del cilindro mm: "))
        volumen = math.pi * radio**2 * altura

    else:
        print("\nOpción no válida\n")
        continue


    print(f"\nEl volumen es {volumen} ^3 mm\n")
    
    print("\n1. Prisma")
    print("2. Pirámide")
    print("3. Cono truncado")
    print("4. Cilindro")
    print("0. Opcion salir")

#____________________________________________________
    
print("\nfin de programa") 



