# ============================================================
# UNIDAD 07 - Nivel simple - Ejercicio 8 (version alternativa con for)
# ============================================================
#
# Misma consigna que simple_08_sublista.py, pero recorriendo los indices
# con un for en lugar de usar slicing, para entender que hace
# el slicing por dentro.
#
# Diferencia encontrada al probar: Al principio, si el índice final
# superaba el largo de la lista, esta versión daba IndexError.
# Para que se comporte igual que el slicing, antes del for se ajusta
# el índice final al largo de la lista.
# ============================================================

lista_original = ["a", "b", "c", "d", "e", "f"]
lista_recortada = []

indice_inicial = int(input("Ingrese el índice inicial: "))
indice_final = int(input("Ingrese el índice final: "))

largo_lista = len(lista_original)
if indice_final > largo_lista:
    print(f"Índice final ajustado a {largo_lista}")
    indice_final = largo_lista

for indice in range(indice_inicial, indice_final):
    elemento = lista_original[indice]
    lista_recortada.append(elemento)

print(f"Lista original: {lista_original}")
print(f"Sublista: {lista_recortada}")
