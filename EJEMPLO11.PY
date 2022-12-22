#MOSTRAR UN MENU DE OPCIONES DONDE EL USUARIO ELIJA CUAL ES EL PLATILLO QUE DESEA CONSEGUIR

print("**********         MENU          *************")
print("***                                        ***")
print("***a) aaroz con pollo 25.00 ***")
print("***b) tallarines rojos 20.00 ***")
print("***c) chicharron 35.00***")
print("***d) aji de gallina 18.00")
print("***                                        ***")
print("**********************************************")
platillo=input("Elija una opcion [a,b,c,d]: ")
bebidas=int(input("Cuantas bebidas desea: "))
totalbebidas=bebidas*6.00
error=0
if platillo == "a":
    totalplatillo=25.00
elif platillo =="b":
    totalplatillo=20.00
elif platillo =="c":
    totalplatillo=35.00
elif platillo =="d":
    totalplatillo=18.00
else:
    print("Opcion Incorrecta")
    error=1
if error==0:
    print("Su cuenta es de : ", totalplatillo + totalbebidas)