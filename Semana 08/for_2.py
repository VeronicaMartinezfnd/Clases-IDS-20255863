numeros = [1, 2, 3, 4]
#print(len(numeros))
"""for x in numeros:
    print("Hola")
"""
palabra = "Aulas"
#print(len(palabra))

"""for x in palabra:
    print("Hola")
"""

"""dias = ["Lunes", "Martes", "Miercoles",
        "Jueves", "Viernes", "Sabado", "Domingo"]
"""
"""for x in dias[2]:
    print(x)
"""
"""for x in dias:
    print(x[:2])
"""
"""for i in range(0,10,2):
    print(i)
"""
personas = ["Ana", "Luis", "Luisa"]

"""for p in personas:
    print(p[0])
"""
"""for p in personas:
    for l in p:
        print(l)
"""
"""valores = [[1, 3, 6], 
           [2, 7, 4], 
           [6, 5, 9], 
           [1, 10, 20]]
mayores = []

for i in valores:
    for j in i:
        if j > 6:
            mayores.append(j)
            
print(mayores)
"""

horas = [[8, 8, 9, 8, 10], 
         [7, 9, 10, 8, 7], 
         [7, 9, 10, 8, 8], 
         [8, 8, 10, 7, 11]]

mayores = []

"""for v in horas:
    for valorcito in v:
        if valorcito > 6:
            mayores.append(valorcito)

print(mayores)
"""
minimo = int(input())

for v in horas:
    for valorcito in v:
        if valorcito > minimo:
            mayores.append(valorcito)

print(mayores)
