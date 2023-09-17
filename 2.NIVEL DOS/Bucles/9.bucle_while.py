# While:Los bucles while se utilizan en Python para repetir un bloque de código varias veces. 
# La declaración `while` toma un único argumento, que es una expresión booleana. 
# El bucle seguirá ejecutando el bloque de código mientras la expresión se evalúe como `True`.
# Por ejemplo, el siguiente código imprimirá los números del 1 al 10:

i = 1; 

while i <= 10:
    
  print(i); 
  i += 1; 

print("\n"); 
  
# El bucle `while` también puede utilizarse para iterar sobre una secuencia de valores. 
# Por ejemplo, el siguiente código imprimirá cada elemento de la lista `numbers`:
numbers = [1, 2, 3, 4, 5]; 

i = 0; 

while i < len(numbers):
    
  print(numbers[i]); 
  i += 1; 

print("\n"); 

# El bucle `while` es una herramienta poderosa que puede utilizarse para repetir un bloque de código varias veces. 
# Es importante tener en cuenta que el bucle `while` seguirá ejecutando el bloque de código incluso si la expresión se evalúa como `False`. 
# Esto puede dar lugar a bucles infinitos, por lo que es importante utilizar el bucle `while` con cuidado.

# El for recorre elementos mientras que el whilw se va a ejecutar siempre que una condición sea real.
