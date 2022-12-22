condicion = True
while condicion:
    m = int(input("Ingrese numero: "))
    if m < 0:
        print ("Numero negativo" , (m))
        condicion = False