"""
EJERCICIO 2 — Validar Email
############################

Definí una función llamada `validar_email(email)` que reciba un string y
devuelva `True` si el email es válido, o `False` en caso contrario.

Validaciones requeridas:

1. Debe contener **exactamente un símbolo `@`** (ni más, ni menos).
2. Debe tener **al menos un carácter antes** del `@` (nombre de usuario).
3. Debe tener **al menos un carácter después** del `@` y antes del punto
   (dominio).
4. Debe contener **al menos un punto `.`** después del `@`.
5. Debe tener **al menos 2 caracteres después del último punto** (extensión
   del tipo `.com`, `.ar`, `.edu`).
6. **No debe contener espacios en blanco** en ninguna parte.
7. El email **no puede empezar ni terminar** con `@` o `.`.

Ejemplos:

    validar_email("juan@gmail.com")          # True
    validar_email("maria.lopez@utn.edu.ar")  # True
    validar_email("correo@dominio.com.ar")   # True
    validar_email("usuario@@gmail.com")      # False  (dos @)
    validar_email("gmail.com")               # False  (sin @)
    validar_email("juan @gmail.com")         # False  (tiene espacio)
    validar_email("@gmail.com")              # False  (sin usuario)
    validar_email("juan@gmail")              # False  (sin punto después del @)
    validar_email("juan@.com")               # False  (sin dominio)
    validar_email("juan@gmail.c")            # False  (extensión muy corta)

Ayuda: podés usar `.count()` para contar caracteres, `.find()` o `.index()`
para localizar posiciones, y validar cada condición paso a paso.

"""


def validar_email(email):

    if email.count("@") != 1:
        return False
    if " " in email:
        return False
    if email[0] == "@" or email[-1] == "@":
        return False
    if email[0] == "." or email[-1] == ".":
        return False

    partes = email.split("@")
    usuario = partes[0]
    dominio = partes[1]
    if len(usuario) < 1:
        return False
    if "." not in dominio:
        return False
    if dominio[0] == ".":
        return False
    partes_dominio = dominio.split(".")
    extension = partes_dominio[-1]
    if len(extension) < 2:
        return False

    return True


print(validar_email("juan@gmail.com"))          # True
print(validar_email("maria.lopez@utn.edu.ar"))  # True
print(validar_email("correo@dominio.com.ar"))   # True
print(validar_email("usuario@@gmail.com"))      # False  (dos @)
print(validar_email("gmail.com"))               # False  (sin @)
print(validar_email("juan @gmail.com"))         # False  (tiene espacio)
print(validar_email("@gmail.com"))              # False  (sin usuario)
print(validar_email("juan@gmail"))              # False  (sin punto después del @)
print(validar_email("juan@.com"))               # False  (sin dominio)
print(validar_email("juan@gmail.c"))            # False  (extensión muy corta)
