"""
EJERCICIO 1 — Validar Contraseña
##################################

Escribí una función llamada `validar_contrasena(contrasena)` que reciba un string
y retorne `True` si la contraseña es válida, o `False` si no lo es.

Condiciones que debe cumplir una contraseña válida:

1. Debe tener al menos 8 caracteres.
2. Debe contener al menos una letra mayúscula (A-Z).
3. Debe contener al menos una letra minúscula (a-z).
4. Debe contener al menos un dígito (0-9).
5. No debe contener espacios en blanco.

No uses expresiones regulares (módulo `re`). Recorré el string con un bucle
y verificá cada condición manualmente.

Ejemplos:

    validar_contrasena("Hola1234")      # True
    validar_contrasena("hola1234")      # False  (sin mayúscula)
    validar_contrasena("HOLA1234")      # False  (sin minúscula)
    validar_contrasena("HolaMundo")     # False  (sin dígito)
    validar_contrasena("Hola 123")      # False  (tiene espacio)
    validar_contrasena("Ho1")           # False  (menos de 8 caracteres)

Ayuda: podés usar los métodos `.isupper()`, `.islower()` y `.isdigit()` para
verificar el tipo de cada carácter dentro del bucle.

"""


def validar_contrasena(contrasena):

    longitud = False
    mayuscula = False
    minuscula = False
    digito = False
    contiene_espacio = False

    cantidad_caracteres = len(contrasena)
    if cantidad_caracteres >= 8:
        longitud = True

    for caracter in contrasena:
        if caracter.isupper():
            mayuscula = True
        elif caracter.islower():
            minuscula = True
        elif caracter.isdigit():
            digito = True
        elif caracter == " ":
            contiene_espacio = True

    if longitud and mayuscula and minuscula and digito and not contiene_espacio:
        contrasena_valida = True
    else:
        contrasena_valida = False

    return contrasena_valida


print(f"Holarr32321 -> {validar_contrasena('Holarr32321')} esperado: True")
print(f"Hola1234 333 -> {validar_contrasena('Hola1234 333')} esperado: False")
print(f"Ho23r2    32 -> {validar_contrasena('Ho23r2    32')} esperado: False")
print(f"Hola1234 -> {validar_contrasena('Hola1234')} esperado: True")
print(f"hola1234 -> {validar_contrasena('hola1234')} esperado: False")
print(f"HOLA1234 -> {validar_contrasena('HOLA1234')} esperado: False")
print(f"HolaMundo -> {validar_contrasena('HolaMundo')} esperado: False")
print(f"Hola 123 -> {validar_contrasena('Hola 123')} esperado: False")
print(f"Ho1 -> {validar_contrasena('Ho1')} esperado: False")
