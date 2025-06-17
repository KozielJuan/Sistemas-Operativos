import os
os.system("cls")
stock = int(input("Stock inicial: "))
inicial = stock

while stock > 0:
    venta = int(input("Cantidad vendida (0 para salir): "))
    if venta == 0:
        break
    if venta <= stock:
        stock -= venta
    else:
        print("Venta excede el stock.")

    if stock < inicial * 0.1:
        print("Alerta: queda menos del 10% del stock.")

print("Stock final:", stock)