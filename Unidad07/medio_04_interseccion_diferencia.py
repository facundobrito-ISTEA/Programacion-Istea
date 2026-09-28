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


def mostrar_resultados(lista_a, lista_b):
    print(f"Primera lista: {lista_a}")
    print(f"Segunda lista: {lista_b}")
    solo_en_primera = diferencia(lista_a, lista_b)
    print(f"Elementos que están solo en la primera lista: {solo_en_primera}")
    en_ambas = interseccion(lista_a, lista_b)
    print(f"Elementos que están en ambas listas, sin repetidos: {en_ambas}")
    print()


lista_1 = [1, 3, 3, 4, 4]
lista_2 = [3, 4, 4, 5]

mostrar_resultados(lista_1, lista_2)

lista_3 = [1, 2, 3, 4]
lista_4 = [3, 4, 5, 6]

mostrar_resultados(lista_3, lista_4)

lista_5 = ["ana", "luis", "pedro"]
lista_6 = ["luis", "pedro", "juan"]

mostrar_resultados(lista_5, lista_6)
