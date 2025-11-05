""""Indicaciones
Después de un largo día de clases, Alvin tiene hambre y decide pedir su cena usando un programa que le desarrollaron sus estudiantes de Introducción al Desarrollo de Software. Actualmente, el programa aún está en desarrollo y tiene un menú bastante pequeño, que consta únicamente de 10 platos.

Para ayudar a Alvin a realizar su pedido correctamente, debes crear una tupla que contenga los platos disponibles en el menú del programa en el orden dado. El menú actualmente incluye los siguientes platos:








El programa debe permitir que Alvin elija el plato que desea introduciendo un número entero que representa el número del plato en el menú. Luego, para confirmar que la elección fue correcta, el programa debe mostrar el siguiente mensaje: El plato seleccionado por Alvin es: (nombre del plato)

Entrada
Un número entero n que representa el número del plato en el menú elegido por Alvin."""

platos = ("Hamburguesa","Hotdog","Pizza","Tacos","Lasaña","Ensalada","Pupusas","Burrito","Alitas de pollo","Papas fritas")

plato = int(input())

print(f"El plato seleccionado por Alvin es: {platos[plato - 1]}")