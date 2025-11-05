q1= int(input())
q2= int(input())
q3= int(input())
q4= int(input())
q5= int(input())

p1= float(input())
p2= float(input())
p3= float(input())
p4= float(input())
p5= float(input())

puntos = [q1, q2, q3, q4, q5]
porcentaje = [p1, p2, p3, p4, p5]

total1= q1 * p1
total2= q2 * p2
total3= q3 * p3
total4= q4 * p4
total5= q5 * p5

total_final = total1 + total2 + total3 + total4 + total5

print(f"{total_final:.0f}")