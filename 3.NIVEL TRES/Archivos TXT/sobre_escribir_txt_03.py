# Abre un archivo de texto ubicado en la ruta especificada.
# Se utiliza el parámetro 'encoding="UTF-8"' para asegurar la correcta lectura de caracteres especiales en codificación UTF-8.
# La estructura 'with' garantiza que el archivo se cierre automáticamente después de su uso.
with open("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Archivos\\4.1.archivos.txt", "w", encoding="UTF-8") as archivo:
    # Escribe la cadena "jajajajaj bebe hermosa" en el archivo y almacena la cantidad de caracteres escritos en la variable 'contenido'.
    contenido = archivo.write("jajajajaj bebe hermosa")

# No requiere cerrar el archivo ya que la estructura 'with' se encarga automáticamente de cerrarlo.
