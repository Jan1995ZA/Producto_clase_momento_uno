
# Define una función llamada fibonacci que genera la secuencia de Fibonacci hasta un valor dado num.
def fibonacci(num):
    # Inicializa dos variables a y b con los valores iniciales de la secuencia de Fibonacci.
    a, b = 0, 1
    # Inicializa una lista llamada fibonacci_list con el primer valor de la secuencia (0).
    fibonacci_list = [a]
    # Itera desde 0 hasta num-1.
    for i in range(num):
        # Comprueba si la suma de a y b es mayor que num.
        if b > num:
            # Si es mayor, retorna la lista de la secuencia de Fibonacci hasta ese punto.
            return fibonacci_list
        else:
            # Si no es mayor, agrega b a la lista de Fibonacci.
            fibonacci_list.append(b)
            # Calcula el siguiente número en la secuencia y actualiza a y b.
            c = a + b
            a, b = b, c

# Llama a la función fibonacci con el valor 20 y almacena el resultado en la variable resultado.
resultado = fibonacci(20)

# Imprime la lista de la secuencia de Fibonacci generada.
print(resultado)
