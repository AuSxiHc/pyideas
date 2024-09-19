a = input("Enter number: ")
l = len(a)
n = int(a)
s = 0
for i in range(l):
    s += n%10
    n //= 10
if int(a)==s:
    print("Its perfect...")
else:
    print("Wont work out vro")