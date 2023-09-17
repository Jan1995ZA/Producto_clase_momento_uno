# Enruta desde otra carpeta.
# Importamos la función 'saludar' del módulo 'modulos_saludar' y le damos un alias 'm_saludar'
from funciones_python.modulos_saludar import saludar as m_saludar

# Llamamos a la función 'saludar' con el nombre "Juan" como argumento y almacenamos el resultado en la variable 'saludo'
saludo = m_saludar("Juan")

# Imprimimos el saludo en la consola
print(saludo)
######################################################
# Importamos el módulo 'modulos_saludar' desde el paquete 'funciones_python'
import funciones_python.modulos_saludar

# Llamamos a la función 'saludar' del módulo 'modulos_saludar' con el nombre "Noe" como argumento y almacenamos el resultado en la variable 'saludo'
saludo = funciones_python.modulos_saludar.saludar("Noe")

# Imprimimos el saludo en la consola
print(saludo)
#####################################################
# Importamos el módulo 'modulos_saludar' desde el paquete 'funciones_python'
import funciones_python.modulos_saludar as m_salud

# Llamamos a la función 'saludar' del módulo 'modulos_saludar' con el nombre "Noe" como argumento y almacenamos el resultado en la variable 'saludo'
saludo = m_salud.saludar("Leo")

# Imprimimos el saludo en la consola
print(saludo)
##########################################################
# Importamos el módulo 'sys' que proporciona funciones y variables relacionadas con la configuración del sistema
import sys

# Agregamos la ruta al directorio 'Modulos' al final de la lista de rutas de Python para que Python pueda encontrar el módulo 'modulos_caminar'
sys.path.append("c:\\Users\\juanz\\OneDrive\\Escritorio\\Semestre 4\\clase_de_python\\3.NIVEL TRES\\Modulos")

# Importamos el módulo 'modulos_caminar' con un alias 'camina'
import modulos_caminar as camina

# Llamamos a la función 'caminar' del módulo 'modulos_caminar' con el argumento "Sol" y almacenamos el resultado en la variable 'resultado'
resultado = camina.caminar("Sol")

# Imprimimos el resultado de la función 'caminar' en la consola
print(resultado)

# Imprimimos el módulo 'sys' para mostrar información sobre la configuración del sistema
print(sys)

# Imprimimos la lista de nombres de módulos internos disponibles en el sistema
print(sys.builtin_module_names)

# Imprimimos la lista de rutas de búsqueda de módulos de Python
print(sys.path)
