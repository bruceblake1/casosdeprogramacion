#RESTA SELECTIVA
n1= int(input("Ingrese el primer numero: "))
n2= int(input("Ingrese el segundo numero: "))
if (n1 >= n2):
    print(" El resultado de la resta es: " +str(n1-n2))
elif n1==n2:
    print(" El resultado de la resta es:" +str(n1-n2))
else:
    print(" El resultado de la resta es: " -str(n2-n1))
print("Fin")