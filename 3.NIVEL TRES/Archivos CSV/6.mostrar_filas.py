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

# Comentario: Seleccionar y mostrar la primera fila del DataFrame
primera_fila = df_uno.head(1)
print(primera_fila)

# Comentario: Seleccionar y mostrar las dos primeras filas del DataFrame
primera_fila = df_uno.head(2)
print(primera_fila)

# Comentario: Seleccionar y mostrar las tres primeras filas del DataFrame
primera_fila = df_uno.head(3)
print(primera_fila)

# Comentario: Estas líneas utilizan el método "head()" para seleccionar y mostrar las primeras filas del DataFrame "df_uno".

# Comentario: Seleccionar y mostrar la ultima fila del DataFrame
primera_fila = df_uno.tail(1)
print(primera_fila)

# Comentario: Seleccionar y mostrar las dos ultimas filas del DataFrame
primera_fila = df_uno.tail(2)
print(primera_fila)

# Comentario: Seleccionar y mostrar las tres ultimas filas del DataFrame
primera_fila = df_uno.tail(3)
print(primera_fila)

# Comentario: Estas líneas utilizan el método "tail()" para seleccionar y mostrar las últimas filas del DataFrame "df_uno".
