# Parcial 01

## ✅ Recomendaciones

(Ver también el archivo [`Importante.md`](Importante.md))

- Leé **muy bien** el enunciado de cada ejercicio antes de empezar.
- Hacé un pseudocódigo o un diagrama de flujo para pensar la solución antes de
  escribir código.
- Pensá el **algoritmo** antes de tirar líneas.
- Dividí en **funciones pequeñas**, cada una con una sola responsabilidad, y
  llamálas desde el archivo principal.
- Resolvé primero que **funcione**; después refactorizá para que quede
  prolijo.
- En esa refactorización, evaluá si hace falta **validar la entrada del
  usuario**.
- La parte teórica (si la hubiera) podés escribirla como comentario o hacer
  que se imprima en pantalla al ejecutar el script.

---

## 📝 Ejercicios

### Ejercicio 1 — Buscar y Reemplazar en una Lista
Definí `buscar_reemplazar(lista, palabra, reemplazo)` que reciba una lista de
strings y devuelva una **nueva lista** donde todas las ocurrencias de `palabra`
estén reemplazadas por `reemplazo`.

### Ejercicio 2 — Validar Email
Definí `validar_email(email)` que retorne `True` si el email cumple **todas**
las reglas de formato indicadas en el archivo, o `False` en caso contrario.

### Ejercicio 3 — Análisis de una Lista de Números
Dada una lista de enteros, mostrar la lista original, su valor **máximo** y
**mínimo**, la lista **ordenada** de menor a mayor y los números **mayores
a 5**. **Sin usar** `sorted()`, `max()` ni `min()`: hay que recorrer la lista
con bucles.

### Ejercicio 4 — Juego de Adivinanza de Palabras con Módulo
Definí `jugar_adivinanza(palabra_secreta)` que implemente un juego tipo
ahorcado **sin dibujo**: el usuario ingresa letras de a una, se muestra el
progreso con guiones bajos y el juego termina al adivinar la palabra o tras
**5 errores** acumulados. Las funciones auxiliares deben estar en un módulo
separado `juego.py` con docstrings.

---

## 🎯 Puntaje

| Ejercicio | Puntos |
|:---------:|:------:|
| 1 | 25% |
| 2 | 25% |
| 3 | 25% |
| 4 | 25% |

**Aprobación con nota 4 = 60% bien hecho del examen.**

---