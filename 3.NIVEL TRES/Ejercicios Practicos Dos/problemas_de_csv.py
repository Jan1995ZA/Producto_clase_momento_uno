# Importamos la biblioteca pandas y la renombramos como pd para abreviar.
import pandas as pd

# Cargamos un archivo CSV en un DataFrame llamado 'df'.
df = pd.read_csv("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Archivos CSV\\textos.csv")

# Imprimimos el contenido del DataFrame 'df'.
print(df)

# Accedemos a la columna 'edad' y mostramos el valor en la primera fila.
print(df['edad'][0])

# Mostramos el tipo de dato del valor en la primera fila de la columna 'edad'.
print(type(df['edad'][0]))

# Convertimos la columna 'edad' a tipo de dato str (cadena).
df['edad'] = df['edad'].astype(str)

# Mostramos el valor en la primera fila de la columna 'edad' después de la conversión.
print(df['edad'][0])

# Mostramos el tipo de dato del valor en la primera fila de la columna 'edad' después de la conversión.
print(type(df['edad'][0]))

# Convertimos la columna 'edad' a tipo de dato float (número decimal).
df['edad'] = df['edad'].astype(float)

# Mostramos el valor en la primera fila de la columna 'edad' después de la segunda conversión.
print(df['edad'][0])

# Mostramos el tipo de dato del valor en la primera fila de la columna 'edad' después de la segunda conversión.
print(type(df['edad'][0]))


remplace = df['nombre'].replace("Juan","Maestro")

print(remplace)

df = df.dropna()

print(df)

df = df.drop_duplicates()

df.to_csv("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Archivos CSV\\dato_textos.csv")

print(df)

"6:54:22 / 8:06:29"