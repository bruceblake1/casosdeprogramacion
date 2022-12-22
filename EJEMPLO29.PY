resp= "Si"
while (resp!="No"):
    print ("Ingresa el Nombre del alumno")
    nom=input()
    print ("Cuantas calificaciones vas a promediar")
    nCal= input()
    nCal= int(nCal)
    suma= 0
    for i in range (1, nCal+1):
        print("Ingresa la ", i , "a. calificar")
        cal= input()
        cal = float(cal)
        suma= suma + cal
    promedio = suma/ nCal
    #comprobando si el promedio es aprobatorio o desaprobatorio
    if (promedio>=10.5):
        print("el alumno", nom, "tiene de promedio", promedio, "y es aprobatorio")
    else:
        print("el alumno", nom, "tiene de promedio", promedio, "y es reprobatorio")
    #pregunta si el usuario desea capturar otro alumno
    print("Desea captura a otro alumno(si/no)? : ")
    resp= input()