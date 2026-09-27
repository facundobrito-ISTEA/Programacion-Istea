# ============================================================
# UNIDAD 07 - Nivel simple - Ejercicio 6
# ============================================================
#
# Escribir un programa que elimine todos los elementos duplicados
# de una lista dada, conservando solo la primera aparicion de cada uno.
# No usar set() para resolverlo; hacerlo manualmente con un bucle.
#
# Ejemplo:
#   Original:       [3, 1, 2, 3, 4, 1, 5, 2]
#   Sin duplicados: [3, 1, 2, 4, 5]
# ============================================================

lista_original = [3, 1, 2, 3, 4, 1, 5, 2, 5, 7, 8, 93, 1, 2, 3, 100, 500, "papa", "batata"]
lista_sin_duplicados = []

for item in lista_original:
    if item not in lista_sin_duplicados:
        lista_sin_duplicados.append(item)

print(f"Original: {lista_original}")
print(f"Sin duplicados: {lista_sin_duplicados}")