# ============================================================
# UNIDAD 07 - Nivel simple - Ejercicio 4 (version extendida)
# ============================================================
#
# Misma consigna que simple_04_split_strip.py, pero ademas
# descarta los elementos vacios que aparecen cuando el usuario
# pone comas de mas (por ejemplo: "manzana,, pera,").
#
# Como hay que descartar elementos, se arma una lista nueva
# y solo se agregan las palabras que no quedan vacias
# despues del strip().
# ============================================================

lista_palabras_depuradas = []

texto_ingresado = input("Ingrese un listado de palabras separadas por comas: ")

lista_palabras = texto_ingresado.split(",")

for item in lista_palabras:
    palabra = item.strip()
    # ✅ Bien hecho: muy buena idea la versión extendida para las comas de más.
    # 💡 Sugerencia: un string vacío es "falso", así que alcanza con `if palabra:`.
    if len(palabra) != 0:
        lista_palabras_depuradas.append(palabra)

print(f"Lista original: {lista_palabras}")
print(f"Lista depurada: {lista_palabras_depuradas}")