par = False

for i in range(5):
    num = int(input("Ingresá un número: "))
    if num % 2 == 0:
        par = True

if par:
    print("Al menos uno es par.")
else:
    print("No hay números pares.")