# ============================================================
# PRACTICA EN CLASE - Grupo 1: ¿Cual es tu signo del zodiaco?
# (Unidades 2 y 3)
# ============================================================
#
# Escribir un programa que le pida al usuario su dia y su mes
# de nacimiento y le diga cual es su signo del zodiaco.
#
# Ejemplo de ejecucion:
#   Ingresa tu dia de nacimiento: 15
#   Ingresa tu mes de nacimiento: 8
#   Tu signo del zodiaco es: Leo
# ============================================================

print("Bienvenido al programa para conocer tu signo del zodiaco")

dia = int(input("Por favor, ingrese su dia de nacimiento: "))
mes = int(input("Ingrese su mes de nacimiento en numero: "))

if mes == 12:
    if dia >= 22:
        signo = "Capricornio"
    else:
        signo = "Sagitario"
elif mes == 11:
    if dia >= 22:
        signo = "Sagitario"
    else:
        signo = "Escorpio"
elif mes == 10:
    if dia >= 23:
        signo = "Escorpio"
    else:
        signo = "Libra"
elif mes == 9:
    if dia >= 23:
        signo = "Libra"
    else:
        signo = "Virgo"
elif mes == 8:
    if dia >= 23:
        signo = "Virgo"
    else:
        signo = "Leo"
elif mes == 7:
    if dia >= 23:
        signo = "Leo"
    else:
        signo = "Cáncer"
elif mes == 6:
    if dia >= 21:
        signo = "Cáncer"
    else:
        signo = "Géminis"
elif mes == 5:
    if dia >= 21:
        signo = "Géminis"
    else:
        signo = "Tauro"
elif mes == 4:
    if dia >= 20:
        signo = "Tauro"
    else:
        signo = "Aries"
elif mes == 3:
    if dia >= 21:
        signo = "Aries"
    else:
        signo = "Piscis"
elif mes == 2:
    if dia >= 19:
        signo = "Piscis"
    else:
        signo = "Acuario"
elif mes == 1:
    if dia >= 20:
        signo = "Acuario"
    else:
        signo = "Capricornio"
else:
    signo = "Mes no válido"


print("Tu signo del zodiaco es: " + signo)
