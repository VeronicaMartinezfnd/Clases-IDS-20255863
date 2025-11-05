n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

numeros = [n1, n2, n3, n4, n5, n6]

mayor = max(numeros)
menor = min(numeros)
diferencia = mayor - menor
total_sum =(n1 + n2 + n3 + n4 + n5 + n6)
promedio = (n1 + n2 + n3 + n4 + n5 + n6)/6

print(f"Maximo: {mayor:.2f}")
print(f"Minimo: {menor:.2f}")
print(f"Diferencia: {diferencia:.2f}")
print(f"Suma: {total_sum:.2f}")
print(f"Promedio: {promedio:.2f}")