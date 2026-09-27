# ============================================================
# UNIDAD 07 - Nivel simple - Ejercicio 1
# ============================================================
#
# Solicitar al usuario que ingrese 5 numeros enteros uno por uno
# y almacenarlos en una lista usando append().
# Al terminar, imprimir la lista completa.
#
# Ejemplo de salida:
#   Lista ingresada: [10, 3, 7, 25, 1]
# ============================================================

lista_enteros = []

# 💡 Sugerencia: como i no se usa adentro del for, la convención es
# llamarla _ (for _ in range(5)).
for i in range(5):
    numero = int(input("Ingrese un numero entero: "))
    lista_enteros.append(numero)

print(f"Lista ingresada: {lista_enteros}")