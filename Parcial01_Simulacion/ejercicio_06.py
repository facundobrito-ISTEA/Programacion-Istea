"""
EJERCICIO 6 — Conversor de Unidades con Módulo
################################################

Desarrollá un programa que convierta unidades de distancia y peso.

El programa debe mostrar un menú al usuario y permitirle elegir qué conversión
realizar. Debe seguir mostrando el menú hasta que el usuario elija salir.

Menú:
    1. Kilómetros a Millas
    2. Kilogramos a Libras
    3. Salir

Fórmulas:
    - 1 kilómetro = 0.621371 millas
    - 1 kilogramo = 2.20462 libras

Requisitos:
- Las funciones de conversión deben estar en un módulo separado llamado `conversiones.py`.
- Cada función debe tener un docstring de una línea que explique qué hace.
  Ver formato: https://peps.python.org/pep-0257/#one-line-docstrings
- El menú y la lógica principal deben estar en este archivo (ejercicio_06.py).
- Si el usuario ingresa una opción de menú que no es 1, 2 o 3 (incluyendo texto
  no numérico), mostrar "Opción no válida. Intente nuevamente." y volver a
  mostrar el menú.
- Validar que el valor ingresado para convertir sea un número positivo. Si no
  lo es (número negativo, cero, o texto no numérico), mostrar un mensaje de
  error (por ejemplo "Valor inválido, debe ser un número positivo.") y volver
  a mostrar el menú sin cortar el programa.

Ejemplo de ejecución:

    ¿Qué desea convertir?
    1. Kilómetros a Millas
    2. Kilogramos a Libras
    3. Salir
    Ingrese una opción: 1
    Ingrese los kilómetros: 10
    10 km = 6.21 millas

    Ingrese una opción: 2
    Ingrese los kilogramos: 70
    70 kg = 154.32 libras

    Ingrese una opción: 3
    ¡Hasta luego!

Mostrá los resultados redondeados a 2 decimales (por ejemplo, `f"{valor:.2f}"`).

"""

import conversiones


def es_numero_positivo(texto):
    nuevo_valor = texto.replace(".", "", 1)
    if not nuevo_valor.isdigit():
        return False

    numero = float(texto)
    if numero <= 0:
        return False

    return True


opcion = ""

while opcion != "3":
    print("¿Qué desea convertir?")
    print("1. Kilómetros a Millas")
    print("2. Kilogramos a Libras")
    print("3. Salir")
    print()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        kilometros = input("Ingrese los kilómetros: ")
        if es_numero_positivo(kilometros):
            valor_km = kilometros
            kilometros = float(kilometros)
            millas = conversiones.km_a_millas(kilometros)
            print(f"{valor_km} km = {millas:.2f} millas")
        else:
            print("Valor inválido, debe ser un número positivo.")
        print()

    elif opcion == "2":
        kilogramos = input("Ingrese los kilogramos: ")
        if es_numero_positivo(kilogramos):
            valor_kg = kilogramos
            kilogramos = float(kilogramos)
            libras = conversiones.kg_a_libras(kilogramos)
            print(f"{valor_kg} kg = {libras:.2f} libras")
        else:
            print("Valor inválido, debe ser un número positivo.")
        print()
    elif opcion == "3":
        print("¡Hasta luego!")
    else:
        print("Opción no válida. Intente nuevamente.")
