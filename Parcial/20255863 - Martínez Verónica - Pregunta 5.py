#Este es el problema E. Contiene Letra

palabra = input()
letra = input()

palabra1= palabra.lower()
letra1= letra.lower()

validacion = palabra1.count(letra1) >= 1

print(validacion)