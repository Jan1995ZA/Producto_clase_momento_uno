# Hoy falto el profesor de clases y los chicos se oreganizaron para armar la suya propia 
# uno de los alumnos va a ser el profesor y otro va hacer su asistente
# a. pedir la edad y nombre de los compañeros que vinieron hoy a clases y ordenar los datos de menor a mayor.
# b. El mayor de la clase es el profesor y el menor es el aisitente: ¿Quien es quien?
# 
# # 

def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []; # Lista 

    for i in range(cantidad_de_compañeros):
        nombre = input("Ingresa el nombre del alumno: "); 
        edad = int(input("Ingresa la edad del alumno: ")); 
        compañero = (nombre,edad); #tupla
        compañeros.append(compañero); #APPEND - agrega un elemento al final de la lista
        print(compañero); 
    compañeros.sort(key = lambda x:x[1]); #la edad es el segundo parametro y el orden esta determinado por este.. esto hace que coloquemos 1

    asistente = compañeros[0][0]; 
    profesor =  compañeros[-1][0]; 
    return asistente,profesor; 


asistente , profesor=obtener_compañeros(5); 
print(f"El asistente es: {asistente} Y el Profesor es:{profesor}"); 
