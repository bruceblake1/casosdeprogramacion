#EDAD(MULTIPLE)
#EDAD EN AÑOS               MENSAJE
#DE 0 HASTA 12              ESTAS EN EDAD INFANTIL
#DE 13 A 17                 ESTAS EN LA ADOLESCENCIA
#DE 18 A 30                 ESTAS ES LA MADUREZ
#DE 31 A 60                 ERES ADULTO JOVEN
#DE 60 A MAS                ERES ADULTO MAYOR
edad= int(input(" Cuantos años tienes?: "))
if edad<=12:
    print(" Estas en la edad infantil: ")
elif edad>12 and edad<18:
    print("Estas en la adolescencia")
elif edad>=18 and edad<30:
    print(" Estas en la madurez ")
elif edad>=30 and edad<60:
    print(" Eres adulto joven ")
elif edad>=60:
    print("Eres adulto mayor")
print("Que tenga un buen día")