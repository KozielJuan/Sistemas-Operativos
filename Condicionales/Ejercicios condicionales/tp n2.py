vel=float(input("Ingrese la velocidad del vehiculo:"))
if vel<=60:
    print("Dentro del limite permitido")
elif vel>60 and vel<=80:
    print("Esta en exceso leve")
else:
    print("Esta en exceso grave")