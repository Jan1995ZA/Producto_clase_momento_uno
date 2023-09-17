# un bucle es repetir de forma controlada la ejecución de un codigo
## Que es iterar un elemento?Iterar es el proceso de recorrer un elemento o un conjunto de elementos de una colección de datos. En Python, existen diferentes formas de iterar un elemento, dependiendo del tipo de elemento que se desea recorrer.

## Iterar una lista
###se puede utilizar el bucle `for` con la función `range()` y el índice de la lista.
my_list = [1, 2, 3, 4, 5]; 

for i in range(len(my_list)):
    print(my_list[i]);  # Este código imprimirá los elementos de la lista en orden, empezando desde el índice 0 y terminando en el índice `len(my_list)-1`.

## Iterar un diccionario 
### se puede utilizar el bucle `for` con las claves del diccionario.
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key in my_dict:
    print(key, my_dict[key]) # Este código imprimirá las claves y valores del diccionario en paralelo.

## Iterar un conjunto
###se puede utilizar el bucle `for` con las claves del conjunto.
my_set = {1, 2, 3, 4, 5}

for element in my_set:
    print(element) #Este código imprimirá todos los elementos del conjunto

## Iterar una cadena
### se puede utilizar el bucle `for` con la función `range()` y el índice de la cadena
my_string = "hello world"

for i in range(len(my_string)):
    print(my_string[i]) # Este código imprimirá cada caracter de la cadena en orden, 
                        # empezando desde el índice 0 y terminando 
                         # en el índice `len(my_string)-1`.