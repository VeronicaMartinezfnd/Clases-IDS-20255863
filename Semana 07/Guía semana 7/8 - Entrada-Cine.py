n = int(input())
edades = []
total = 0

for i in range(0,n):
    edades.append(int(input()))
    
for e in edades:
    if e >= 15:
        total +=1
print(total)