# ============================================================
# UNIDAD 07 - Nivel medio - Ejercicio 4
# ============================================================
#
# Interseccion y diferencia entre dos listas:
# Crear dos funciones separadas:
#
#   a) interseccion(lista1, lista2): retorna una lista con los elementos
#      que estan presentes en AMBAS listas (sin repetidos).
#
#   b) diferencia(lista1, lista2): retorna una lista con los elementos
#      que estan en lista1 pero NO estan en lista2.
#
# Las funciones deben funcionar con listas de cualquier longitud y tipo.
# No usar operadores de conjuntos (set); implementar con bucles.
#
# Ejemplo:
#   interseccion([1, 2, 3, 4], [3, 4, 5, 6])  # [3, 4]
#   diferencia([1, 2, 3, 4], [3, 4, 5, 6])    # [1, 2]
# ============================================================

def interseccion(lista1, lista2):
    en_ambas = []

    for elemento in lista1:
        if elemento in lista2 and elemento not in en_ambas:
            en_ambas.append(elemento)

    return en_ambas


def diferencia(lista1, lista2):
    solo_en_lista1 = []

    for elemento in lista1:
        if elemento not in lista2:
            solo_en_lista1.append(elemento)

    return solo_en_lista1


lista1 = [1, 3, 3, 4, 4]
lista2 = [3, 4, 4, 5]

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(
    f"Elementos que están en la lista1 y no en la lista2: {diferencia(lista1, lista2)}")
print(
    f"Elementos que están en ambas listas, sin repetidos: {interseccion(lista1, lista2)}")
print()

lista3 = [1, 2, 3, 4]
lista4 = [3, 4, 5, 6]

print(f"Lista 3: {lista3}")
print(f"Lista 4: {lista4}")
print(
    f"Elementos que están en la lista3 y no en la lista4: {diferencia(lista3, lista4)}")
print(
    f"Elementos que están en ambas listas, sin repetidos: {interseccion(lista3, lista4)}")
print()

lista5 = ["ana", "luis", "pedro"]
lista6 = ["luis", "pedro", "juan"]

print(f"Lista 5: {lista5}")
print(f"Lista 6: {lista6}")
print(
    f"Elementos que están en la lista5 y no en la lista6: {diferencia(lista5, lista6)}")
print(
    f"Elementos que están en ambas listas, sin repetidos: {interseccion(lista5, lista6)}")
