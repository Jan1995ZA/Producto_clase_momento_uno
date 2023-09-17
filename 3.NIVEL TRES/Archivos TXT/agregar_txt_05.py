# Abre un archivo de texto ubicado en la ruta especificada en modo "a" (append).
# El modo "a" permite agregar contenido al final del archivo sin sobrescribir su contenido existente.
# Se utiliza el parámetro 'encoding="UTF-8"' para asegurar la correcta lectura de caracteres especiales en codificación UTF-8.
# La estructura 'with' garantiza que el archivo se cierre automáticamente después de su uso.
with open("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Archivos\\4.1.archivos.txt", "a", encoding="UTF-8") as archivo:
    # Escribe las cadenas "bebe hermosa juana" y "misertddrf" en el archivo utilizando 'writelines'.
    archivo.writelines(["bebe hermosa juana\n", "misertddrf"])
    for i in range(5):
        archivo.write(f"{i}. hola mundo\n")
# No requiere cerrar el archivo ya que la estructura 'with' se encarga automáticamente de cerrarlo.
