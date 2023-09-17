# Importa el módulo "modulos_saludar".
import modulos_saludar

# Llama a la función "saludar" del módulo "modulos_saludar" y almacena el resultado en la variable "saludo".
saludo = modulos_saludar.saludar("Juan")

# Imprime el saludo.
print(saludo)

# Imprime el tipo del módulo "modulos_saludar".
print(type(modulos_saludar))

# Importa el módulo "modulolos_caminar" y le asigna un alias "m_caminar".
import modulos_caminar as m_caminar

# Llama a la función "caminar" del módulo "modulolos_caminar" (usando el alias) y almacena el resultado en la variable "camina".
camina = m_caminar.caminar("Juan")

# Imprime la acción de caminar.
print(camina)

# Importa solo la función "saludar" del módulo "modulos_saludar".
from modulos_saludar import saludar

# Llama a la función "saludar" directamente y almacena el resultado en la variable "salodo".
salodo = saludar("Josu")

# Imprime el saludo.
print(salodo)

# Define una variable "name" con el valor "Noelia".
name = "Noelia"

# Combina los saludos y acciones de caminar en una cadena de texto formateada.
saluda_camina = f"{modulos_saludar.saludar(name)} \n{m_caminar.caminar(name)}"

# Imprime la cadena que combina el saludo y la acción de caminar.
print(saluda_camina)

# Imprime una lista de los atributos y funciones disponibles en el módulo "m_caminar".
print(dir(m_caminar))

# Imprime el atributo "__name__" del módulo "m_caminar".
print(m_caminar.__name__)

# Imprime el atributo "__name__" del módulo principal (el programa principal en ejecución).
print(__name__)
