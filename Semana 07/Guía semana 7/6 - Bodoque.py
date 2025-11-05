nombres = []
n = int(input())

for i in range(0,n):
  nombres.append(input())
    
for l in range(0,n):
    if len(nombres[l]) >= 8:
      print("Si aguanto otro desarrollo de personaje")
    elif len(nombres[l]) <= 6:
      print("No vale la pena")
    elif len(nombres[l]) > 6 and len(nombres[l]) < 8:
      print("Dios no creo aguantar esta vez")