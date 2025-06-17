V1 = 3*[0]
V2 = [0]*3
for i in range(3):
    V1[i] = int( input("V1({}): ".format(i+1)))
for i in range(3):
    V2[i] = int( input("V2({}): ".format(i+1)))
suma = 0
for i in range(3):
    P = V1[i]*V2[i]
    suma = suma + P
print("El producto escalar es:", suma)
x = V1[1]* V2[2] - V1[2]* V2[1]
y = -( V1[0]* V2[2] - V1[2]* V2[0] )
z = V1[0]* V2[1] - V1[1]* V2[0]
print("El producto vectorial es: {}i {}j {}k".format(x, y, z))