comprobar = True
while comprobar == True:
    n = int(input("Ingrese un numero positivo: "))
    if n >= 0:
        for i in range(1,20):
            print(n, "x " , i , " = ", n*i)
        comprobar = False
    else:
        print("El numero no es correcto. Intentelo denuevo ")
