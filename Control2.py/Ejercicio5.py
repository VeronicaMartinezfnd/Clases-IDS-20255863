"""La primera línea presenta un único entero M, la cantidad de veces que se debe imprimir la cadena B.
La siguiente línea, un único entero S, los saltos entre caracteres que se deben imprimir en la cadena A.
La tercera línea, contiene la cadena A.
La última línea, presenta la cadena B."""

m = int(input())
s = int(input())

a= input()
b= input()

print(f"{a[0::s]}_Alvin{b * m}")

