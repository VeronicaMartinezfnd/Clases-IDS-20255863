n = int(input())
v1, v2, v3 = map(int, input().split(' '))
combos = []

for i in range(0,n):
    combos.append(input())
    
    a = combos[i].count("A") * v1
    b = combos[i].count("B") * v2
    c = combos[i].count("C") * v3
        
    total = a + b + c
    print(total)