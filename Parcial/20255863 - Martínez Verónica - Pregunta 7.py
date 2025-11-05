#Este es el problema G. Validacion de DUI

dui = input()

guion = dui[8] == "-"
largo = len(dui) == 10
ultimo = int(dui[-1])
entero = ultimo == int(dui[-1])

validar = (guion and largo and entero) == True

print(validar)