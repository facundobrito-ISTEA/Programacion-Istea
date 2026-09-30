"""
EJERCICIO 2 — Combinar Dos Listas
##################################

Escribí una función llamada `combinar_listas(lista1, lista2)` que reciba dos listas
como parámetros y devuelva una nueva lista con todos los elementos de ambas,
primero los de `lista1` y luego los de `lista2`.

Importante: no uses el operador `+` entre listas ni el método `.extend()`.
Debés recorrer cada lista con un bucle y construir la nueva lista elemento por elemento.

Luego llamá a la función con los siguientes ejemplos e imprimí los resultados:

    lista_a = [1, 2, 3]
    lista_b = [4, 5, 6]
    # Resultado esperado: [1, 2, 3, 4, 5, 6]

    lista_c = ["manzana", "pera"]
    lista_d = ["naranja", "uva", "durazno"]
    # Resultado esperado: ["manzana", "pera", "naranja", "uva", "durazno"]

"""


def combinar_listas(lista1, lista2):

    lista_combinada = []

    for item in lista1:
        lista_combinada.append(item)

    for item in lista2:
        lista_combinada.append(item)

    return lista_combinada


lista_01 = [1, 2, 3]
lista_02 = [4, 5, 6]
lista_combinada = combinar_listas(lista_01, lista_02)
print(f"Las listas originales eran: {lista_01} y {lista_02}")
print(f"La lista combinada es: {lista_combinada}")

lista_03 = ["manzana", "pera"]
lista_04 = ["naranja", "uva", "durazno"]
lista_combinada = combinar_listas(lista_03, lista_04)
print(f"Las listas originales eran: {lista_03} y {lista_04}")
print(f"La lista combinada es: {lista_combinada}")
