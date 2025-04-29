dia=int(input("Ingrese un numero del 1 al 7 (1:lunes 7:domingo):"))
if dia > 0 and dia <= 7:
    if dia >= 1 and dia <= 5:
        print("Dia laboral")
    else:
        print("Fin de semana")