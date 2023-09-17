# El timing para ver los conceptos vistos en Python en un curso de corrido es de  2.5 horas como minimo, 
# 7 horas como maximo y 4 horas en promedio. Este curso lo logro en una hora y media.
# a. Diferencia en porcentaje entre el curso actual y el mas rapido de los otros cursos, el mas lento y el promedio.
# b. Teniendo encuenta que la cantidad de crudo en promedio de los demas cursos es de 5 horas y editados los convierten en 4 horas,
# y el curdo de este video fue de 3 horas y media y se redujo a 1 hora y media. ¿Que % de material inservible,material vacio en
# definitiva, se reduce del crudo en ambos casos?
# c. Ver 10 horas de este curso seria equivalete a ver cuantas horas de otros cursos y al contrario.

#Primero sacamos los datos:
## Cantidad de horas
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
este_curso = 1.5

diferencia_porcentaje_min = (1-(este_curso/otros_cursos_min))*100
diferencia_porcentaje_max = 100-(este_curso*1000//otros_cursos_max/10)
diferencia_porcentaje_promedio = (1-(este_curso/otros_cursos_promedio))*100

print(f"Este curso dura el {diferencia_porcentaje_min} % menos del mas corto")
print(f"Este curso dura el {diferencia_porcentaje_max} % menos del mas largo")
print(f"Este curso dura el {diferencia_porcentaje_promedio} % menos que el promedio")
print("Punto 'a' Listo \n")
print("##########################################################")
##################
## Crudo promedio

otros_cursos_crudo = 5
otros_cursos_editados = 4

este_curso_crudo = 3.5
este_curso_editado = 1.5

material_inservible_otros_cursos = 100-(otros_cursos_editados*1000//otros_cursos_crudo/10)
material_inservible_este_curso = 100-(este_curso_editado*1000//este_curso_crudo/10)

print(f"El % de material inservible y eliminado de otros cursos es del {material_inservible_otros_cursos} %")
print(f"El % de material inservible y eliminado de este cursos es del {material_inservible_este_curso} %")
print("Punto 'b' Listo \n")
print("##########################################################")

##################
## ver 10 horas a cuanto equivale del promedio
horas_equivalente_este_curso = ((otros_cursos_promedio*100)//este_curso)/10

horas_equivalente_otros_curso = ((este_curso*100)//otros_cursos_promedio)/10

print(f"Ver 10 horas de este curso seria equivalete a ver {horas_equivalente_este_curso} h de otro ")
print(f"Ver 10 horas de otro curso seria equivalete a ver {horas_equivalente_otros_curso} h de este ")
print("Punto 'c' Listo \n")
print("##########################################################")

