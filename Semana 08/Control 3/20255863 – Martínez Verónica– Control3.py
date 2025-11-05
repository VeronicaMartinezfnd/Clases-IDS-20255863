# Si se quiere ver la línea de comentario en párrafos ejecutar el comando (alt + z)
#Creación de variables
#Se le asigna un valor a la variable agente, asimismo, se crean dos listas vacias para manipularlas más adelante

agente = "encargado"
platillo = []
precios = []

#Ingreso a la aplicación
#Se le pide al usuario ingresar el nombre del agente por medio  y si este concuerda con el valor creado con anterioridad lo dejará pasar al siguiente bucle, de lo contrario, se le mostrará un mensaje de que dicho agente no está registrado

comprobar = False
while comprobar != True:
    if input("Favor ingrese el nombre del agente: ").lower() == agente:
        comprobar = True
    else:
        print("Agente no registrado")
        
#Gestión del menú principal
# Se crea un bucle infinito para manipular las diversas opciones que se le brindarán al usuario para gestionar su menu 

menu = True

while menu == True:
    opcion = int(input("1. Creación de platillos, 2. Consulta de platillos y precios, 3. Colocar pedido, 4. Salir: "))
    
     #Salir
     # Por medio de una condicional se crea el efecto de la opción 4 que es salir, ya que al digitar 4 se reemplazará el valor de menu y no se permitirá continuar el bucle ya que el bucle se ejecuta solo cuando menu = True
    
    if opcion == 4:
        menu = False
        
     #Creación de platillos
     #Por medio de otra condicional dentro del bucle se crean dos inputs uno de tipo string y el otro de tipo número, donde el usuario ingresa un platillo y su respectivo precio
        
    elif opcion == 1:
        platillo.append(input("Ingrese el nombre del platillo a crear: ").lower())
        precios.append(float(input("Ingrese el precio del platillo a crear: ")))
        
     #Consulta de platillos
     #Por medio de una condicional dentro de la condicional original mostramos los platillos existentes y si no los hay mostrará un mensaje haciendole saber al usuario que la lista de platillos está vacía
        
    elif opcion == 2:
        if platillo == []:
            print("Actualmente no hay platillos ingresados")
        else:
            for a in range(len(platillo)):
                print(f"{platillo[a]}: ${precios[a]}")
     
     #Colocar un pedido
     #Como en la opción anterior tenemos una condicional dentro de otra y por medio de un input se le pide al usuario indicar el platillo de su orden y si este no existe se le comunica la inexistencia de dicho platillo y se le devuelve al bucle
     
    elif opcion == 3:
        plato = input("Indique el nombre del platillo para su orden: ")
        if plato.lower() in platillo:
            print(f"Usted ha elegido {plato.lower()} con un precio de ${precios[platillo.index(plato.lower())]}")
        else:
            print("Ese platillo no existe")
            menu = True