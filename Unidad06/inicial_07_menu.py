# ============================================================
# UNIDAD 06 - Ejercicios basicos de funciones - Ejercicio 7
# ============================================================
#
# Menu de Opciones:
# Crear una funcion mostrar_menu() que no reciba parametros e imprima
# en pantalla un menu con al menos 3 opciones.
#
# Luego, en el programa principal, llamar a mostrar_menu() y pedirle
# al usuario que elija una opcion. Imprimir cual eligio.
#
# Salida esperada:
#   === MENU PRINCIPAL ===
#   1. Saludar
#   2. Sumar dos numeros
#   3. Salir
#   Elige una opcion: _
# ============================================================

def mostrar_menu():

    print("=== MENU PRINCIPAL ===")
    print("1. Saludar")
    print("2. Sumar dos numeros")
    print("3. Salir")


mostrar_menu()

opcion = int(input("Elige una opcion: "))

if opcion == 1:
    print("Eligió la opción 1. Saludar")
elif opcion == 2:
    print("Eligió la opción 2. Sumar dos numeros")
elif opcion == 3:
    print("Eligió la opción 3. Salir")
else:
    print("Eligió una opcion incorrecta")
