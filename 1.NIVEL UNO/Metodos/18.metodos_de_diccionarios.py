diccionario = {
    "nombre": 'Juan',
    "apellido":'Perez',
    "salario": 20_000_000
}

#KEYS() - devuelve las claves de la tabla (tambien nos sirve para iterar)
claves = diccionario.keys()
print(claves)

#GET() - devuelve el valor de una clave en particular
valor_de_nombre = diccionario.get("nombre")
print(valor_de_nombre)

#CLEAR() - elimina todos los elementos de la tabla
#diccionario.clear()
#print(diccionario)

#POP() - elimina un elemento ovarios
diccionario.pop("nombre")
print(diccionario)

#ITEMS() - para iterar el dict (iterar es recorrer el elemento)
diccionario_iterable = diccionario.items()
print(diccionario_iterable)