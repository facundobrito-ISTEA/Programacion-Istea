"""✅ Ejercicio 1 — Crear una tupla
Creá una tupla llamada `mis_datos` con tu nombre (string), tu edad (entero) y
tu ciudad (string). Imprimí la tupla completa. 
"""

mis_datos = ("Facundo", 44, "San Justo")
print(mis_datos)

"""✅ Ejercicio 2 — Acceder a elementos
Dada la tupla:
colores = ("rojo", "verde", "azul")
Imprimí el primer color usando un índice positivo.
Imprimí el último color usando un índice negativo.
"""
colores = ("rojo", "verde", "azul")
print(f"El primer color es: {colores[0]}")
print(f"El último color es: {colores[-1]}")

"""✅ Ejercicio 3 — Iterar sobre una tupla
Recorré la tupla colores con un bucle for e imprimí cada elemento en mayúsculas (usá el método .upper()).
"""
for color in colores:
    print(color.upper())

""" Ejercicio 4 — Operadores con tuplas
Dadas las tuplas:

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
Concatená ambas en una nueva tupla tupla_unida.
Multiplicá tupla1 por 2 y guardá el resultado en tupla_doble.
Imprimí ambas."""

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

tupla_unida = tupla1 + tupla2
tupla_doble = tupla1 * 2
print(tupla_unida)
print(tupla_doble)


print(type(tupla1 + tupla2))
print(type(tupla1 * 2))


""" Ejercicio 5 — Verificar pertenencia
Dada la tupla:

numeros = (10, 20, 30, 40, 50)
Verificá si el número 30 está dentro y mostrá un mensaje distinto según el caso (usá in con un if/else)."""

numeros = (10, 20, 30, 40, 50)

if 30 in numeros:
    print("El número 30 está dentro de la tupla")
else:
    print("El número 30 no está dentro de la tupla")

"""✅ Ejercicio 6 — Crear un diccionario
Creá un diccionario llamado mi_perfil con las claves "nombre", "apellido", "edad" y "ciudad". Asignales tus datos como valores e imprimí el diccionario completo."""

mi_perfil = {
    "nombre": "Facundo",
    "apellido": "Brito",
    "edad": 44,
    "ciudad": "San Justo"
}
print(mi_perfil)

"""✅ Ejercicio 7 — Acceder a un valor
Usando el diccionario anterior, imprimí únicamente el valor de la clave "ciudad"."""

print(mi_perfil["ciudad"])

"""✅ Ejercicio 8 — Modificar un valor
Cambiá el valor asociado a "edad" en mi_perfil y mostrá el diccionario actualizado."""

mi_perfil["edad"] = 50
print(mi_perfil)

"""✅ Ejercicio 9 — Agregar una clave nueva
Agregá la clave "correo" con un mail ficticio e imprimí el resultado."""

mi_perfil["correo"] = "a@a.com"
print(mi_perfil)

"""✅ Ejercicio 10 — Eliminar una clave
Eliminá la clave "apellido" del diccionario mi_perfil y mostrá el resultado final."""
del mi_perfil["apellido"]
print(mi_perfil)

"""🔄 Combinando tuplas y diccionarios
✅ Ejercicio 11 — Diccionario con tuplas como valores
Creá un diccionario coordenadas donde las claves sean nombres de ciudades y los valores tuplas con (latitud, longitud).

coordenadas = {
    "Buenos Aires": (-34.6037, -58.3816),
    "Madrid": (40.4168, -3.7038),
}
Imprimí las coordenadas de una ciudad específica (por ejemplo, "Madrid")."""

coordenadas = {
    "Buenos Aires": (-34.6037, -58.3816),
    "Madrid": (40.4168, -3.7038),
}

print(f"Las coordenadas de Madrid son: {coordenadas['Madrid']}")

"""✅ Ejercicio 12 — Iterar sobre el diccionario
Recorré el diccionario del ejercicio anterior con un for y mostrá cada ciudad con el siguiente formato:

Ciudad: Buenos Aires → Latitud: -34.6037, Longitud: -58.3816
💡 Pista: usá .items() y desempaquetado de la tupla."""


print("\nCoordenadas de todos las ciudades:")
for ciudad, (lat, lon) in coordenadas.items():
    print(f"Ciudad: {ciudad} → Latitud: {lat}, Longitud: {lon}")