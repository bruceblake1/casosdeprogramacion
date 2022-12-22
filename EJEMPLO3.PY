#ESTRUCTURA SECUENCIAL
#Luego de una caida del puente de san juan de lurigancho y surco, se debe tomar una ruta alterna la cual incrementa el tiempo en un 60%
# y la distancia un 45%, se pide leer el tiempo y la distancia anterior, determinar el tiempo y la distancia actual.
ta=eval(input("Ingrese tiempo="))
da=eval(input("Ingrese distancia="))

ti= (ta*0.6) + ta
di= (da*0.45) + da

print("Tiempo anterior="+str(ta)+"h")
print("Distancia anterior="+str(da)+"km")
print("Tiempo que incremento="+str(ti)+"h")
print("Distancia que incremento="+str(di)+"km")