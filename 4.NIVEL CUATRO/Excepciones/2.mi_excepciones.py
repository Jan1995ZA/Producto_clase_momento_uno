# Define una clase personalizada de excepción llamada MiExcept
class MiExcept(Exception):
    def __init__(self, err):
        # Constructor de la excepción que muestra un mensaje personalizado
        print(f"Impresionante, cometiste el siguiente error: {err}")

try:
    # Intenta elevar una instancia de MiExcept con el mensaje "jajjajajaj mk"
    raise MiExcept("jajjajajaj mk")
except:
    # Se ejecuta cuando se captura una excepción
    print("Pelota")

# Intenta elevar otra instancia de MiExcept con el mensaje "mera loca",
# pero esto generará un error antes de llegar aquí
raise MiExcept("mera loca")
