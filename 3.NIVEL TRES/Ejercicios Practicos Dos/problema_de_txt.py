# Definimos dos listas con nombres y apellidos.
nombres = ["Juan", "Alejo", "Victor", "Melissa"]
apellidos = ["Zapata", "Arismendy", "Perez", "Peña"]

# Abrimos un archivo llamado "nombres_y_apellidos.txt" en modo escritura ("w") con la codificación UTF-8.
with open("nombres_y_apellidos.txt", "w", encoding="UTF-8") as archivo:
    # Escribimos una línea en el archivo que sirve como encabezado.
    archivo.writelines("los datos son:\n")
    
    # Utilizamos una comprensión de lista junto con la función zip para recorrer simultáneamente las listas de nombres y apellidos.
    # Luego, escribimos en el archivo los nombres y apellidos con el formato especificado.
    [archivo.writelines(f"\nNombre:{n}\nApellido:{a}\n--------------") for n, a in zip(nombres, apellidos)]
