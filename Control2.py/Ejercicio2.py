""""¡Felicitaciones por ayudar a Alvin a elegir su plato! 🎉

Gracias a ti, Alvin pudo continuar con su pedido y ahora es un cliente frecuente del programa. Pero otro día mientras Alvin realizaba un pedido, se dio cuenta de una catástrofe: ¡le estaban cobrando más de 50 dólares por su plato! Al parecer, los estudiantes que llenaron la información del programa se distrajeron jugando Silksong y colocaron mal los precios de algunos platos.

Los precios actuales de los 10 platos son:

Hamburguesa — 
Hotdog — 
Pizza — 
Tacos — 
Lasaña — 
Ensalada — 
Pupusas — 
Burrito — 
Alitas de pollo — 
Papas fritas — 
Para salvar la billetera de Alvin y lograr que pueda disfrutar de su cena, debes corregir los precios mal ingresados. Tu misión es:

Crear una lista con los precios actuales de los platos en el orden dado.
Leer dos entradas:

El primer valor de cada par indica el número del plato en el menú
El segundo valor de cada par es el nuevo precio del plato
Actualizar los precios en la lista según los valores ingresados (no alterar los números decimales) y mostrar la lista completa con el mensaje:

Los precios actualizados son: [lista completa de precios]

Entrada
Dos líneas, cada una con un valor:

Primera línea: número del plato en el menú a corregir
Segunda línea: nuevo precio del plato (decimal)

Salida
Un mensaje con el formato:

Los precios actualizados son: [lista completa de precios]
donde [lista completa de precios] es la lista después de aplicar los cambios.
"""
precios = [3.52, 55.15, 4.25, 60.25, 5.65, 3.15, 2.65, 70.75, 6.25, 2.55]

plato = int(input())
precio = float(input())

precios[plato - 1] =  precio

print(f"Los precios actualizados son: {precios}")