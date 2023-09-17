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

# Comentario: Seleccionar y mostrar un elemento específico del DataFrame usando la función loc.
elemento_esp_loc = df_uno.loc[2, "edad"]

# Comentario: El código anterior selecciona el valor en la fila 2 y la columna "edad" del DataFrame.
print(elemento_esp_loc)

# Comentario: Seleccionar y mostrar otro elemento específico del DataFrame usando la función loc.
elemento_esp_loc = df_uno.loc[1, "edad"]

# Comentario: El código anterior selecciona el valor en la fila 1 y la columna "edad" del DataFrame.
print(elemento_esp_loc)

# Comentario: Seleccionar y mostrar otro elemento específico del DataFrame usando la función loc.
elemento_esp_loc = df_uno.loc[0, "edad"]

# Comentario: El código anterior selecciona el valor en la fila 0 y la columna "edad" del DataFrame.
print(elemento_esp_loc)


# Comentario: Seleccionar y mostrar un elemento específico del DataFrame usando la función iloc.
elemento_esp_iloc = df_uno.iloc[2, 2]

# Comentario: El código anterior selecciona el valor en la fila 2 y la columna 2 del DataFrame.

print(elemento_esp_iloc)

# Comentario: Seleccionar y mostrar otro elemento específico del DataFrame usando la función iloc.
elemento_esp_iloc = df_uno.iloc[2, 1]

# Comentario: El código anterior selecciona el valor en la fila 2 y la columna 1 del DataFrame.
print(elemento_esp_iloc)

# Comentario: Seleccionar y mostrar otro elemento específico del DataFrame usando la función iloc.
elemento_esp_iloc = df_uno.iloc[0, 2]

# Comentario: El código anterior selecciona el valor en la fila 0 y la columna 2 del DataFrame.
print(elemento_esp_iloc)

# Comentario: Seleccionar y mostrar todos los elementos de la columna en la posición 2 (tercera columna) del DataFrame.
elemento_esp_iloc = df_uno.iloc[:, 2]

# Comentario: El código anterior selecciona todos los elementos de la tercera columna del DataFrame.
# El ":" en la primera posición significa "todas las filas", y el 2 en la segunda posición se refiere a la tercera columna.
print(elemento_esp_iloc)



# Comentario: Seleccionar y mostrar todos los elementos de la columna "edad" utilizando loc.
elemento_esp_loc = df_uno.loc[:, "edad"]

# Comentario: El código anterior selecciona y muestra todos los elementos de la columna "edad" del DataFrame.
# ":" en la primera posición significa "todas las filas" y "edad" en la segunda posición se refiere a la columna "edad".
print(elemento_esp_loc)

# Comentario: Seleccionar y mostrar todas las filas donde el valor en la columna "edad" sea menor que 40 utilizando loc.
elemento_esp_loc = df_uno.loc[df_uno["edad"] < 40, :]

# Comentario: El código anterior filtra el DataFrame para seleccionar y mostrar todas las filas donde el valor en la columna "edad" sea menor que 40.
print(elemento_esp_loc)

# Comentario: Seleccionar y mostrar todas las filas donde el valor en la columna "edad" sea mayor que 40 utilizando loc.
elemento_esp_loc = df_uno.loc[df_uno["edad"] > 40, :]

# Comentario: El código anterior filtra el DataFrame para seleccionar y mostrar todas las filas donde el valor en la columna "edad" sea mayor que 40.
print(elemento_esp_loc)

# Comentario: Seleccionar y mostrar todas las filas donde el valor en la columna "edad" sea igual a 40 utilizando loc.
elemento_esp_loc = df_uno.loc[df_uno["edad"] == 40, :]

# Comentario: El código anterior filtra el DataFrame para seleccionar y mostrar todas las filas donde el valor en la columna "edad" sea igual a 40.
print(elemento_esp_loc)

# Comentario: Seleccionar y mostrar todas las filas donde el valor en la columna "edad" sea diferente de 40 utilizando loc.
elemento_esp_loc = df_uno.loc[df_uno["edad"] != 40, :]

# Comentario: El código anterior filtra el DataFrame para seleccionar y mostrar todas las filas donde el valor en la columna "edad" sea diferente de 40.
print(elemento_esp_loc)

"6:43:05 / 8:06:29"


#Nota: la diferencia de "loc", que usa etiquetas de fila y columna, "iloc" utiliza índices enteros basados en posición.


