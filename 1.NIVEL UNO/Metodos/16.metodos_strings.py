#metodos son funciones que se utilizan en POO 
#nombre_de_la_funcion(parametros)
#ejemplo print(parametro) y type(parametro)
#Nota: asi funciona los metodos DATO.METODO()
cadena_uno = "Hola,soy,Juan"
cadena_dos = "Maquina"

#UNA FUNCION
#DIR - devuelve la lista de atributos validos del objeto pasado.
resultado_uno =dir(cadena_uno)
print (resultado_uno)#devuelve una lista con los nombres de todos los metodos,

#CONVIERTEN LA CADENA DE TEXTO
#UPPER - toma el texto y lo pasa a mayuscula
resultado_dos = cadena_uno.upper()
print(resultado_dos)

#LOWER - toma el texto y lo pasa a minuscula
resultado_tres = cadena_uno.lower()
print(resultado_tres)

#CAPITALIZE - toma el texto y pasa la primer letra en mayuscula.
resultado_cuatro= cadena_uno.capitalize() #se puede poner solo capital
print(resultado_cuatro)

#BUSCAN UN VALOR
#FIND - busca una cadena dentro de otra cadena (False = -1)
resultado_cinco = cadena_uno.find("J")   #(posicion donde empieza la palabra)
print(resultado_cinco)

#INDEX - busca una cadena dentro de otra cadena (False = sale error)
resultado_seis = cadena_uno.index("J")
print(resultado_seis)

#COMPARA Y BUSCA
#ISNUMERIC - si es numerico "4" o 4 devuelve True de lo contrario False
resultado_siete = cadena_uno.isnumeric()
print(resultado_siete)

#ISALPHA - si es alfanumerico desde la a-z (no puede contar con espacios) devuelve True de lo contrario False
resultado_ocho = cadena_uno.isalpha()
print(resultado_ocho)

#COUNT - Nos dice cuantas veces encontro una concidencia
resultado_nueve = cadena_uno.count('a')    #en este caso
print(resultado_nueve)

#FUNCION
#LEN - Cantidad de caracteres que tiene una cadena [0,1,2,3..]
resultado_diez = len(cadena_uno)       ##la cantidad de caracteres
print(resultado_diez)

#ENDSWITH - Verifica si una cadena termia con una cadena dada.
resultado_once = cadena_uno.endswith("n")
print(resultado_once)

#STARTSWITH - Verifica si una cadena empieza con una cadena dada.
resultado_doce = cadena_uno.startswith("H")     ###empieza por
print(resultado_doce)

#REPLACE - remplaza un fracmento de la cadena por otro dato (dos parametros)
resultado_trece = cadena_uno.replace(","," ")
print(resultado_trece)

#SPLIT - nos devuelve una matriz (lista)
resultado_catorce = cadena_uno.split(",")
print(resultado_catorce)


