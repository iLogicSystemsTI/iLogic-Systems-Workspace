import random
import string


def generar_contrasea(
    longitud,
    incluir_mayusculas=True,
    incluir_minusculas=True,
    incluir_numeros=True,
    incluir_simbolos=True,
):
    caracteres = ""

    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    if caracteres == "":
        print("Error: Debes incluir al menos un tipo de caracteres.")
        return None

    contrasea = "".join(random.choice(caracteres) for _ in range(longitud))
    return contrasea


longitud = 12
contrasea = generar_contrasea(longitud)
print("Contrasea generada:", contrasea)
