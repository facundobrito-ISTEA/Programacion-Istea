"""
EJERCICIO 3 — Análisis de una Lista de Números
###############################################

Dada la siguiente lista de números:

    numeros = [4, 7, 2, 9, 1, 5, 8, 3, 6]

Tu programa debe:

1. Imprimir la lista original.
2. Imprimir el número **más alto** y el **más bajo** de la lista.
3. Imprimir la lista **ordenada de menor a mayor**.
4. Imprimir solamente los números **mayores a 5**.

Restricciones:

- **No** se permite usar las funciones `sorted()`, `max()` ni `min()`.
- Recorré la lista con un bucle para calcular cada resultado.

Ejemplo de salida esperada:

    Lista original: [4, 7, 2, 9, 1, 5, 8, 3, 6]
    Número más alto: 9
    Número más bajo: 1
    Lista ordenada: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Números mayores a 5: [7, 9, 8, 6]

"""

numeros = [4, 7, 2, 9, 1, 5, 8, 3, 6]

def calcular_maximo(lista):
    maximo = lista[0]
    for elemento in lista:
        if elemento > maximo:
            maximo = elemento
    return maximo

def calcular_minimo(lista):
    minimo = lista[0]
    for elemento in lista:
        if elemento < minimo:
            minimo = elemento
    return minimo

def ordenamiento(lista):
    lista_ordenada = []
    lista_intermedia = []
    for i in lista:
        lista_intermedia.append(i)

    while len(lista_intermedia) > 0:
        menor = calcular_minimo(lista_intermedia)
        lista_ordenada.append(menor)
        lista_intermedia.remove(menor)
    return lista_ordenada

def calcular_mayores(lista):
    numeros_mayores = []   
    for elemento in lista:
        if elemento > 5:
            numeros_mayores.append(elemento)
    return numeros_mayores

print(f"Lista original: {numeros}")
print(f"Número más alto: {calcular_maximo(numeros)}")
print(f"Número más bajo: {calcular_minimo(numeros)}")
print(f"Lista ordenada: {ordenamiento(numeros)}")
print(f"Números mayores a 5: {calcular_mayores(numeros)}")