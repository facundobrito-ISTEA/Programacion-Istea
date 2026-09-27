# ============================================================
# UNIDAD 07 - Nivel medio - Ejercicio 2
# ============================================================
#
# Eliminar duplicados con funcion:
# Crear una funcion llamada eliminar_duplicados(lista) que reciba una lista
# y retorne una nueva lista con los elementos unicos, conservando el orden
# de primera aparicion.
# No usar set() para resolverlo; hacerlo con un bucle y verificacion manual.
#
# Ejemplo:
#   eliminar_duplicados([1, 2, 3, 1, 2, 4])   # [1, 2, 3, 4]
#   eliminar_duplicados(["ana", "luis", "ana", "pedro"])  # ["ana", "luis", "pedro"]
# ============================================================

def eliminar_duplicados(lista):
    lista_sin_duplicados = []

    for item in lista:
        if item not in lista_sin_duplicados:
            lista_sin_duplicados.append(item)

    return lista_sin_duplicados


lista_01 = [1, 1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6, 5, 5, 4, 4, 3, 7, 8]
lista_02 = ["papa", 1, 1, "batata", 3, 4, 5,
            "pera", 6, 6, "pera", 6, 6, 5, 5, 4, 4, 3, 7, 8]
lista_03 = [1, 2, 3, 1, 2, 4]
lista_04 = ["ana", "luis", "ana", "pedro"]

print(f"Original: {lista_01}")
print(f"Sin duplicados: {eliminar_duplicados(lista_01)}")
print()
print(f"Original: {lista_02}")
print(f"Sin duplicados: {eliminar_duplicados(lista_02)}")
print()
print(f"Original: {lista_03}")
print(f"Sin duplicados: {eliminar_duplicados(lista_03)}")
print()
print(f"Original: {lista_04}")
print(f"Sin duplicados: {eliminar_duplicados(lista_04)}")
