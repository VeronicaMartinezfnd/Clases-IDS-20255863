monto = int(input("Digite el monto: "))
tipo = input("Digite si el impuesto es local o extranjero: ")

if monto > 500: 
    if tipo.lower() == "local":
        local = 0.1
        print(f"Impuesto local: {local}")
    else:
        export = 0.14
        print(f"Impuesto exportación: {export}")  
elif monto > 200:
    if tipo.lower() == "local":
        local = 0.08
        print(f"Impuesto local: {local}")
    else:
        export = 0.12
        print(f"Impuesto exportación: {export}")
elif monto > 50:
    if tipo.lower() == "local":
        local = 0.06
        print(f"Impuesto local: {local}")
    else:
        export = 0.1
        print(f"Impuesto exportación: {export}")
else:
    print("Sus impuestos son de 0")