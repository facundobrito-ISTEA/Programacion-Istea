# ============================================================
# UNIDAD 07 - Nivel simple - Ejercicio 8 (version alternativa con for)
# ============================================================
#
# Misma consigna que esimple_08_sublista.py, pero recorriendo los indices
# con un for en lugar de usar slicing, para entender que hace
# el slicing por dentro.
#
# Diferencia encontrada al probar: si el indice final es mayor
# que el largo de la lista, esta version da IndexError, mientras
# que el slicing corta donde termina la lista sin error.
# ============================================================

lista_original = ["a", "b", "c", "d", "e", "f"]
lista_recortada = []

indice_inicial = int(input("Ingrese el índice inicial: "))
indice_final = int(input("Ingrese el índice final: "))

for indice in range(indice_inicial, indice_final):
    elemento = lista_original[indice]
    lista_recortada.append(elemento)

print(f"Lista original: {lista_original}")
print(f"Sublista: {lista_recortada}")