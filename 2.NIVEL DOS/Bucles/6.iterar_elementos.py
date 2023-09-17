##################################
#        listas y tuplas         #                 
##################################
##Que es un for in?
# El bucle for en Python es una estructura de control que se utiliza para iterar sobre una secuencia de elementos. 
# El bucle for se utiliza para realizar la misma operación en cada elemento de la secuencia. 
# La sintaxis del bucle for es la siguiente:

#for elemento in secuencia:
    #instrucción(es)
    
# donde `secuencia` es una secuencia de elementos y `instrucción(es)` es la instrucción(es) que se ejecutará para cada elemento
# de la secuencia.

animales = ["perro","gato","loro","cocodrilo"]; #lista con cuatro elementos

#¿como iteramos la lista animales (recorrer cada elemento)?

# animal = elemento ejm "perro"
# animales = secuencia ejm "Lista"

# recorriendo la lista animales

numeros = [5,6,3,4];  

for animal in animales:
    print(f"el valor de animal es: {animal}");
    
print("\n"); 

for numero in numeros:
    resultado_numero = numero*10; 
    print(f"el valor es: {resultado_numero}");
    
print("\n"); 


#fors anidados: la fincion zip nos permite como parametro recorre mas de una lista

nombres = ["Juan","Maria","Josue","Manuela"]; 

for numero,animal,nombre in zip(animales,numeros,nombres):
    print(f"Recorriendo la lista 1: {numero}"); 
    print(f"Recorriendo la lista 2: {animal}"); 
    print(f"Recorriendo la lista 3: {nombre}"); 
    
print("\n");  
# iterar con funcion range()

for n in range(5,10): #(No funciona en conjuntos)
    print(f"{n}"); 
    
print("\n"); 

#con len() podemos tener el numero de elememtos de una lista

#elementos = len(numeros); 
#print(elementos); 

#forma no correcta
for num in range(len(numeros)): #(No funciona en conjuntos)
    print(numeros[num]); 
    
print("\n"); 

#forma correcta es con la funcion enumerata()
for num in enumerate(numeros):
    
    #print(num); 
    #print(type(num)); 
    #################
    indice = num[0]; 
    valor = num[1]; 
    #print(indice); 
    print(valor); 
    
print("\n"); 

#usando el "else"

for numero in numeros:
    print("Ejacutando el ultimo bucle, valor actual: "); 
else:
    print("El bucle termino"); 

print("\n"); 

# Esto funciona igual para tuplas:
tupla_de_animales= ("Perro", "Gato", "Caballo")
for animals in tupla_de_animales :
    print (animals)
else:
    print("El bucle termino");  
    
print("\n"); 

##################################
#           Conjuntos            #                 
##################################

animales = {"perro","gato","loro","cocodrilo"}; #conjunto con cuatro elementos

numeros = {5,6,3,4};  

nombres = {"Juan","Maria","Josue","Manuela"}; 

for animal in animales:
    print(f"el valor de animal es: {animal}");
    
print("\n"); 

for numero in numeros:
    resultado_numero = numero*10; 
    print(f"el valor es: {resultado_numero}");
    
print("\n"); 

#fors anidados: la fincion zip nos permite como parametro recorre mas de una conjunto
for numero,animal,nombre in zip(animales,numeros,nombres):
    print(f"Recorriendo la conjunto 1: {numero}"); 
    print(f"Recorriendo la conjunto 2: {animal}"); 
    print(f"Recorriendo la conjunto 3: {nombre}"); 
    
print("\n");  

#forma correcta es con la funcion enumerate()
for num in enumerate(numeros):
    
    #print(num); 
    #print(type(num)); 
    #################
    indice = num[0]; 
    valor = num[1]; 
    print(f"{indice}:{valor}"); 
    
    
    
print("\n"); 

#usando el "else"

for numero in numeros:
    print("Ejacutando el ultimo bucle, valor actual: "); 
else:
    print("El bucle termino"); 

print("\n"); 

