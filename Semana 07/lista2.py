nombres = ["Ana", "Antonio", "Paulina", "Jose"]
print(nombres)
nombres[2] = "Pablo"
print(nombres)
#nombres.append("Hazel")
#.insert = tiene dos parámetros: en que indice lo quiero agregrar(en qué posición: 0...) y qué quiero agregar
nombres.append(input("Ingrese el nuevo nombre: "))
print(nombres)
#nombres.insert(3, "Vero")
#nombres.insert(int(input("Indique el índice: ")), "Vero")
nombres.insert(int(input("Indique el índice: ")), input("Nombre: "))
print(nombres)
nombres.remove("Vero")
print(nombres)
"""nombre_deleted = nombres.pop(int(input("Indice a borrar: "))-1)
print(nombres)
print(nombre_deleted)"""