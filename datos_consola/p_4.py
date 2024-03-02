"""4. Realice un programa que le permita al usuario escoger entre robot Cilíndrico, Cartesiano y esférico,
donde como respuesta a la selección conteste con el tipo y número de articulaciones que posee."""

print("Seleccione el tipo de robot:")
print("1. Cilíndrico")
print("2. Cartesiano")
print("3. Esférico")


opcion = input("Ingrese el tipo de robot: ")

if opcion == "1":
    print("El robot cilíndrico tiene 1 articulacion rotacional y dos prismaticaS")
elif opcion == "2":
    print("El robot cartesiano tiene 3 articulaciones prismaticas")
elif opcion == "3":
   print("los robots esfericos tienen 2 articulaciones rotacionales y una lineal. ")

else:
    print("Opcion Incorrecta")