# Importar la biblioteca Pandas y aliasarla como "pd"
import pandas as pd

# Comentario: La línea anterior importa la biblioteca Pandas y le asigna un alias "pd" para facilitar su uso.

# Comentario: Se imprime el tipo de objeto asociado a "pd" (que es Pandas)
#print(type(pd))

# Comentario: Esta línea imprime el tipo de objeto que representa "pd". En este caso, imprimirá "<class 'pandas.core.module.Module'>".

# Comentario: Crear un DataFrame (estructura de datos bidimensional)
# Leer un archivo CSV llamado "textos.csv" ubicado en la ruta especificada
df_uno = pd.read_csv("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Archivos CSV\\textos.csv")

# Comentario: En esta línea, se lee un archivo CSV llamado "textos.csv" y se carga en un DataFrame llamado "df_uno".

# Comentario: Obtener el número total de filas y columnas del DataFrame "df_uno"
filas_y_columnas_totales = df_uno.shape

# Comentario: La variable "filas_y_columnas_totales" contiene una tupla con dos valores: (número de filas, número de columnas)

# Comentario: Imprimir el número total de filas del DataFrame
filas_totales = filas_y_columnas_totales[0]
print(filas_totales)

# Comentario: Imprimir el número total de columnas del DataFrame
columnas_totales = filas_y_columnas_totales[1]
print(columnas_totales)

# Desempaquetar el resultado de shape en las variables filas y columnas
filas, columnas = filas_y_columnas_totales

# Comentario: En esta línea, el resultado de la función shape, que es una tupla (número de filas, número de columnas), se desempaqueta en las variables filas y columnas.

# Comentario: Imprimir el número total de filas del DataFrame
print(filas)

# Comentario: Imprimir el número total de columnas del DataFrame
print(columnas)
