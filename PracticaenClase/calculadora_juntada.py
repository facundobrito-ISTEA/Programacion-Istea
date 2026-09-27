# ============================================================
# PRACTICA EN CLASE - Grupo 2: La calculadora de la juntada
# (Unidades 2 y 3)
# ============================================================
#
# Escribir un programa que ayude a calcular cuanto paga cada
# persona cuando salen a comer con amigos.
#
# Pedir: total de la cuenta, cantidad de personas y si dejan
# propina (s/n). Si dejan propina, se agrega un 10% al total.
#
# Mostrar el total final, cuanto paga cada persona (redondeado
# a 2 decimales) y un mensaje segun el monto individual:
#   Menos de $5000         -> "¡Que barato, repitan!"
#   Entre $5000 y $10000   -> "Precio razonable."
#   Mas de $10000          -> "Hoy gastaron bien..."
# ============================================================

total = float(input("Ingrese el monto total de la cuenta a dividir: "))

personas = int(
    input("Ingrese el total de las personas que van a dividir la cuenta: "))

propina = input(
    "Ingrese s si desea dejar la propina y n si no desea dejar la propina: ")

# 💡 Sugerencia: si el usuario escribe "S" (mayúscula) o " s" (con espacio), no
# se suma la propina. Podés normalizar la respuesta:
# propina.strip().lower() == "s".
if propina == "s":
    total = total * 1.10
    total = round(total, 2)
    print("El total de la cuenta con propina es de $" + str(total))
else:
    print("El total de la cuenta es de $" + str(total))

# 💡 Sugerencia: si ingresan 0 personas, el programa se corta con
# ZeroDivisionError. Podrías validar que personas sea mayor a 0 antes de dividir.
por_persona = total / personas
por_persona = round(por_persona, 2)
print("Cada persona paga: $" + str(por_persona))

if por_persona < 5000:
    print("¡Qué barato, repitan!")
# 💡 Sugerencia: como el if anterior ya descartó los < 5000, alcanza con
# `elif por_persona <= 10000:`. Si querés dejarlo explícito, Python permite
# `5000 <= por_persona <= 10000`.
elif por_persona >= 5000 and por_persona <= 10000:
    print("Precio razonable.")
else:
    print("Hoy gastaron bien...")
