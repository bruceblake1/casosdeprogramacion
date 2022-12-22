num=1
print("¿Cuantas edades promediara? ")
cant= int(input())
prom= 0
while num <= cant:
    print("Ingrese la edad numero: ", num)
    edad = float (input())
    prom+=edad
    num+=1
print("El promedio de edades es: ", prom/cant)