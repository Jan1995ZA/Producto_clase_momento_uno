# Definición de una función llamada sumar_dos
def sumar_dos():
    # Se utiliza un bucle while True para solicitar números hasta que se ingrese una entrada válida
    while True:
        # Se solicita al usuario ingresar el primer número y se almacena en la variable 'a'
        a = input("Numero 1: ")
        # Se solicita al usuario ingresar el segundo número y se almacena en la variable 'b'
        b = input("Numero 2: ")
        
        try:
            # Se intenta sumar los números ingresados convirtiéndolos a enteros
            resultado = int(a) + int(b)
        except:
            # Si ocurre una excepción (por ejemplo, si no se ingresan números válidos), se muestra un mensaje de error
            print("Te pedí un número")  # Este bloque 'except' se ejecuta en caso de error
            
        else:
            # Si no se produce ninguna excepción, se sale del bucle 'while'
            break
        # La siguiente línea imprime un mensaje después de manejar la excepción (ya sea que ocurra o no)
        finally:
            print("\nManejo de excepcion finalizado\n")
            
    # Se retorna una cadena que contiene el resultado de la suma
    return f"El resultado de la suma es: {resultado}"

# Se llama a la función 'sumar_dos' y se imprime el resultado
print(sumar_dos())



#"ValueError": cuando se intenta convertir una cadena en un número entero utilizando la función int(), pero la cadena no representa un número válido
#"UnboundLocalError":es una excepción que se genera cuando intentas acceder o modificar una variable local que aún no ha sido inicializada dentro de la función donde se encuentra. 
# Esto puede ocurrir si intentas usar una variable antes de asignarle un valor o si intentas cambiar su valor sin haberla declarado como una variable global.
