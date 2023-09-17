# Lista:

numeros = [1,2,3,4,5,6,7,8,9,10]

multiplicar_por_dos = lambda x:x*2;  # lambda es una forma de crear una funcion anonima (que no tiene nombre) que podemos almacenar en variables.

print(multiplicar_por_dos(5)); 

# Beneficios de "lambda": 
# 1. lo podemos utilizar cuando queremos hacer algo simple y rapido,que retorne automaticamente.

# Crear una funcion comun que diga si es par o no:
def esPar (numero):
    if (numero%2==0):
        return True

# Usando "filter" como una funcion comun

numeros_pares = filter(esPar,numeros); 

print(list(numeros_pares)); 

# Crear una funcion comun que diga si es par o no: lambda
par = filter(lambda numero: numero%2==0,numeros); 

print(list(par)); 

