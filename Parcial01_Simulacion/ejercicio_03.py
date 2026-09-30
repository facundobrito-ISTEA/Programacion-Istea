"""
EJERCICIO 3 — Eliminar Duplicados de una Lista
################################################

Escribí una función llamada `eliminar_duplicados(lista)` que reciba una lista
y devuelva una nueva lista con los mismos elementos pero sin repetidos.
El orden de aparición de los elementos debe mantenerse (se conserva la primera vez
que aparece cada elemento).

Importante: no uses `set()` para resolver esto.
Debés recorrer la lista con un bucle y verificar manualmente si el elemento ya fue agregado.

Luego llamá a la función con los siguientes ejemplos e imprimí los resultados:

    lista1 = [1, 2, 3, 1, 2, 4]
    # Resultado esperado: [1, 2, 3, 4]

    lista2 = ["Pedro", "Florencia", "Ana", "Pedro", "Ana"]
    # Resultado esperado: ["Pedro", "Florencia", "Ana"]

    lista3 = [1, 2, 3, 1, 2, 4, "Pedro", "Florencia", "Ana", "Pedro"]
    # Resultado esperado: [1, 2, 3, 4, "Pedro", "Florencia", "Ana"]

"""


def eliminar_duplicados(lista):

    sin_duplicados = []

    for item in lista:
        # ✅ Bien hecho: el `not in` sobre la lista nueva mantiene el orden de
        # primera aparición sin usar set().
        if item not in sin_duplicados:
            sin_duplicados.append(item)

    return sin_duplicados


# todo perfecto!
lista1 = [1, 2, 3, 1, 2, 4]
lista_final = eliminar_duplicados(lista1)
print(f"La lista original era: {lista1}")
print(f"La lista sin duplicados es: {lista_final}")

lista2 = ["Pedro", "Florencia", "Ana", "Pedro", "Ana"]
lista_final = eliminar_duplicados(lista2)
print(f"La lista original era: {lista2}")
print(f"La lista sin duplicados es: {lista_final}")

lista3 = [1, 2, 3, 1, 2, 4, "Pedro", "Florencia", "Ana", "Pedro"]
lista_final = eliminar_duplicados(lista3)
print(f"La lista original era: {lista3}")
print(f"La lista sin duplicados es: {lista_final}")
