# ============================================================
# UNIDAD 07 - Nivel medio - Ejercicio 3
# ============================================================
#
# Combinar dos listas:
# Crear una funcion llamada combinar_listas(lista1, lista2) que reciba
# dos listas y retorne una nueva lista con todos los elementos de ambas,
# primero los de lista1 y luego los de lista2.
# No usar el operador + ni el metodo extend(); hacerlo con un bucle.
#
# Ejemplo:
#   combinar_listas([1, 2, 3], [4, 5, 6])   # [1, 2, 3, 4, 5, 6]
#   combinar_listas(["a", "b"], ["c"])      # ["a", "b", "c"]
# ============================================================

def combinar_listas(lista1, lista2):
    lista_combinada = []

    for item in lista1:
        lista_combinada.append(item)

    for item in lista2:
        lista_combinada.append(item)

    return lista_combinada


lista1 = [1, 2, 3, 6]
lista2 = [4, 5, 6]
lista_combinada = combinar_listas(lista1, lista2)

print(f"Las listas originales eran: {lista1} {lista2}")
print(f"La lista combinada es: {lista_combinada}")
print()
lista3 = ["a", "b"]
lista4 = ["c"]
lista_combinada = combinar_listas(lista3, lista4)

print(f"Las listas originales eran: {lista3} {lista4}")
print(f"La lista combinada es: {lista_combinada}")
