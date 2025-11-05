#Sistema de gestión de alumnos

menu_iniciado = True
alumnos = []

while menu_iniciado:
    opcion = int(input("1. Agregar, 2. Consultar, 3. Modificar, 4. Borrar, 5. Salir"))
    if opcion == 5:
        menu_iniciado = False
    elif opcion == 1:
        alumnos.append(input())
    elif opcion == 2:
        for a in alumnos:
            print(a)
    elif opcion == 3:
        indice = int(input("Digite el numero del alumno (1-3): "))
        borrado = input("Digite el nuevo nombre: ")
        alumnos[indice-1]= borrado
    elif opcion == 4:
        indice = int(input("Digite el numero del alumno (1-3) a popear: "))
        alumnos_borrado= alumnos.pop(indice-1)
        print(f"Hemos borrado a: {alumnos_borrado}")
    else:
        print("La opción elegida no es válida.")
        menu_iniciado = False

print("Gracias por usar nuestro sistema")