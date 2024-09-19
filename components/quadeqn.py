import math as m
a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))
c = int(input("Enter value of C: "))
d = m.pow(b,2)-4*a*c 
rt1 = (-b + m.sqrt(d))/2*a
rt2 = (-b - m.sqrt(d))/2*a
print("Roots =",-rt1,"and",-rt2)