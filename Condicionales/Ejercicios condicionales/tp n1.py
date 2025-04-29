edad=int(input("Ingrese la edad:"))
if edad < 18:
    print("Menor de edad")
elif edad >=18 and edad<64:
    print("Adulto")
elif edad >= 64:
    print("Adulto Mayor")