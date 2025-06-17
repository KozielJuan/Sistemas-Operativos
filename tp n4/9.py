import os
os.system("cls")
limite = 20000
total = 0

print("Ingrese el valor de cada compra (0 para finalizar):")
while total < limite:
    compra = float(input("Compra: "))
    if compra == 0:
        break
    if total + compra > limite:
        print("Límite superado. No puede realizar la compra.")
        break
    total += compra

print("Total gastado:", total)