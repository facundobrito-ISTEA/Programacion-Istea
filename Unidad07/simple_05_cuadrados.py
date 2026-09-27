# ============================================================
# UNIDAD 07 - Nivel simple - Ejercicio 5
# ============================================================
#
# Crear una lista con los numeros del 1 al 10.
# Usando un bucle for, calcular el cuadrado de cada numero
# y almacenarlo en una nueva lista.
# Imprimir la lista de cuadrados resultante.
#
# Ejemplo de salida:
#   Cuadrados: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# ============================================================

lista_numeros = []
lista_cuadrados = []

for numero_generado in range(1, 11):
    lista_numeros.append(numero_generado)

for numero in lista_numeros:
    cuadrado = numero ** 2
    lista_cuadrados.append(cuadrado)

print(f"Números: {lista_numeros}")
print(f"Cuadrados: {lista_cuadrados}")