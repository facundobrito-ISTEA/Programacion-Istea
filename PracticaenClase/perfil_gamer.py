# ============================================================
# PRACTICA EN CLASE - Grupo 3: El generador de perfil gamer
# (Unidades 2 y 3)
# ============================================================
#
# Pedir nombre, apellido, anio de nacimiento y un numero del
# 1 al 4 para la clase del personaje. Mostrar:
#   - Tag de usuario: NOMBRE + APELLIDO + "_" + edad + "_GG"
#     (ejemplo: "LUCASGOMEZ_26_GG")
#   - Clase: 1-Guerrero, 2-Mago, 3-Arquero, 4-Sanador,
#     otro numero -> "Clase desconocida"
#   - Nivel inicial: (2026 - anio de nacimiento) // 5
#   - Estado: "Veterano" si el nivel es >= 5, si no "Novato"
# ============================================================

nombre = input("Ingresá tu nombre: ")
apellido = input("Ingresá tu apellido: ")
anio = int(input("Ingresá tu año de nacimiento: "))
clase = input("Elegí tu clase (1-Guerrero, 2-Mago, 3-Arquero, 4-Sanador): ")
clase = int(clase)

edad_jugador = 2026 - anio
tag = nombre.upper() + apellido.upper() + "_" + str(edad_jugador) + "_GG"

print("=== TU PERFIL GAMER ===")
print("Tag de usuario: " + tag)

if clase == 1:
    print("Clase: Guerrero 🗡️")
elif clase == 2:
    print("Clase: Mago 🔮")
elif clase == 3:
    print("Clase: Arquero 🏹")
elif clase == 4:
    print("Clase: Sanador 💚")
else:
    print("Clase desconocida")

nivel = edad_jugador // 5

print("Nivel inicial: " + str(nivel))

if nivel >= 5:
    print("Estado: Veterano")
else:
    print("Estado: Novato")