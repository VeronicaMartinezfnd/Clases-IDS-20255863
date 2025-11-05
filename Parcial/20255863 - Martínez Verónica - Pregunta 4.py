#Este es el problema D.Palíndromo

cadena = input()

verdadero = cadena.lower() == cadena[::-1].lower()

print(verdadero)