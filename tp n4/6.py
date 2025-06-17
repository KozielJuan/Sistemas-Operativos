import os
os.system("cls")
total = 0
mayor = 0
personas = 0

print("Ingrese donaciones (0 para finalizar):")
while True:
    donacion = float(input("Donación: "))
    if donacion == 0:
        break
    total += donacion
    personas += 1
    if donacion > mayor:
        mayor = donacion

print("Total recaudado:", total)
print("Mayor donación:", mayor)
print("Cantidad de personas:", personas)