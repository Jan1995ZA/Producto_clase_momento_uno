#Datos compuestas: son datos que adentro tienen datos simples o otro datos compuestos que pidemos agrupar.
#Ejemplo de dato compuesto: un objeto con varios campos, cada campo puede ser simple o compuesto por mas campos.

#Tipos de datos compuestos: listas, tuplas y diccionarios.

#Se puden modificar (Lista)
lista = [
    10,
    'a',
    True
    ] #[int, str , bool ]
print(type([0]))
print(lista[0])

#No se pueden modificar (tupla)
tupla= (
    23456789,
    "abc",
    False
    ) #(int,str,bool)
print(type((1)))
print(tupla[1])

#conjunto set: se puede redefinir, pero no se puede cambiar el elemento.
#no se pude accerder por el indice a un elemento del conjunto.
#no puedo repetir valores.
#para acceder a cada elemento se puede utilizar un bucle.
set_ = {
    1,
    'a',
    'b'
}
print(type({}))
print(set_)

#diccionario: es un JSON en este la clave es el nombre del elmento definido.
dicc={
    'nombre':'Juan', 
    "apellido":"Perez"
    }
print(type({}))
print(dicc['nombre'])
print(dicc)
#################################################
print(type(lista)) #listas
print(type(tupla)) #tuplas 
print(type(dicc)) #diccionarios