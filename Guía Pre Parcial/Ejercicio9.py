plato = int(input())
complemento = int(input())

platos = ("Hamburguesa", "Pizza", "Tacos", "Pupusas", "Hotdog")
complementos = ("Papas fritas", "Alitas de pollo", "Ensalada", "Sopa", "Lasaña")

print(f"El pedido de Alvin es: {platos[plato - 1]} con {complementos[complemento - 1]}")