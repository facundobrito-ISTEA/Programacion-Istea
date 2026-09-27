# ============================================================
# UNIDAD 07 - Nivel simple - Ejercicio 7
# ============================================================
#
# Crear una funcion llamada buscar_elemento(lista, elemento) que busque
# un elemento especifico dentro de una lista y retorne su indice
# si lo encuentra, o el mensaje "Elemento no encontrado" si no esta.
# No usar el metodo index() de Python; hacer la busqueda con un bucle.
#
# Ejemplo de uso:
#   buscar_elemento([1, 2, 3, 4, 5], 3)   # retorna 2
#   buscar_elemento([1, 2, 3, 4, 5], 9)   # retorna "Elemento no encontrado"
# ============================================================

def buscar_elemento(lista, elemento_a_buscar):
    for indice in range(len(lista)):
        elemento = lista[indice]
        if elemento == elemento_a_buscar:
            return indice
    
    return "Elemento no encontrado"

# 💡 Sugerencia (PEP 8): dejá dos líneas en blanco después de una función.
# También hay espacios al final de la línea en blanco dentro de la función.
numeros = [1, 2, 3, 4, 5]
buscado = 3
resultado = buscar_elemento(numeros, buscado)
print(f"Buscar {buscado} en {numeros}: {resultado}")
print()
buscado = 6
resultado = buscar_elemento(numeros, buscado)
print(f"Buscar {buscado} en {numeros}: {resultado}")