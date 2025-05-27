import math
b=int(input("ingrese los lados del lado b: "))
c=int(input("ingrese los lados del lado c: "))
alfa=int(input("ingrese el angulo en grados sexagesimales: "))
pi=3.1416
a=(b**2+c**2-2*b*c*cos(alfa*pi/180))**0.5
print("el lado a vale: ",a)