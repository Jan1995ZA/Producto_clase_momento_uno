# Importar la biblioteca Pandas y aliasarla como "pd"
import pandas as pd

# Comentario: Se imprime el tipo de objeto asociado a "pd" (que es Pandas)
#print(type(pd))

# Comentario: Crear dos DataFrames (estructuras de datos bidimensionales)
# Leer dos archivos CSV llamados "textos.csv" ubicados en la misma ruta especificada
df_uno = pd.read_csv("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Archivos CSV\\textos.csv")
df_dos = pd.read_csv("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Archivos CSV\\textos.csv")

# Comentario: Concatenar los dos DataFrames en uno solo
df_concatenado = pd.concat([df_uno, df_dos])

# Imprimir el DataFrame concatenado
print(f"{df_concatenado}\n")

# Comentario: Ordenar el DataFrame concatenado por la columna "edad"
ordenado = df_concatenado.sort_values("edad")

# Imprimir el DataFrame ordenado por edad
print(ordenado)
