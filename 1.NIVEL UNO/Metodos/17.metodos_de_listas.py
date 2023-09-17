#Metodos de listas

#LIST - crear una lista (funcion) - toma como parametro una lista 

lista = list(["Hola","Juan",34])
print(lista)

#LEN - cuenta la cantidad de elementos de una lista (funcion) 
# antes lo trabajamos para mirar la cantidad de caracteres de un string, ahora lo aplicamos para mirar la cantidad de elemnetos.

resultado = len(lista)
print(resultado)

#APPEND - agrega un elemento al final de la lista
lista.append("Zapata")
print(lista)

#INSERT - agrega un elemento al final de la lista en el indice especificado (como parametro primero es la pos y luego el elemento)
lista.insert(2,"Arismendy")
print(lista)

#EXTEND - agrega varios elementos a la lista toma como parametro una lista 
lista.extend(["Hermano",20])
print(lista)

#POP - elimina y regresa el ultimo elemento de la lista
lista.pop(0)
print(lista)

#REMOVE - remueve el primer elemento que coincida con el valor pasado como parametro. 
# Si no encuentra ningun elemento, genera error
lista.remove('Arismendy')
print(lista)

#CLEAR - elimina todos los elemetos de una lista
#lista.clear()
#print(lista)

#SORT - ordena una lista de forma ascendente a descendente o viceversa - no funciona si tiene cadena de textos str
lista = list([1,6,5,9,7,4,True,False])
lista.sort()
#lista.sort(reverse=True)
print(lista)

#REVERSE - invierte el orden de las posiciones de cada elemento dentro de una lista (no ordena)
lista.reverse()
print(lista)

##########
print(dir(lista))
