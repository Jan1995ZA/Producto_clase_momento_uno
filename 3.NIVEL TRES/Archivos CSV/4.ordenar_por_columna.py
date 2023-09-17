# Importar la biblioteca Pandas y aliasarla como "pd"
import pandas as pd

# Comentario: Se imprime el tipo de objeto asociado a "pd" (que es Pandas)
#print(type(pd))

# Comentario: Crear un DataFrame (estructura de datos bidimensional)
# Leer un archivo CSV llamado "textos.csv" ubicado en la ruta especificada
df = pd.read_csv("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Archivos CSV\\textos.csv")

# Comentario: Imprimir el contenido del DataFrame (archivo leído)

# Seleccionar la columna "nombre" del DataFrame y almacenarla en la variable "nombres"
nombres = df["nombre"]

# Ordenar el DataFrame por la columna "edad" de forma ascendente
df_ordenado = df.sort_values("edad")

# Imprimir el DataFrame original
print(f"{df}\n")

# Imprimir el DataFrame ordenado por edad de forma ascendente
print(f"{df_ordenado}\n")

# Ordenar el DataFrame por la columna "edad" de forma descendente
df_ordenado = df.sort_values("edad", ascending=False)

# Imprimir el DataFrame ordenado por edad de forma descendente
print(df_ordenado)
