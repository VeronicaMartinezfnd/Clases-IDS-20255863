x = int(input())
A = input()
B = input()

tamañoA = len(A)
tamañoB = len(B)

posicion = int(tamañoA/x) 
posicionB = int(tamañoB/x)

contraseña = A[0:posicion] + B[-posicionB:]

print(contraseña)