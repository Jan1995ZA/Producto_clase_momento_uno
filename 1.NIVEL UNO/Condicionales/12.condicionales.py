#Condicionales
##Que son los condicionales?
#Los condicionales son instrucciones que le permiten controlar el flujo de su programa. 
# Se utilizan para verificar ciertas condiciones y luego ejecutar diferentes códigos según el resultado.
###########################
#La instrucción condicional más básica en Python es la instrucción if. 
# La sintaxis de una instrucción if es la siguiente:

"""if <condición>:
  <código>
​"""
#La condición es una expresión booleana que evalúa a verdadero o falso. 
# Si la condición es verdadera, se ejecutará el código dentro del bloque if. 
# Si la condición es falsa, se omitirá el código dentro del bloque if.
###########################
#También puede usar la instrucción else para especificar qué código debe ejecutarse si la condición es falsa. 
# La sintaxis de la instrucción else es la siguiente:

"""if <condición>:
  <código>
else:
  <código>"""
#La instrucción else es opcional. 
#Si no incluye una instrucción else, se ejecutará el código después de la instrucción if si la condición es falsa.

###########################
#También puede usar la instrucción elif para verificar varias condiciones. 
#La sintaxis de la instrucción elif es la siguiente:

"""if <condición1>:
  <código>
elif <condición2>:
  <código>
...
else:
  <código>
​"""
#Las instrucciones elif se verifican en orden. 
# Si la primera condición es verdadera, se ejecutará el código dentro del primer bloque if. 
# Si la primera condición es falsa, se verificará la segunda condición. 
# Este proceso continúa hasta que una condición sea verdadera o todas las condiciones sean falsas. 
# Si todas las condiciones son falsas, se ejecutará el código dentro del bloque else.

#Los condicionales son una herramienta poderosa que se puede utilizar para controlar el flujo de su programa. 
# Se pueden utilizar para hacer que sus programas sean más eficientes y evitar errores.