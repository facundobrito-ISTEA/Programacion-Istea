"""📈 Ejercicio 2 — Análisis de ventas por producto
Tenés un diccionario donde la clave es el nombre del producto y el valor es una tupla con las ventas mensuales.

ventas = {
    "Producto A": (1200, 1500, 900),
    "Producto B": (800, 700, 1000),
    "Producto C": (2000, 1800, 1700),
}
Escribí un programa que:

Calcule el total de ventas de cada producto.
Determine cuál producto vendió más en total.
Imprima un ranking de productos ordenado de mayor a menor.
"""

ventas = {
    "Producto A": (1200, 1500, 900),
    "Producto B": (800, 700, 1000),
    "Producto C": (2000, 1800, 1700),
}


suma_producto_total = {}

for nombre, ventas_mensuales in ventas.items():
    suma_total = 0
    for valor in ventas_mensuales:
        suma_total = suma_total + valor
    suma_producto_total[nombre] = suma_total

ranking = []
for nombre, producto_total in suma_producto_total.items():
    ranking.append((producto_total, nombre))

ranking_ordenado = sorted(ranking, reverse=True)

print(
    f"El producto que más vendió es el {ranking_ordenado[0][1]}, con un total de ventas de {ranking_ordenado[0][0]}")

print("El ranking de productos vendidos de mayor a menor es:")
for producto_total, nombre in ranking_ordenado:
    print(f"{nombre}, con un total de ventas de {producto_total}")
