# Desempaquetado de variable: Es una forma de python de asignarle variables de una forma bastante particular.

#Creando una tupla
datos_tupla = ("Lucas","Dalton",1_000_000);
#Creando una lista
datos_lista = ["Juan","Dalton",1_000_000];


#desempaquetado
nombre,apellido,suscriptores = datos_tupla;
nombre,apellido,suscriptores=datos_lista;
#mostrar resultado
print(nombre);
print(apellido);
print(suscriptores);

#El encapsulamiento solo funciona solamente si la cantidad de variables que ponene es igual a la cantidad de datos que tiene el arreglo.



