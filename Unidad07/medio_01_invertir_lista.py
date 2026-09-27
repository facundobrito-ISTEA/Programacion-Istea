# ============================================================
# UNIDAD 07 - Nivel medio - Ejercicio 1
# ============================================================
#
# Invertir una lista manualmente:
# Primero, escribir el codigo directamente (sin funcion) para invertir
# el orden de una lista de 5 elementos.
# Luego, crear una funcion llamada invertir_lista(lista) que reciba
# cualquier lista y retorne una nueva lista con los elementos en orden inverso.
# No usar lista.reverse() ni slicing [::-1]; hacerlo con un bucle.
#
# Ejemplo:
#   invertir_lista([1, 2, 3, 4, 5])   # [5, 4, 3, 2, 1]
#
# Extra: probar la funcion con una lista de 100 numeros generados con random.
# ============================================================

import random

# ------------------------------------------------------------
# Funciones
# ------------------------------------------------------------

def invertir_lista(lista):
    lista_invertida = []
    cantidad_elementos = len(lista)

    for indice in range(cantidad_elementos - 1, -1, -1):
        dato = lista[indice]
        lista_invertida.append(dato)

    return lista_invertida


def numeros_aleatorios(cantidad):
    lista_numeros = []

    for i in range(cantidad):
        valor = random.randint(1, 100)
        lista_numeros.append(valor)

    return lista_numeros


# ------------------------------------------------------------
# Parte 1: invertir una lista de 5 elementos sin función
# ------------------------------------------------------------

letras = ["a", "b", "c", "d", "e"]
letras_invertidas = []
cantidad_letras = len(letras)

for indice in range(cantidad_letras - 1, -1, -1):
    letra = letras[indice]
    letras_invertidas.append(letra)

print(f"Lista original: {letras}")
print(f"Lista invertida: {letras_invertidas}")
print()


# ------------------------------------------------------------
# Parte 2: pruebas de la función invertir_lista
# ------------------------------------------------------------

lista_profe = [1, 2, 3, 4, 5]
print(f"Lista original: {lista_profe}")
print(f"Lista invertida: {invertir_lista(lista_profe)}")
print()

datos = numeros_aleatorios(100)
print(f"Lista original con 100 datos aleatorios: {datos}")
print(f"Lista invertida con 100 datos aleatorios: {invertir_lista(datos)}")