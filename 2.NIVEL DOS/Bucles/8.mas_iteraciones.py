#lista
frutas = ["banana","pera","ciruela","granada","naranja"]; 


# Evitando que se coma una manzana con la sentencia "continue"
for fruta in frutas:
    if fruta == 'naranja':
        print(f'no me grusta la {fruta}'); 
        continue
    print(f'me voy a comer una {fruta}'); 
else:
    print('Termino de comer'); 
print("\n")

# Evitando que continue el bucle cuando se come una fruta que le cae mal con la sentencia "break".
for fruta in frutas:
    if fruta == 'ciruela':
        print(f'le dio malestar la {fruta} debe parar de comer por un tiempo'); 
        break
    print(f'se va comer una {fruta}'); 

print('Termino de comer'); 
print("\n")

# Iterar una cadena de texto 

cadenas = "Hola mundo"

for cadena in cadenas:
    print(cadena); 
    
print('Termino'); 
print("\n")


#for en varias lineas de codigo "duplicar la cantidad"
numeros = [2,5,8,10]; 
numeros_duplicados = list(); 

for numero in numeros:
    numeros_duplicados.append(numero*2); #En Python, el método "append()" se utiliza en listas para agregar un elemento al final
    # de la lista existente. Ayuda a ampliar la lista añadiendo un nuevo elemento al final de la misma. 
    # Este método es útil cuando se quieren almacenar o modificar datos en una lista de forma dinámica.
    
print(f'Antes: {numeros}'); 
print(f'Despues: {numeros_duplicados}'); 

print('Termino'); 
print("\n")

#for en una sola linea de codigo "duplicar la cantidad"

    
numeros_duplicados_2 = [x*2 for x in numeros]; 

print(f'Antes: {numeros}'); 
print(f'Despues: {numeros_duplicados_2}');  

print('Termino'); 
print("\n")

print(type(numeros_duplicados_2)); 


