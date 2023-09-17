cadena = "0123456789"  # Se crea una cadena de caracteres que contiene los dígitos del 0 al 9.

# Imprime toda la cadena, desde el principio hasta el final.
print(cadena[:])  # Resultado: "0123456789"

# Imprime los primeros 5 caracteres de la cadena (índices 0 a 4).
print(cadena[:5])  # Resultado: "01234"

# Imprime los caracteres desde el índice 2 (incluido) hasta el índice 4 (no incluido).
print(cadena[2:5])  # Resultado: "234"

# Imprime la cadena desde el principio hasta el penúltimo carácter (excluyendo el último carácter).
print(cadena[:-1])  # Resultado: "012345678"

# Imprime el último carácter de la cadena.
print(cadena[-1:])  # Resultado: "9"
