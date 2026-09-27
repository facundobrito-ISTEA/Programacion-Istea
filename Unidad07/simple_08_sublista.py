# ============================================================
# UNIDAD 07 - Nivel simple - Ejercicio 8
# ============================================================
#
# Escribir un programa que extraiga una sublista de una lista principal.
# El usuario debe indicar el indice inicial y el indice final.
# Usar slicing para extraer la sublista e imprimirla.
#
# Ejemplo:
#   Lista original:  [1, 2, 3, 4, 5, 6]
#   Indice inicial: 2
#   Indice final:   6
#   Sublista:       [3, 4, 5, 6]
# ============================================================

lista_original = [1, 2, 3, 4, 5, 6]

indice_inicial = int(input("Ingrese el índice inicial: "))
indice_final = int(input("Ingrese el índice final: "))

lista_recortada = lista_original[indice_inicial:indice_final]

print(f"Lista original: {lista_original}")
print(f"Sublista: {lista_recortada}")