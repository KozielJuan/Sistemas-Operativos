animal = []

print ("Ingresar dimensión del array: ")
tamArray = int( input())
print ( "Ingrese los nombres de los animales:")
for x in range(tamArray):
    elemento = input( "Ingrese Animal{}: ".format(x+1) )
    animal.append(elemento)

print ( "Ingrese animal buscado:")
nom = input()
print ( "El animal tiene como vecino a:")
print("-------------------------------------------------------")
for x in range(tamArray):
    if animal[x] == nom:
        if x == 0:
            print(animal[x+1])
        elif x == tamArray-1:
            print(animal[x-1])
        else:
            print(animal[x-1])
            print(animal[x+1])