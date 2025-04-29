saldo=int(input("Ingrese el saldo restante:"))
retiro=int(input("Ingrese lo que desea retirar:"))
if saldo > retiro:
    total=saldo-retiro
    print("usted retiro",retiro,", el saldo ahora es de",total)
else:
    print("Saldo insuficiente")