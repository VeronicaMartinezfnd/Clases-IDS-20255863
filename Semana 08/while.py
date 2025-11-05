"""inicio = 0
maximo = 5

while inicio < maximo:
    print("Saludo")
    inicio = inicio + 1
"""
presupuesto = 1000

gasto = 0

while gasto <= presupuesto:
    compra = float(input("Digite el valor de la compra: "))
    gasto += compra
gasto -= compra
print(f"{gasto:.0f}")