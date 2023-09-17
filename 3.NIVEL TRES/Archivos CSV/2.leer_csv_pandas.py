# Importar la biblioteca Pandas y aliasarla como "pd"
import pandas as pd

# Comentario: Se imprime el tipo de objeto asociado a "pd" (que es Pandas)
#print(type(pd))

# Comentario: Crear un DataFrame (estructura de datos bidimensional)
# Leer un archivo CSV llamado "textos.csv" ubicado en la ruta especificada
df = pd.read_csv("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Archivos CSV\\textos.csv")

# Comentario: Imprimir el contenido del DataFrame (archivo leído)
print(f"{df}\n")
print(df["nombre"],f"\n")
print(df["apellido"],f"\n")
print(df["edad"],f"\n")

# Comentario: Leer el archivo CSV nuevamente con nombres de columnas personalizados
df = pd.read_csv("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Archivos CSV\\textos.csv", names=["name", "lastname", "age"])

# Comentario: Imprimir el contenido del DataFrame (archivo leído)
print(f"{df}\n")
print(df["name"],f"\n")
print(df["lastname"],f"\n")
print(df["age"],f"\n")

"6:28:15 / 8:06:29"