V = 100*[0] 
i = 0

print ("Ingrese tamaño del vector")
n = int( input())
opc = -1
while opc != 0:
    print("Ingrese 1 para añadir un elemento al vector")
    print("Ingrese 2 para eliminar un elemento del vector")
    print("Ingrese 3 para listar el contenido del vector ")
    print("Ingrese 4 para contar las apariciones de Un número en el vector")
    print("Ingrese 5 para calcular la media y el máximo de los elementos de un vector")
    print("Ingrese 0 para terminar")

    opc = int( input("Ingrese Opción: "))

    if opc == 1:
        if (i < n) :
            V[i] = int( input("IngreseEntero: "))
            i = i + 1
    elif opc == 2:

        print("Ingrese el número que desea eliminar")
        num = int( input())
        if num > 0:
            a = 0

        for j in range(i):
            if V[j] == num :
                a = j
                break
        if a >= 0 and a <= i:
            for j in range(a, i-1 +1):
                V[j] = V[j+1]
            V[i] = 0
            i = i - 1

    elif opc == 3:
        if i > 0:
            for j in range(i):
                print(V[j])
                
    elif opc == 4:
        c = 0
        print("Ingrese numero para contar número de apariciones: ")
        num = int(input())
        for j in range(i):
            if num == V[j]:
                c = c + 1
        print(" El número de apariciones es: ", c)
    elif opc == 5:
        max = V[0]
        ma = 0
        for j in range(i):
            if max < V[j]:
                max = V[j]
            ma = ma + V[j]
        ma = ma/i
        print("El maximo es:", max, " y la media es: ", ma)
    elif opc == 0:
        print("FIN DE PROGRAMA")
        break