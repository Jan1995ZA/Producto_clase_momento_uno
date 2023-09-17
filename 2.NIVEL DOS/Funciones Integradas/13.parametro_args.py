# Datos por el usuario:
"""
a = int(input("Ingresa el primer numero: ")); 
b = int(input("Ingresa el segundo numero: ")); 
"""

# forma  sumar valores con funciones:
"""
def sum(a,b):
    return a+b,a,b

resultado,primer_numero,segundo_numero = sum(a,b); 

print(f"El valor de a es '{primer_numero}' y el valor de b es '{segundo_numero}': la suma de estos dos es igual a '{resultado}'")
"""
# utilizar el parametro "args" en la funcion suma: el parametro args se debe utilizar al final siempre 
"""
def suma(*numeros):
    return sum(numeros); # funcion que suma los numeros de una lista

resultado = suma(4,5,6,7,9); 

print(f'El resultado es igual a "{resultado}"'); 
   """  
# utilizar el parametro "args" en la funcion suma: el parametro args se debe utilizar al final siempre 
"""
def suma(nombre,*numeros):
    return f"{nombre}, la suma es: {sum(numeros)}"; # funcion que suma los numeros de una lista

resultado = suma("Juan",4,5,6,7,9); 

print(f'El resultado es igual a "{resultado}"'); """


# funcion mas utilizada para rellenar datos parametro "args":

def suma_t(nombre,numeros):
    return sum([*numeros]),nombre

resultado,nombre = suma_t("Juan",[4,7,6,7,9]); 

print(f'El resultado es igual a "{resultado}" {nombre}'); 

