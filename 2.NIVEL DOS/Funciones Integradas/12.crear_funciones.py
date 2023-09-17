# Crear funciones

#creando una funcion simple:

"""
def saludar():
    print("Hola"); 

saludar(); 
saludar(); 
"""

# Creando una funcion con parametros: un paramtro es una variable que se crea para poder utilizarlas en una funcion.

"""
def saludar(nombre,sexo):
    sexo = sexo.lower();  # lower es un metodo que convierte todo a minuscula.
    if sexo == "mujer":
        adjetivo = "maestra"; 
        print(f"Hola {nombre}, {adjetivo} como estas ?"); 
    elif sexo == "hombre":
        adjetivo = "maestro"; 
        print(f"Hola {nombre}, {adjetivo} como estas ?"); 
    else:
        adjetivo = "amor"; 
        print(f"Hola {nombre}, {adjetivo} como estas ?"); 
        
saludar("Juan","Hombre"); 
saludar("Juan","Mujer"); 
saludar("Juan","Otro"); 
"""
# Crear un funcion que retorne valores:
"""
def crear_contraseña_randon(num):
    chars = "abcdefghij"; 
    numero_entero = str(num); #convertir el primer numero str
    num = int(numero_entero[0]); 
    c1 = num-2; 
    c2 = num; 
    c3 = num-5; 
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{numero_entero*2}"; 
    #print(contraseña); 
    return contraseña # nos permite guardar el valor en una variable y si queremos podemos mostrar el dato al usuario o no .

password = crear_contraseña_randon(12); 
print(password); 
print(type(password)); 
"""
# Crear un funcion que retorne multiples valores:
"""
def crear_contraseña_randon(num):
    chars = "abcdefghij"; 
    numero_entero = str(num); #convertir el primer numero str
    num = int(numero_entero[0]); 
    c1 = num-2; 
    c2 = num; 
    c3 = num-5; 
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{numero_entero*2}"; 
    #print(contraseña); 
    return contraseña,num # nos permite guardar el valor en una variable y si queremos podemos mostrar el dato al usuario o no .
# desempaquetando la funcion
password,primer_numero = crear_contraseña_randon(12); 

# Obteniendo los datos utilizados
print(password); 
print(primer_numero); 
"""





