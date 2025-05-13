total = 0
while True:
    precio = float(input("Ingresá el precio del producto (0 para terminar): "))
    if precio == 0:
        break
    total += precio
if total > 10000:
    total *= 0.9
    print("Se aplicó un 10% de descuento.")
print(f"Total a pagar: ${total:.2f}")