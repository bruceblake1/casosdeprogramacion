#LISTA DE NUMEROS PARES COMPRENDIDOS ENTRE UN INTERVALO DE NUMEROS
numero1= int(input("Introduce el primer numero: "))
numero2=numero1
while numero2 <= numero1:
    numero2= int(input("Introdue el segundo numero: "))
for n in range (numero1,numero2+1):
    if n % 2 == 0:
        print(n)