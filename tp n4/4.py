import os
os.system("cls")
aprobados = 0
print("Ingrese las notas de 10 alumnos:")
for i in range(10):
    nota = float(input(f"Nota {i+1}: "))
    if nota >= 7:
        aprobados += 1

print("Aprobados:", aprobados)
print("Desaprobados:", 10 - aprobados)