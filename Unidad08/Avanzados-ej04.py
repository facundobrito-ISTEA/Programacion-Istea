"""## 📊 Ejercicio 4 — Registro de estudiantes (menú interactivo)

Construí un programa para gestionar un registro de estudiantes. Usá un
diccionario donde la **clave** sea el ID del estudiante y el **valor** una tupla
`(nombre, edad, promedio)`.

El programa debe mostrar este menú en bucle hasta que el usuario elija salir:

1. Agregar estudiante
2. Listar todos los estudiantes
3. Buscar estudiante por ID
4. Eliminar estudiante por ID
5. Salir

> 💡 Usá un `while True` con `if/elif/else`. Validá que el ID exista antes de
> buscar o eliminar.
"""

id_siguiente = 1
estudiantes = {}


def menu() -> None:
    """Muestra por pantalla las opciones del menú."""
    print("1. Agregar estudiante")
    print("2. Listar todos los estudiantes")
    print("3. Buscar estudiante por ID")
    print("4. Eliminar estudiante por ID")
    print("5. Salir")


def pedir_opcion() -> int:
    """Muestra el menú y pide una opción hasta que sea válida.

    Retorna:
        int: Opción elegida, un número del 1 al 5.
    """
    menu()
    while True:
        opcion = input("Elija la opción deseada: ")
        if opcion.isdigit():
            opcion_num = int(opcion)
            if opcion_num >= 1 and opcion_num <= 5:
                return opcion_num

        print("Debe elegir un número del 1 al 5")
        menu()


def esta_vacio(estudiantes: dict[int, tuple[str, int, float]]) -> bool:
    """Indica si el registro de estudiantes está vacío.

    Parámetros:
        estudiantes (dict): Registro con el ID como clave y la tupla
            (nombre, edad, promedio) como valor.

    Retorna:
        bool: True si no hay estudiantes, False si hay al menos uno.
    """
    if not estudiantes:
        return True
    else:
        return False


def pedir_texto(mensaje: str) -> str:
    """Pide un texto por teclado hasta que tenga al menos un carácter.

    Parámetros:
        mensaje (str): Texto que se muestra al pedir el dato.

    Retorna:
        str: Texto ingresado, sin espacios en los extremos y con un
            solo espacio entre palabras.
    """
    while True:
        texto = input(mensaje)
        texto_limpio = texto.lstrip()
        texto_limpio = texto_limpio.rstrip()
        while "  " in texto_limpio:
            texto_limpio = texto_limpio.replace("  ", " ")
        if texto_limpio == "":
            print("No puede estar vacío, debe tener al menos un carácter")
        else:
            return texto_limpio


def pedir_numero(mensaje: str, minimo: float, maximo: float) -> float:
    """Pide un número por teclado hasta que esté dentro del rango.

    Parámetros:
        mensaje (str): Texto que se muestra al pedir el dato.
        minimo (float): Valor mínimo permitido.
        maximo (float): Valor máximo permitido.

    Retorna:
        float: Número ingresado, entre minimo y maximo.
    """
    while True:
        try:
            numero = float(input(mensaje))
            if numero >= minimo and numero <= maximo:
                return numero
            print(f"Debe estar entre {minimo} y {maximo}")
        except ValueError:
            print("Debe ingresar un número válido")


while True:
    eleccion = pedir_opcion()

    if eleccion == 1:
        nombre = pedir_texto("Ingrese el nombre: ")
        edad = int(pedir_numero("Ingrese la edad: ", 0, 120))
        promedio = pedir_numero("Ingrese el promedio: ", 0, 10)
        estudiantes[id_siguiente] = (nombre, edad, promedio)
        print(
            f"El estudiante {nombre} "
            f"fue agregado con el ID: {id_siguiente}")
        id_siguiente = id_siguiente + 1

    elif eleccion == 2:
        if esta_vacio(estudiantes):
            print("_")
            print("No hay estudiantes para mostrar")
            print("Elija otra opción")
            print("_")
        else:
            for id_estudiante, (nombre, edad, promedio) in estudiantes.items():
                print(f"ID: {id_estudiante}")
                print(f"Nombre: {nombre}")
                print(f"Edad: {edad}")
                print(f"Promedio: {promedio}")
                print("_")

    elif eleccion == 3:
        if esta_vacio(estudiantes):
            print("No hay estudiantes para buscar")
            print("_")
        else:
            try:
                id_buscado = input("Ingrese el ID a buscar: ")
                id_buscado = int(id_buscado)

                if id_buscado in estudiantes:
                    nombre, edad, promedio = estudiantes[id_buscado]
                    print(f"ID: {id_buscado}")
                    print(f"Nombre: {nombre}")
                    print(f"Edad: {edad}")
                    print(f"Promedio: {promedio}")
                    print("_")
                else:
                    print("No existe el ID buscado")
            except ValueError:
                print("El ID debe ser un número")

    elif eleccion == 4:
        if esta_vacio(estudiantes):
            print("No hay estudiantes para eliminar")
            print("_")
        else:
            try:
                id_a_eliminar = input("Ingrese el ID a eliminar: ")
                id_a_eliminar = int(id_a_eliminar)
                if id_a_eliminar in estudiantes:
                    nombre, edad, promedio = estudiantes[id_a_eliminar]
                    print(f"El estudiante {nombre} "
                          f"con el ID: {id_a_eliminar} fue eliminado")
                    del estudiantes[id_a_eliminar]
                else:
                    print("No existe el ID a eliminar")
            except ValueError:
                print("El ID a eliminar debe ser un número")

    elif eleccion == 5:
        break
