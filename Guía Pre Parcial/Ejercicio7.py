nombre = input()
apellido = input()

pin = (len(nombre) * 1000 + len(apellido)) % 10000
nick = nombre[0:5].lower() + apellido [0].lower()

print(f"Nick: {nick}")
print(f"Pin: {pin}")
print(f"ID: C3-{nick}-{pin}")