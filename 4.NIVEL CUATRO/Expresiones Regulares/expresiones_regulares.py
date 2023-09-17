import re  # Importa el módulo de expresiones regulares
"""
texto = '''Hola maestro, esta es la cadena 1, como estas?
Esta es la segunda línea de texto y esta es la última
'''

# Busca la primera aparición de "Hola" en el texto
resultado = re.search("Hola", texto)
print(resultado)

# Busca todas las apariciones de "esta" en el texto
resultado = re.findall("esta", texto)
print(resultado)

# Busca todas las apariciones de "esta" en el texto, ignorando mayúsculas y minúsculas
resultado = re.findall("esta", texto, flags=re.IGNORECASE)
print(resultado)
"""
###################################################################
"""
# Ejemplo 1: Búsqueda de una palabra específica en un texto
texto = "Este es un ejemplo de texto. Hola, mundo."
patron = r"Hola"  # Define el patrón a buscar
resultado = re.search(patron, texto)  # Busca el patrón en el texto
print(resultado)

# Ejemplo 2: Búsqueda de todas las ocurrencias de una palabra en un texto
texto = "Este es un ejemplo de texto. Hola, Hola, mundo."
patron = r"Hola"  # Define el patrón a buscar
resultado = re.findall(patron, texto)  # Busca todas las ocurrencias del patrón en el texto
print(resultado)

# Ejemplo 3: Búsqueda de números enteros en un texto
texto = "Los números son: 42, 3.14, y 12345"
patron = r"\d+"  # Define el patrón para encontrar números enteros (uno o más dígitos)
resultado = re.findall(patron, texto)  # Busca todas las ocurrencias del patrón en el texto
print(resultado)

# Ejemplo 4: Búsqueda de direcciones de correo electrónico
texto = "Mis correos son: correo1@example.com y correo2@example.org"
patron = r"\S+@\S+"  # Define el patrón para encontrar direcciones de correo electrónico
resultado = re.findall(patron, texto)  # Busca todas las ocurrencias del patrón en el texto
print(resultado)

# Ejemplo 5: Búsqueda de números de teléfono en formato específico
texto = "Mis números de teléfono son: 123-456-7890 y 555-5555"
patron = r"\d{3}-\d{3}-\d{4}"  # Define el patrón para encontrar números de teléfono en formato XXX-XXX-XXXX
resultado = re.findall(patron, texto)  # Busca todas las ocurrencias del patrón en el texto
print(resultado)

# Ejemplo 6: Búsqueda de palabras que comienzan con una letra específica
texto = "La manzana es una fruta, mientras que el melón es otra."
patron = r"\b[Mm]\w+"  # Define el patrón para encontrar palabras que comienzan con 'M' o 'm'
resultado = re.findall(patron, texto)  # Busca todas las ocurrencias del patrón en el texto
print(resultado)

# Ejemplo 7: Búsqueda de URLs en un texto
texto = "Visita nuestro sitio web en https://www.ejemplo.com"
patron = r"https?://\S+"  # Define el patrón para encontrar URLs que comienzan con http:// o https://
resultado = re.findall(patron, texto)  # Busca todas las ocurrencias del patrón en el texto
print(resultado)

"""
############################################
#              flags                       #
############################################

# Ejemplo 1: Búsqueda con la bandera re.IGNORECASE (ignorar mayúsculas y minúsculas)
texto = "Este es un ejemplo de texto. Hola, hOla, mundo."
patron = r"hola"  # Patrón en minúsculas
resultado = re.findall(patron, texto, flags=re.IGNORECASE)  # Ignora mayúsculas/minúsculas
print(resultado)

# Ejemplo 2: Búsqueda con la bandera re.MULTILINE (búsqueda en múltiples líneas)
texto = "Línea 1\nLínea 2\nLínea 3"
patron = r"Línea \d+"
resultado = re.findall(patron, texto, flags=re.MULTILINE)  # Busca en múltiples líneas
print(resultado)

# Ejemplo 3: Búsqueda con la bandera re.DOTALL (inclusión del carácter de nueva línea)
texto = "Línea 1\nLínea 2\nLínea 3"
patron = r"Línea .+"
resultado = re.findall(patron, texto, flags=re.DOTALL)  # Incluye el carácter de nueva línea
print(resultado)

# Ejemplo 4: Búsqueda con la bandera re.VERBOSE (modo verbose para patrones legibles)
texto = "123-456-7890"
patron = r"""
   \d{3}   # Coincide con los primeros tres dígitos
   -       # Coincide con el guion
   \d{3}   # Coincide con los siguientes tres dígitos
   -       # Coincide con el guion final
   \d{4}   # Coincide con los últimos cuatro dígitos
"""
resultado = re.findall(patron, texto, flags=re.VERBOSE)  # Patrón legible en modo verbose
print(resultado)
