import csv

# Abre un archivo CSV ubicado en la ruta especificada.
with open("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Archivos CSV\\textos.csv") as archivo:
    # Crea un lector CSV para el archivo.
    reader = csv.reader(archivo)
    
    # Itera a través de las filas del archivo CSV.
    for row in reader:
        # Imprime cada fila en la consola.
        print(row)
