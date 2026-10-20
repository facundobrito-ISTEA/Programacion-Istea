"""Ejercicio 3 — Distancia entre ciudades
Usá el siguiente diccionario de coordenadas:

coordenadas = {
    "Buenos Aires": (-34.6037, -58.3816),
    "Madrid":       ( 40.4168,  -3.7038),
    "Roma":         ( 41.9028,  12.4964),
    "Tokio":        ( 35.6895, 139.6917),
}
Implementá una función distancia(ciudad_a, ciudad_b) que calcule la distancia euclidiana simplificada:

distancia = √((x2 - x1)² + (y2 - y1)²)
Pedile al usuario que elija dos ciudades por nombre y mostrá la distancia entre ellas.

💡 La fórmula es geométrica, no geográfica real. Es a fines didácticos.
"""

from math import sqrt, pow

coordenadas = {
    "Buenos Aires": (-34.6037, -58.3816),
    "Madrid":       (40.4168,  -3.7038),
    "Roma":         (41.9028,  12.4964),
    "Tokio":        (35.6895, 139.6917),
}


def validar_ciudad(coordenadas, ciudad="_"):

    ciudad_elegida = input("Ingrese la ciudad elegida: ")

    while ciudad_elegida not in coordenadas or ciudad_elegida == ciudad:
        if ciudad_elegida not in coordenadas:
            print("Elija una de las ciudades disponibles")
        else:
            print("Las ciudades elegidas no pueden ser las mismas")

        ciudad_elegida = input("Ingrese la ciudad elegida: ")
    return ciudad_elegida


def distancia(ciudad_a, ciudad_b):
    referencias_1 = coordenadas[ciudad_a]
    referencias_2 = coordenadas[ciudad_b]

    x1 = referencias_1[0]
    y1 = referencias_1[1]
    x2 = referencias_2[0]
    y2 = referencias_2[1]

    distancia_ciudades = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    return distancia_ciudades


print("Entre las siguientes ciudades:")
for ciudad in coordenadas:
    print(ciudad)
print("Elija 2 para mostrarle la distancia entre ellas")
ciudad_1 = validar_ciudad(coordenadas)
ciudad_2 = validar_ciudad(coordenadas, ciudad_1)

distancia_entre_ciudades = distancia(ciudad_1, ciudad_2)

print(
    f"La distancia entre {ciudad_1} y {ciudad_2} es de {distancia_entre_ciudades:.2f} grados")
