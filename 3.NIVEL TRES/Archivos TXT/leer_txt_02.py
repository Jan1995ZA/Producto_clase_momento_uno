# Abre un archivo de texto ubicado en la ruta especificada.
# Se utiliza el parámetro 'encoding="UTF-8"' para asegurar la correcta lectura de caracteres especiales en codificación UTF-8.
# La estructura 'with' garantiza que el archivo se cierre automáticamente después de su uso.
with open("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Archivos\\4.1.archivos.txt", encoding="UTF-8") as archivo:
    # Lee todo el contenido del archivo y lo almacena en la variable 'contenido'.
    contenido = archivo.read()
    
    # Imprime el contenido del archivo en la consola.
    print(contenido)
#No requiere cerrar el archivo.

"6:07:31 / 8:06:29"
