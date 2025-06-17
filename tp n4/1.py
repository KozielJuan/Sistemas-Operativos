import os
os.system("cls")
limite = 100000
total = 0

print("Ingrese los gastos del mes (0 para terminar):")
while True:
    gasto = float(input("Gasto: "))
    if gasto == 0:
        break
    total += gasto

print("Total gastado:", total)
if total > limite:
    print("¡Advertencia! Se superó el límite presupuestado.")