nombre =""
print("Digame su nombre porfavor: ")
while nombre!= "Aaron":
    nombre = input()
    if nombre != "Aaron" :
        print("Ingrese su nombre nuevamente: ")
    else:
        print("Su nombre es Aaron")
        break
print("Ha salido del bucle")