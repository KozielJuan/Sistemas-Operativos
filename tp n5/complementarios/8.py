Vec = []

print ("Ingrese dimensión del vector: ")
tamVec = int( input())
pares = tamVec*[0]
impares = tamVec*[0]
print ( "Ingrese los", tamVec, "valores del vector")
for x in range(tamVec):
    elemento = int( input("Elemento {}: ".format(x+1)))
    Vec.append(elemento)
vpr = 0
i = 0
for x in range(tamVec):
    if Vec[x] % 2 == 0:
        pares[vpr] = Vec[x]
        vpr = vpr + 1
    else:
        impares[i] = Vec[x]
        i = i + 1
print(pares[0:vpr])
print ( "El vector de pares tiene" , vpr, "elementos")
print(impares[0:i])
print ( "El vector de impares tiene", i, "elementos")

if vpr > i :
    print ( "El vector de pares es el más grande")
elif vpr < i:
    print ( "El vector de impares es el mas grande")
else:
    print ( "Los 2 vectores son iguales en número de elementos")