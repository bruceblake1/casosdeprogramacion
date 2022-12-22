while True:
    print("Si ingresas un 15, algo malo puede ocurrir: ")
    num = int(input("Yo recomiendo ingresar cualquier otro numero: "))
    if num!=13:
        print("Estamos a salvo del 15")
    if num==15:
        while num==15:
            print("Has caido en la trampa del 15")
    print("Has salido sano y salvo de la maldicion 15")
    continuar=int(input("Quieres continuar?n1 = Si\nOtro numero = No: "))
    if continuar !=1:
        break
print("Hasta luego!!!!")