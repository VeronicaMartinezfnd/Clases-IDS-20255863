nombre = "Verónica"
palabra = "RECONOCER"
palabra2 = "ratón"

"""print(nombre[0:8:2])""" #La segunda vez que se pone el ':2' es para decirle de cuántos son los saltos que debe dar
"""print(palabra[4:9])"""#Si se pasa del número de las letras intuirá que nos referimos hata el final 
"""print(palabra[4:])"""#Si omito el segundo número intuirá que debe llegar hasta el final de la palabra
"""print(palabra[:4:])"""#Si omito ambos números intuirá que solo hablo de la cuarta posición de letra en la palabra (Recordá que los posicionamientos comienzan desde 0)

"""print(palabra[::-1])"""
"""print(palabra[::2])"""
print(palabra[1::3])
print(palabra2[::-1])

######################################################################################################

"""prueba = "carreton"

print(prueba==prueba[::-1])"""

prueba = "bob"

print(prueba==prueba[::-1])

num = 1234 #Si lo hiciera texto, es decir, ponerlo entre comillas 
print(len(prueba))#Si hubiese puesto la variable num me hubiera dado error ya que npo es iuna colección de letras como la variable prueba

edad = int(input())

#print(len(edad))

print(palabra.lower())
print(palabra2.upper())
print(palabra2.capitalize())

#Método: funciones que aplican a objetos
#incio:fin:salto