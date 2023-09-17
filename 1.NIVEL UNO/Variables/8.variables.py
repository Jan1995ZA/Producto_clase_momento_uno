#Definición de variable
#Las variables son una parte esencial de la programación en Python.
#Le permiten almacenar datos y reutilizarlos en todo su programa.
#Las variables se declaran y se definen.
#La diferencia entre las dos operaciones es que al asignarle un valor a una variable le decimos qué tipo de dato va a tener (string, int o float por ejemplo).
#Se pueden cambiar el valor asignado a las variables durante la ejecución del script

#Variables string
nombre="Juan"
apellido='Gonzalez'

#Variables numero
edad=34 #int
peso=78.6 #float
print("Edad: ", edad, "Peso:", peso)

#Variables booleano
estudiante=True
print('Estudiante:', estudiante )

#operadores de pertenencia
print ("Juan" in nombre)#in nos permite saber si existe o no dentro de una
print("Juan" not in nombre)#not in nos permite saber si no existe o si dentro de una

#f strins
print(f"{nombre} {apellido}") #f strins para concatenar (toma el dato y lo pasa a texto)

#operador
del nombre #del es un operador para borrar datos

#camelCase
miVariable = 10

#snake_case (Variables,Funciones,Metodos)
mi_variable2 = 'hola mundo'

