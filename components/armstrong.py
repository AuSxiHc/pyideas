a = input("Enter number: ")
clone = int(a)
l = len(a)
n = int(a)
s = 0
for i in range(l):
    s += (n%10)**3
    n //= 10
if clone == s:
    print("Armstrong")
else:
    print("Noodle arms :>")