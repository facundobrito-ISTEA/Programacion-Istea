# ============================================================
# UNIDAD 07 - Nivel simple - Ejercicio 2
# ============================================================
#
# Crear una lista con los nombres de al menos 5 companeros de clase.
# Imprimir la lista en el orden original.
# Luego ordenarla alfabeticamente con sort() e imprimirla nuevamente.
#
# Ejemplo de salida:
#   Original:   ['Marcos', 'Ana', 'Luis', 'Carla', 'Pedro']
#   Ordenada:   ['Ana', 'Carla', 'Luis', 'Marcos', 'Pedro']
# ============================================================

lista_nombres = ["Luis", "Ernesto", "Fabian", "Walter", "Ezequiel"]

print(f"Original: {lista_nombres}")

lista_nombres.sort()

print(f"Ordenada: {lista_nombres}")