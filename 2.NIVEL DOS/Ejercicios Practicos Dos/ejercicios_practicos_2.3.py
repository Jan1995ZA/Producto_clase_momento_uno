# Define una función llamada es_primo que verifica si un número dado es primo o no.
def es_primo(num):
    # Itera desde 2 hasta num-2 (exclusivo).
    for i in range(2, num-1):
        # Si num es divisible entre i (es decir, num % i es igual a 0), entonces no es primo.
        if num % i == 0:
            return False
    # Si no se encontraron divisores, el número es primo.
    return True

# Define una función llamada primos_hasta que encuentra todos los números primos hasta num.
def primos_hasta(num):
    # Inicializa una lista vacía llamada primos para almacenar los números primos encontrados.
    primos = []
    # Itera desde 3 hasta num (inclusive).
    for i in range(3, num+1):
        # Llama a la función es_primo para verificar si i es primo.
        resultado = es_primo(i)
        # Si es_primo retorna True, agrega i a la lista de primos.
        if resultado == True:
            primos.append(i)
    # Retorna la lista de números primos encontrados.
    return primos

# Solicita al usuario que ingrese un número y lo almacena en la variable num.
num = int(input("numero: "))

# Llama a la función primos_hasta para encontrar los números primos hasta el número ingresado.
resultado = primos_hasta(num)

# Imprime la lista de números primos encontrados.
print(resultado)
