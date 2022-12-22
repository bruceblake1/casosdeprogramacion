#AUMENTO DE SUELDO
#TIEMPO DE SERVICIO DE 1 A 5 AÑOS, AUMENTO 3%
#TIEMPO DE SERVICIO DE 5 A 10 AÑOS, AUMENTO 5%
#TIEMPO DE SERVICIO DE 10 A 20 AÑOS, AUMENTO 8%
#TIMEPO DE SERVICIO DE 20 A MAS AÑOS, AUMENTO 12%
años= int(input("Cuantos años de servicios tienes?: "))
sueldo= int(input("Cuanto es tu sueldo?: "))
if años >= 1 and años >= 5:
    print(" TU AUMENTO DE SUELDO ES:" +str(sueldo+sueldo*0.03))
elif años >= 5 and años >= 10:
    print(" TU AUMENTO DE SUELDO ES:" +str(sueldo+sueldo*0.05))
elif años >=10 and años>=20:
    print(" TU AUMENTO DE SUELDO ES:" +str(sueldo+sueldo*0.08))
elif años>=20:
    print(" TU AUMENTO DE SUELDO ES:" +str(sueldo+sueldo*0.12))
else:
    print("Usted no ha trabajado")