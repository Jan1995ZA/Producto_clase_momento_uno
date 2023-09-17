# Importar la biblioteca Pandas y aliasarla como "pd"
import pandas as pd

# Comentario: La línea anterior importa la biblioteca Pandas y le asigna un alias "pd" para facilitar su uso.

# Comentario: Se imprime el tipo de objeto asociado a "pd" (que es Pandas)
#print(type(pd))

# Comentario: Esta línea imprime el tipo de objeto que representa "pd". En este caso, imprimirá "<class 'pandas.core.module.Module'>".

# Comentario: Crear un DataFrame (estructura de datos bidimensional)
# Leer un archivo CSV llamado "textos.csv" ubicado en la ruta especificada
df_uno = pd.read_csv("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Archivos CSV\\textos.csv")

df_info = df_uno.describe()

print(df_info)