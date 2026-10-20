"""
🔢 Ejercicio 1 — Conteo de palabras únicas
A partir de una lista de frases, construí un diccionario donde las claves sean las palabras únicas y los valores la cantidad de veces que aparece cada una en el conjunto de frases.

Requisitos:

Dividí cada frase con split().
Convertí todas las palabras a minúsculas.
Ignorá los signos de puntuación (.,!?).
Mostrá el diccionario final ordenado alfabéticamente por clave.
frases = [
    "Hola mundo",
    "Mundo, hola!",
    "Python es genial",
    "Hola de nuevo",
]
"""
diccionario = {}

frases = [
    "Hola mundo",
    "Mundo, hola!",
    "Python es genial",
    "Hola de nuevo",
]

for frase in frases:
    for palabra in frase.split():
        palabra = palabra.lower()
        palabra = palabra.strip(".,;:!?")
        if palabra in diccionario:
            diccionario[palabra] = diccionario[palabra] + 1
        else:
            diccionario[palabra] = 1

for key in sorted(diccionario):
    print(f"{key}: {diccionario[key]}")