"""numeros = ["uno", "dos", "tres", "cuatro"]
numeros1 = ["uno", "Dos", "tres", "cuatro"]
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])"""

"""nombre = "Antonio"
print(nombre.count("n"))
print(nombre.count("o"))
print(nombre.count("t"))
print(nombre.count("a"))
print(nombre.lower().count("a"))"""

"""print(numeros.count("dos"))
print(numeros1[1].lower().count("dos"))"""

nombres = ["Ana","Antonio","Ana","Jose"]
print(len(nombres[0]))
print(nombres.count("Ana"))
print(nombres.count("Luis"))
r_a = 0
r_a = r_a + nombres[0].lower().count("a")
r_a = r_a + nombres[1].lower().count("a")
r_a = r_a + nombres[2].lower().count("a")
r_a = r_a + nombres[3].lower().count("a")

print(r_a)
#print(nombres[0].lower().count("a"))