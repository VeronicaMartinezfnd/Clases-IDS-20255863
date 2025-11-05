correo = input()

un_arroba = correo.count("@") == 1
un_punto = correo.count(".") >= 1
antes = correo[0:3:1].count("@") == 0
despues = correo[-1:-4:1].count("@") == 0
espacio = correo.count(" ") == 0
inicio = correo[0] != "."
fin = correo[-1] != "."

valido = (un_arroba and un_punto and antes and despues and espacio and inicio and fin) == True

print(valido)

"""El correo contiene exactamente un @
Antes y después del @ debe haber al menos 3 caracteres
El correo debe contener al menos un punto
El correo no puede contener espacios
El correo no puede iniciar ni terminar con un punto"""