continuar = 1
while continuar == 1 :
    edad = int(input("Ingresa tu edad: "))
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
        continuar = int(input("Quieres continuar?\n1 = Si\nOtro numero = No: "))
print("Hasta luego")