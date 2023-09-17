# Abre un archivo de texto ubicado en la ruta especificada.
# Se utiliza el parámetro 'encoding="UTF-8"' para asegurar la correcta lectura de caracteres especiales en codificación UTF-8.
archivo_sin_leer = open("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Archivos\\4.1.archivos.txt", encoding="UTF-8") # El método open() es una función incorporada en Python que se utiliza para abrir archivos.

# Lee todo el contenido del archivo y lo almacena en la variable 'archivo'.
archivo = archivo_sin_leer.read() # Cuando se llama al método read() sin un argumento, se lee todo el contenido del archivo desde la posición actual del puntero de lectura hasta el final del archivo.

# Imprime el contenido del archivo en la consola.
print(archivo)

# Cierra el archivo después de su uso para liberar recursos.
archivo_sin_leer.close()

# Se utiliza el parámetro 'encoding="UTF-8"' para asegurar la correcta lectura de caracteres especiales en codificación UTF-8.
archivo_sin_leer = open("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Archivos\\4.1.archivos.txt", encoding="UTF-8") # El método open() es una función incorporada en Python que se utiliza para abrir archivos.

# Lee todas las líneas del archivo y las almacena en la lista 'lineas'.
lineas = archivo_sin_leer.readlines()

# Imprime la lista de líneas.
print(lineas)

# Cierra el archivo después de su uso para liberar recursos.
archivo_sin_leer.close()

# Se utiliza el parámetro 'encoding="UTF-8"' para asegurar la correcta lectura de caracteres especiales en codificación UTF-8.
archivo_sin_leer = open("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Archivos\\4.1.archivos.txt", encoding="UTF-8") # El método open() es una función incorporada en Python que se utiliza para abrir archivos.

# Lee una sola línea del archivo y la almacena en la variable 'linea'.
linea = archivo_sin_leer.readline()

# Imprime la línea leída.
print(linea)

# Cierra el archivo después de su uso para liberar recursos.
archivo_sin_leer.close()
