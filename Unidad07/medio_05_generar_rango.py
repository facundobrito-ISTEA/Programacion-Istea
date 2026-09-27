# ============================================================
# UNIDAD 07 - Nivel medio - Ejercicio 5
# ============================================================
#
# Generador de lista desde un rango:
# Crear una funcion llamada generar_rango(inicio, fin, paso) que genere
# y retorne una lista con todos los numeros desde inicio hasta fin
# (sin incluir fin), avanzando de a "paso" unidades.
# No usar range() ni list(range()); construir la lista con un bucle while.
#
# Ejemplo:
#   generar_rango(0, 10, 2)    # [0, 2, 4, 6, 8]
#   generar_rango(1, 20, 3)    # [1, 4, 7, 10, 13, 16, 19]
#   generar_rango(10, 0, -2)   # [10, 8, 6, 4, 2]
# ============================================================

def generar_rango(inicio, fin, paso):
    rango = []

    actual = inicio

    if paso > 0:
        while actual < fin:
            rango.append(actual)
            actual = actual + paso
    elif paso < 0:
        while actual > fin:
            rango.append(actual)
            actual = actual + paso
    # si el paso es 0 no entra a ningún while y retorna la lista vacía
    return rango


print(f"El rango generado es (0, 10, 2): {generar_rango(0, 10, 2)}")
print(f"El rango generado es (1, 20, 3): {generar_rango(1, 20, 3)}")
print(f"El rango generado es (10, 0, -2): {generar_rango(10, 0, -2)}")
print()
print(
    f"Casos no válidos (inicio menor que el fin con paso negativo(0, 10, -2)): {generar_rango(0, 10, -2)}")
print(
    f"Casos no válidos (inicio mayor que el fin con paso positivo(10, 0, 2)): {generar_rango(10, 0, 2)}")
print(f"Casos no válidos (paso cero(10, 0, 0)): {generar_rango(10, 0, 0)}")
