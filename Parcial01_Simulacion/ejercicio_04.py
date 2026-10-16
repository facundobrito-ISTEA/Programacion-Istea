"""
EJERCICIO 4 — Contar Apariciones en una Lista
###############################################

Escribí una función llamada `contar_apariciones(lista, elemento)` que reciba
una lista y un elemento, y devuelva cuántas veces aparece ese elemento en la lista.

Importante: no uses el método `.count()` de las listas.
Debés recorrer la lista con un bucle y contar manualmente.

Luego escribí otra función llamada `contar_todos(lista)` que reciba una lista
y devuelva un resumen de cuántas veces aparece cada elemento único.
El resultado debe imprimirse de esta forma (un elemento por línea):

    "manzana" aparece 3 veces
    "pera" aparece 1 vez
    "naranja" aparece 2 veces

Atención: si el conteo es 1, se escribe "vez" (singular); si es distinto de 1,
se escribe "veces" (plural). Tené en cuenta este detalle al armar el mensaje.

Probá las funciones con los siguientes ejemplos:

    frutas = ["manzana", "pera", "manzana", "naranja", "manzana", "naranja"]

    print(contar_apariciones(frutas, "manzana"))  # 3
    print(contar_apariciones(frutas, "pera"))     # 1
    print(contar_apariciones(frutas, "uva"))      # 0

    contar_todos(frutas)
    # manzana aparece 3 veces
    # pera aparece 1 vez
    # naranja aparece 2 veces

Nota: para `contar_todos` podés apoyarte en la función `eliminar_duplicados`
del ejercicio anterior, o resolverlo de otra manera.

"""


def contar_apariciones(lista, elemento):
    cantidad = 0
    for item in lista:
        if elemento == item:
            cantidad = cantidad + 1
    return cantidad



def eliminar_duplicados(lista):

    sin_duplicados = []

    for item in lista:
        if item not in sin_duplicados:
            sin_duplicados.append(item)

    return sin_duplicados


def contar_todos(lista):
    # ✅ Bien hecho: reutilizás tus dos funciones en vez de volver a escribir
    # la lógica, y el singular/plural de "vez" está bien resuelto.
    lista_sin_duplicado = eliminar_duplicados(lista)

    for item in lista_sin_duplicado:
        cantidad = contar_apariciones(lista, item)
        if cantidad == 1:
            palabra = "vez"
        else:
            palabra = "veces"

        print(f'"{item}" aparece {cantidad} {palabra}')


frutas = ["manzana", "pera", "manzana", "naranja", "manzana", "naranja"]

print(contar_apariciones(frutas, "manzana"))  # 3
print(contar_apariciones(frutas, "pera"))     # 1
print(contar_apariciones(frutas, "uva"))      # 0

contar_todos(frutas)
# manzana aparece 3 veces
# pera aparece 1 vez
# naranja aparece 2 veces
