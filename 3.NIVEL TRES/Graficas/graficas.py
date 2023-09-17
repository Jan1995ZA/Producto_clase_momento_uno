# Importar las bibliotecas necesarias
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer un archivo CSV en un DataFrame llamado 'df'
df = pd.read_csv("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Graficas\\fecha_pedo.csv")

# Imprimir el contenido del DataFrame 'df'
print(df)

# Crear un gráfico de líneas utilizando Seaborn, donde 'fecha' se representa en el eje X y 'pedos' en el eje Y
sns.lineplot(x="fecha", y="pedos", data=df)

# Agregar un punto específico ("01-10", 28) al gráfico utilizando 'plt.plot' con el marcador 'o'
plt.plot("01-10", 28, "o")

# Mostrar el gráfico
plt.show()

####################################################

# Leer un archivo CSV en un DataFrame llamado 'df'
df = pd.read_csv("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Graficas\\sueldos_trabajos.csv")

# Crear el gráfico de barras
sns.barplot(x="trabajos", y="sueldos", data=df)

# Calcular el total de ingresos (suma de sueldos)
total_ingreso = df['sueldos'].sum()

# Mostrar el total de ingresos
print(f"Total de ingresos: {total_ingreso}")

# Mostrar el gráfico
plt.show()

##########################################

# Leer un archivo CSV en un DataFrame llamado 'df'
df = pd.read_csv("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Graficas\\tiempo_recorrido.csv")

# Crear un gráfico de dispersión (scatter plot)
sns.scatterplot(x="tiempo", y="recorrido", data=df)

# Mostrar el gráfico
plt.show()

##########################################

# Leer un archivo CSV en un DataFrame llamado 'df'
df = pd.read_csv("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Graficas\\categoria.csv")


# Crear un diagrama de caja
sns.boxplot(x="categoria", y="valor", data=df)

# Mostrar el gráfico
plt.show()

"7:06:43 / 8:06:29"