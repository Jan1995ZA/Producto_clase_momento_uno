#Que son los modulos en python ?
# Modulos de pyton (los que estan creados por pytho en lenguaje'c')
# Thid party modulos: modulos de teceros
# own modulos: creados por nosotros
#
"""
Los módulos en Python son un mecanismo para organizar el código en archivos separados.

Cada módulo es un archivo Python con la extensión `.py`.

El nombre del módulo es el mismo que el nombre del archivo, sin la extensión.

Por ejemplo, un archivo llamado `mi_modulo.py` define un módulo llamado `mi_modulo`.

Los módulos se pueden importar en otros módulos utilizando la declaración `import`.

Por ejemplo, la siguiente declaración importa el módulo `mi_modulo` en el módulo actual:


​
import mi_modulo
​


Una vez que un módulo ha sido importado, se puede acceder a sus funciones, clases y variables utilizando la notación de puntos.

Por ejemplo, la siguiente declaración llama a la función `mi_funcion()` en el módulo `mi_modulo`:


​
mi_modulo.mi_funcion()
​


Los módulos también se pueden utilizar para crear paquetes.

Un paquete es una colección de módulos relacionados que se agrupan en un directorio.

El nombre del paquete es el mismo que el nombre del directorio.

Por ejemplo, un directorio llamado `mi_paquete` define un paquete llamado `mi_paquete`.

Los paquetes se pueden importar en otros módulos utilizando la declaración `import`.

Por ejemplo, la siguiente declaración importa el paquete `mi_paquete` en el módulo actual:

​
import mi_paquete
​

Una vez que un paquete ha sido importado, se puede acceder a sus módulos utilizando la notación de puntos.

Por ejemplo, la siguiente declaración llama a la función `mi_funcion()` en el módulo `mi_modulo` del paquete `mi_paquete`:

​
mi_paquete.mi_modulo.mi_funcion()
​

Los módulos y paquetes son una parte fundamental de la organización del código en Python.

Permiten dividir el código en archivos separados, lo que facilita su mantenimiento y reutilización.

"""
