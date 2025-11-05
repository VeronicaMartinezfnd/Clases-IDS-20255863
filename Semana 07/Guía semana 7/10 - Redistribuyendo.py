n = int(input())
SLs = []

for i in range(0,n):
    SLs.append(int(input()))
    
for e in SLs:
    if e >= 3:
        print("Ok")
    else:
        print("No")