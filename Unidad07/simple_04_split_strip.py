# ============================================================
# UNIDAD 07 - Nivel simple - Ejercicio 4
# ============================================================
#
# Pedirle al usuario que ingrese una serie de palabras separadas
# por comas en una sola linea (por ejemplo: "manzana, pera, uva, naranja").
# Convertir esa cadena en una lista usando el metodo split(",").
# Limpiar los espacios de cada elemento con strip().
# Imprimir la lista resultante.
#
# Ejemplo de salida:
#   Lista: ['manzana', 'pera', 'uva', 'naranja']
# ============================================================

texto_ingresado = input("Ingrese un listado de palabras separadas por comas: ")

lista_palabras = texto_ingresado.split(",")

for indice in range(len(lista_palabras)):
    palabra = lista_palabras[indice].strip()
    lista_palabras[indice] = palabra

print(f"Lista: {lista_palabras}")