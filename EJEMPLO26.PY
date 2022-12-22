n1= int(input("Ingrese el primer numero: "))
n2= int(input("Ingrese el segundo numero: "))
while (n1<=0 or n2<=0) or n2<=n1:
    print("ERROR")
    n1= int(input("Ingrese el primer numero: "))
    n2= int(input("Ingrese el segundo numero: "))
for numero in range (n1,n2+1):
    cantidad_divisores = 0
    for divisor in range(1,numero+1):
        if numero%divisor == 0:
            cantidad_divisores += 1
        if cantidad_divisores == 2:
            print(numero, " Es un numero primo")