# 1/1! + 2/2! + 10/3! + 34/4! + 154/5!... till n terms

import math as m #Illegal but I got no time

n = int(input("Enter number: "))
a = 1

for i in range(1,n):
    print((i*a)+m.pow(-1,i))
    