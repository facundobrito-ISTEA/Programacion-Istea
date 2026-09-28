# ============================================================
# UNIDAD 07 - Nivel simple - Ejercicio 3
# ============================================================
#
# Escribir una funcion llamada primeros_diez_pares(numeros) que reciba
# una lista de numeros como parametro y retorne una nueva lista con
# los primeros 10 numeros pares que encuentre en esa lista.
# Si hay menos de 10 pares, retornar solo los que haya.
#
# Ejemplo de uso:
#   entrada = [1, 4, 7, 2, 9, 6, 8, 3, 10, 12, 5, 14, 16, 18, 20, 22]
#   resultado = primeros_diez_pares(entrada)
#   print(resultado)  # [4, 2, 6, 8, 10, 12, 14, 16, 18, 20]
# ============================================================

def primeros_diez_pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
            if len(pares) == 10:
                break

    return pares


entrada01 = [1, 4, 7, 2, 9, 6, 8, 3, 10, 12, 5, 14, 16, 18, 20, 22]
resultado = primeros_diez_pares(entrada01)
print(f"La lista original es: {entrada01}")
print(f"Los pares encontrados son (hasta 10): {resultado}")
print()
entrada02 = [1, 4, 80, 90]
resultado = primeros_diez_pares(entrada02)
print(f"La lista original es: {entrada02}")
print(f"Los pares encontrados son (hasta 10): {resultado}")
