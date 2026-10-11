
def mostrar_progreso(palabra_secreta, letras_intentadas):
    """Devuelve la palabra con las letras adivinadas y guiones bajos."""
    progreso = ""
    for letra in palabra_secreta:
        if letra in letras_intentadas:
            progreso = progreso + letra + " "
        else:
            progreso = progreso + "_ "

    return progreso


def palabra_completa(palabra_secreta, letras_intentadas):
    """Indica si ya se adivinaron todas las letras de la palabra."""
    ganaste = True
    for letra in palabra_secreta:
        if letra not in letras_intentadas:
            ganaste = False

    return ganaste
