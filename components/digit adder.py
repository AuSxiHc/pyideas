a = input("Enter number: ")
l = len(a)
n = int(a)
s = 0
for i in range(l):
    s += n%10
    n //= 10
print("Sum of digits:",s)